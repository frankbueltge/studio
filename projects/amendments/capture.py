#!/usr/bin/env python3
"""Capture the amendment history of registered clinical trials.

ClinicalTrials.gov publishes the complete version history of every registered
study record. This script fetches it and writes a frozen corpus.

Two endpoints, both reachable without authentication, both confirmed live
2026-08-16. Note what they are NOT: they sit in the `int` namespace, not in
the documented v2 API. `GET /api/v2/studies/{NCT}/history` returns 404. The
same history is exposed to any visitor at
`https://clinicaltrials.gov/study/{NCT}?tab=history` (confirmed 200, 2026-08-16),
so the data is public; the machine route to it is undocumented and carries no
stability guarantee. Any work built on this must freeze its own corpus and
must not promise that the route still answers tomorrow.

    https://clinicaltrials.gov/api/int/studies/{NCT}/history
        -> every version of the record: index, date, recruitment status,
           which modules changed at that version

    https://clinicaltrials.gov/api/int/studies/{NCT}/history/{version}
        -> the full record text as it stood at that version

Nothing here interprets. The script fetches, diffs the text of the promised
primary outcome measures between consecutive versions, and records every
change with both sides of it verbatim. Whether a given change is typographic
or substantive is NOT decided here; that coding is the work's problem and is
deliberately left out of the capture.

Usage:
    python3 capture.py sample   --n 100        # pick the study set, write studies.json
    python3 capture.py history                 # fetch every version list
    python3 capture.py diff     --limit 12     # fetch every version, diff outcomes
"""

import argparse
import calendar
import concurrent.futures as futures
import json
import os
import subprocess
import sys
import urllib.parse

HERE = os.path.dirname(os.path.abspath(__file__))
CORPUS = os.path.join(HERE, "corpus")
API = "https://clinicaltrials.gov/api"


def get(url, timeout=90):
    """Fetch JSON. curl rather than urllib: the host 403s urllib's default client."""
    proc = subprocess.run(
        ["curl", "-sS", "--max-time", str(timeout), url],
        capture_output=True, text=True,
    )
    if proc.returncode != 0:
        return None
    try:
        return json.loads(proc.stdout)
    except ValueError:
        return None


def sample(n):
    """The study set. Selection is stated here rather than described elsewhere."""
    params = {
        "pageSize": str(n),
        "filter.overallStatus": "COMPLETED",
        "query.term": (
            "AREA[StudyType]INTERVENTIONAL AND AREA[HasResults]true "
            "AND AREA[Phase]PHASE3"
        ),
        "fields": "NCTId,PrimaryCompletionDate,BriefTitle,LeadSponsorName",
    }
    data = get(f"{API}/v2/studies?" + urllib.parse.urlencode(params))
    out = []
    for study in data.get("studies", []):
        section = study["protocolSection"]
        out.append({
            "nct": section["identificationModule"]["nctId"],
            "title": section["identificationModule"].get("briefTitle"),
            "sponsor": section.get("sponsorCollaboratorsModule", {})
                              .get("leadSponsor", {}).get("name"),
            "primary_completion": section.get("statusModule", {})
                                         .get("primaryCompletionDateStruct", {})
                                         .get("date"),
        })
    return out


def history(nct):
    return get(f"{API}/int/studies/{nct}/history")


def outcomes_at(nct, version):
    """The promised primary outcome measures as the record stood at `version`."""
    data = get(f"{API}/int/studies/{nct}/history/{version}")
    if not data:
        return None
    protocol = data.get("study", {}).get("protocolSection", {})
    return [
        measure.get("measure", "").strip()
        for measure in protocol.get("outcomesModule", {}).get("primaryOutcomes", [])
    ]


def full_month(date):
    """Registry dates are either YYYY-MM or YYYY-MM-DD. Widen to a comparable form.

    A YYYY-MM primary completion date is treated as the LAST day of that month,
    which is the conservative choice: it can only move an amendment out of the
    "after the answer was in" set, never into it. The real last day is used, so
    the corpus never carries an impossible date.
    """
    if not date:
        return None
    if len(date) > 7:
        return date
    year, month = (int(part) for part in date.split("-"))
    return "%s-%02d" % (date, calendar.monthrange(year, month)[1])


def diff_study(entry):
    nct = entry["nct"]
    hist = history(nct)
    if not hist or "changes" not in hist:
        return None
    completion = full_month(entry.get("primary_completion"))
    if not completion:
        return None

    changes = hist["changes"]
    with futures.ThreadPoolExecutor(6) as pool:
        versions = list(pool.map(
            lambda change: (change["version"], change["date"], outcomes_at(nct, change["version"])),
            changes,
        ))
    versions = [v for v in versions if v[2] is not None]

    amendments = []
    for i in range(1, len(versions)):
        previous, current = versions[i - 1], versions[i]
        if previous[2] != current[2]:
            amendments.append({
                "version": current[0],
                "date": current[1],
                "after_primary_completion": current[1] > completion,
                "from": previous[2],
                "to": current[2],
            })

    return {
        "nct": nct,
        "sponsor": entry.get("sponsor"),
        "title": entry.get("title"),
        "primary_completion": completion,
        "versions": len(versions),
        "first_version": versions[0][1] if versions else None,
        "last_version": versions[-1][1] if versions else None,
        "amendments": amendments,
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("stage", choices=["sample", "history", "diff"])
    parser.add_argument("--n", type=int, default=100)
    parser.add_argument("--limit", type=int, default=12)
    args = parser.parse_args()

    os.makedirs(CORPUS, exist_ok=True)

    if args.stage == "sample":
        studies = sample(args.n)
        with open(os.path.join(CORPUS, "studies.json"), "w") as handle:
            json.dump(studies, handle, indent=1)
        print(f"studies: {len(studies)}")
        return

    with open(os.path.join(CORPUS, "studies.json")) as handle:
        studies = json.load(handle)

    if args.stage == "history":
        records = []
        with futures.ThreadPoolExecutor(8) as pool:
            for nct, hist in zip(
                [s["nct"] for s in studies],
                pool.map(lambda s: history(s["nct"]), studies),
            ):
                if hist and "changes" in hist:
                    records.append({"nct": nct, "versions": len(hist["changes"]),
                                    "changes": hist["changes"]})
        with open(os.path.join(CORPUS, "history.json"), "w") as handle:
            json.dump(records, handle, indent=1)
        print(f"records: {len(records)}  versions: {sum(r['versions'] for r in records)}")
        return

    if args.stage == "diff":
        results = []
        for entry in studies[: args.limit]:
            result = diff_study(entry)
            if not result:
                continue
            results.append(result)
            after = sum(1 for a in result["amendments"] if a["after_primary_completion"])
            print(f"  {result['nct']}  versions={result['versions']:3d}  "
                  f"outcome amendments={len(result['amendments'])}  after completion={after}")
        with open(os.path.join(CORPUS, "amendments.json"), "w") as handle:
            json.dump(results, handle, indent=1)
        studies_with = sum(1 for r in results if r["amendments"])
        studies_after = sum(1 for r in results
                            if any(a["after_primary_completion"] for a in r["amendments"]))
        print()
        print(f"studies read: {len(results)}")
        print(f"  with any primary-outcome text amendment:      {studies_with}")
        print(f"  with one after the primary completion date:   {studies_after}")


if __name__ == "__main__":
    sys.exit(main())
