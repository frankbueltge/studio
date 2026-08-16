#!/usr/bin/env python3
"""Conductor's feasibility probe for the concept INGRESS, session 100 (2026-08-16).

The concept proposes that a browser run a box-least-squares transit search on real
Kepler light curves, live, in front of a visitor, and that the visitor perceive the
machine performing the act that separates a planet from noise.

This script runs that same search — deliberately naive, the way a browser
implementation would have to be — on two real Kepler targets, and reports what it
finds. It is committed so the numbers in MATERIAL-100.md can be re-derived rather
than believed.

Requires: astropy, numpy. Downloads public-domain light curves from MAST.

    python3 probe.py

Every figure quoted in MATERIAL-100.md is printed by this script.
"""

import glob
import os
import time
import urllib.request

import numpy as np
from astropy.io import fits
from astropy.timeseries import BoxLeastSquares

MAST = "https://archive.stsci.edu/pub/kepler/lightcurves"

# (label, KIC id, path prefix, catalogue periods to interrogate)
TARGETS = [
    (
        "Kepler-90 (KIC 11442793) — eight confirmed planets",
        "011442793",
        "0114",
        [("b", 7.008), ("c", 8.719), ("i", 14.4485)],
    ),
    (
        "TrES-2b / Kepler-1b (KIC 11446443) — one deep hot Jupiter",
        "011446443",
        "0114",
        [("b", 2.47061)],
    ),
]


def fetch(kic, prefix, workdir):
    """Download every long-cadence quarter MAST lists for this target."""
    os.makedirs(workdir, exist_ok=True)
    listing = urllib.request.urlopen(f"{MAST}/{prefix}/{kic}/").read().decode()
    names = sorted(set(
        n for n in listing.split('"') if n.startswith("kplr") and n.endswith("_llc.fits")
    ))
    paths = []
    for n in names:
        p = os.path.join(workdir, n)
        if not os.path.exists(p):
            urllib.request.urlretrieve(f"{MAST}/{prefix}/{kic}/{n}", p)
        paths.append(p)
    return paths


def load(paths, window=101):
    """Stitch quarters, keep good cadences, flatten with a running median.

    The running median is the crude detrending a browser could afford. It is not
    what the mission pipeline does, and that difference is the point of the probe.
    """
    times, fluxes = [], []
    for path in paths:
        d = fits.open(path)[1].data
        t, f, q = d["TIME"], d["PDCSAP_FLUX"], d["SAP_QUALITY"]
        m = np.isfinite(t) & np.isfinite(f) & (q == 0)
        t, f = t[m].astype(float), f[m].astype(float)
        f = f / np.median(f)
        pad = np.pad(f, (window // 2, window // 2), mode="edge")
        trend = np.array([np.median(pad[i:i + window]) for i in range(len(f))])
        times.append(t)
        fluxes.append(f / trend)
    t = np.concatenate(times)
    f = np.concatenate(fluxes)
    order = np.argsort(t)
    return t[order], f[order]


def search(t, f, n_periods=60000, lo=0.5, hi=25.0):
    bls = BoxLeastSquares(t, f)
    periods = np.linspace(lo, hi, n_periods)
    started = time.time()
    r = bls.power(periods, np.array([0.04, 0.08, 0.15]))
    elapsed = time.time() - started
    sde = (r.power - np.median(r.power)) / np.std(r.power)
    return r, sde, elapsed, len(periods)


def main():
    workdir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "_lc")
    os.makedirs(workdir, exist_ok=True)
    for label, kic, prefix, catalogue in TARGETS:
        print(f"\n=== {label} ===")
        paths = fetch(kic, prefix, os.path.join(workdir, kic))
        t, f = load(paths)
        print(f"quarters {len(paths)}  cadences {len(t)}  "
              f"baseline {t.max() - t.min():.0f} d  scatter {np.std(f) * 1e6:.0f} ppm")
        r, sde, elapsed, n = search(t, f)
        i = int(np.argmax(sde))
        print(f"search: {n} trial periods in {elapsed:.1f}s")
        print(f"HIGHEST PEAK  P = {r.period[i]:.5f} d   SDE {sde[i]:.1f}   "
              f"depth {r.depth[i] * 1e6:.0f} ppm")
        for name, P in catalogue:
            j = int(np.argmin(abs(r.period - P)))
            print(f"  at catalogue {name} (P = {P:.4f} d): "
                  f"SDE {sde[j]:.1f}  depth {r.depth[j] * 1e6:.0f} ppm")


if __name__ == "__main__":
    main()
