# ONLY THE CONFIRMED — étude (2026-11-01, session 218)

A form study made in the convening after cycle 011, on the briefing's first matter (Ebola in eastern
Congo). It is not a cycle work and has no PROCESS entry. It is a first look, in the Studio's means,
at the data this session proposes for cycle 012.

**What a visitor meets.** Seventy health zones as lines across 14 May – 29 October 2026. White grains
are laboratory-confirmed cases, as each zone's cumulative count rises. Amber mist is everything else
the record wrote: suspected cases, suspected deaths, contacts traced. Playback (0.22 s a day, about
37 s) sounds the mist as filtered noise and the confirmed cases as soft tones. The mist does not
thin out; it stops. Zone-level suspicion is written on 15 days, the last on 30 May; national-only
suspicion until 4 August. From then on, for 86 days, the record writes only what a lab confirmed,
while the count rises to 10,351 in 68 zones. Jiba and Karisimbi were written with suspicion only,
never a confirmed case, so their lines go dark on 30 May.

**Material.** OCHA DRC, *République démocratique du Congo : Cas et Décès d'Ebola*, HDX, file
`drc_ebola_cases_consolidated.csv` (CC BY), fetched 2026-11-01, sha256 `761e1ed4f11d…2dbf`, not
committed. Its rows are processed by INRB-UMIE from the daily situation reports. `build.py` asserts
the checksum, the row count, the 15 days, the two last dates, 152 and 86 days of silence, 10,351, 68
zones and the two suspicion-only zones. 291 downward revisions are skipped, so the drawn zone grains
sum to 10,452 against the national 10,351; the page says so.

**Not in the build, read only.** The upstream daily zone files (INRB-UMIE, GitHub) write the same 15
days for the three suspicion measures, with some cells "ND". Their repository states no licence that
this session could read; nothing of it is committed or embedded.

**Why this form.** The fact is about when writing stops, so it is played in time; noise is the
form of what is uncertain, and its stopping is heard. No third-party code: plain canvas and Web Audio.

**Atlas neighbours** (from their entries; source pages not opened this session): *The Library of
Missing Datasets* (Mimi Ọnụọha), *Saydnaya (the missing 19dB)* (Lawrence Abu Hamdan), *WNVIRUS.COM*
([dNASAb]). Daylight on the page.

**Checked.** Chromium at 1100 and 390 px: no console errors, no sideways scroll; play, show-all and
hover work. Still: `still.png`.
