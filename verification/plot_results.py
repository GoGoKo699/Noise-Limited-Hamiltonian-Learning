#!/usr/bin/env python3
"""Plot the derived modulus and the preserved finite-count results.

This script reads the committed report. It does not run new simulations.
"""
import argparse
import hashlib
import json
import os
from pathlib import Path
import tempfile

os.environ.setdefault("MPLCONFIGDIR", str(Path(tempfile.gettempdir()) / "noise-limited-matplotlib"))

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def main():
    root = Path(__file__).resolve().parents[1]
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--data", type=Path, default=root / "verification/expected/results.json")
    parser.add_argument("--output-dir", type=Path, default=root / "science/figures")
    args = parser.parse_args()
    data_bytes = args.data.read_bytes()
    data = json.loads(data_bytes)
    finite = data["finite_shots"]
    rows = finite["results"]
    seeds = len(finite["fixed_seeds"])

    plt.rcParams.update({
        "font.family": "DejaVu Sans", "font.size": 10,
        "axes.titlesize": 11, "axes.labelsize": 10,
        "xtick.labelsize": 9, "ytick.labelsize": 9,
        "legend.fontsize": 8.8, "axes.linewidth": 0.8,
        "axes.spines.top": False, "axes.spines.right": False,
        "xtick.direction": "out", "ytick.direction": "out",
        "svg.fonttype": "path", "svg.hashsalt": "noise-limited-hamiltonian-learning",
        "savefig.facecolor": "white", "figure.facecolor": "white",
    })
    navy, teal, orange, gray = "#233F55", "#137C8B", "#C65A28", "#87939B"
    fig, (ax, bx) = plt.subplots(1, 2, figsize=(11.8, 4.35), constrained_layout=True)

    x = np.logspace(-3, 3, 601)
    ax.loglog(x, 1 / (1 + x), color=navy, lw=2.1)
    ax.loglog(x[x <= 0.3], np.ones_like(x[x <= 0.3]), color=gray, lw=1.15, ls="--")
    ax.loglog(x[x >= 3], 1 / x[x >= 3], color=gray, lw=1.15, ls="--")
    ax.axvline(1, color=gray, lw=0.8, ls=":", alpha=0.7)
    ax.scatter([1], [0.5], color=navy, s=18, zorder=4)
    ax.set_xlim(1e-3, 1e3)
    ax.set_ylim(7e-4, 1.6)
    ax.set_title("(a)  Theoretical modulus", loc="left", pad=11, fontweight="semibold")
    ax.set_xlabel(r"Coupling / leakage, $|h|/\Delta$")
    ax.set_ylabel(r"Normalized modulus, $\psi_h(\Delta)/\Delta$")
    ax.text(0.045, 0.76, "Weak interaction\n" + r"$\psi_h\sim\Delta$",
            transform=ax.transAxes, color=navy, va="top", linespacing=1.5)
    ax.text(0.52, 0.38, "Strong interaction\n" + r"$\psi_h\sim\Delta^2/|h|$",
            transform=ax.transAxes, color=navy, va="top", linespacing=1.5)
    ax.text(0.045, 0.08, r"$\frac{\psi_h(\Delta)}{\Delta}=\frac{1}{1+|h|/\Delta}$",
            transform=ax.transAxes, color=navy, fontsize=12)
    ax.grid(which="major", color="#E5EAED", lw=0.6, zorder=0)

    shots = np.array([row["total_shots_per_repetition"] for row in rows])
    rmse_true = np.array([row["rmse_to_h"] for row in rows])
    rmse_invariant = np.array([row["rmse_to_infinite_data_estimator"] for row in rows])
    bias = finite["irreducible_estimator_bias"]
    bx.loglog(shots, rmse_true, color=orange, lw=1.8, marker="o", ms=5.5,
              label=r"RMSE to true $h$")
    bx.loglog(shots, rmse_invariant, color=teal, lw=1.8, marker="s", ms=5.0,
              label=r"RMSE to $h_{\rm rec}$")
    bx.axhline(bias, color="#4B555C", lw=1.2, ls="--",
               label=r"Bias $|h-h_{\rm rec}|$")
    bx.set_xlim(shots[0] / 1.6, shots[-1] * 1.7)
    bx.set_ylim(3.4e-4, 0.11)
    bx.set_title("(b)  Finite-count reconstruction", loc="left", pad=11, fontweight="semibold")
    bx.set_xlabel("Total shots per reconstruction")
    bx.set_ylabel("RMSE (normalized frequency units)")
    bx.text(0.98, 0.96, f"{seeds} fixed seeds per budget", ha="right", va="top",
            transform=bx.transAxes, fontsize=9, color="#4B555C")
    bx.grid(which="major", color="#E5EAED", lw=0.6, zorder=0)
    bx.legend(loc="lower left", frameon=True, facecolor="white", edgecolor="#D8DEE3",
              framealpha=0.98, borderpad=0.6, labelspacing=0.6)

    args.output_dir.mkdir(parents=True, exist_ok=True)
    stem = args.output_dir / "calibration_modulus"
    description = (
        "Panel (a): the derived dimensionless function psi_h(Delta)/Delta=1/(1+|h|/Delta); "
        "dashes denote its weak/strong asymptotic forms. Panel (b): recorded RMSEs from "
        f"{seeds} fixed-seed finite-count reconstructions per budget; dashed line is the "
        "specified reciprocal estimator's infinite-data bias, not an exact minimax constant. "
        f"Source report SHA256: {hashlib.sha256(data_bytes).hexdigest()}."
    )
    fig.savefig(stem.with_suffix(".svg"), metadata={"Date": None, "Creator": "verification/plot_results.py",
                                                  "Title": "Noise-limited Hamiltonian calibration",
                                                  "Description": description})
    fig.savefig(stem.with_suffix(".png"), dpi=200,
                metadata={"Title": "Noise-limited Hamiltonian calibration", "Description": description})
    plt.close(fig)
    print(json.dumps({"figure": str(stem), "source_report_sha256": hashlib.sha256(data_bytes).hexdigest(),
                      "matplotlib": matplotlib.__version__, "new_simulations_run": False}, indent=2))


if __name__ == "__main__":
    main()
