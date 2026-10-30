#!/usr/bin/env python3
"""Run the finite checks; never replace the committed reference implicitly."""
import argparse
import json
from pathlib import Path
import platform
import sys
import time

import numpy as np
import scipy

from checks import (check_canonical_projection, check_lower_family,
                    check_spectator_reconstruction, check_uniform_stability,
                    check_finite_shots)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, help="Write a fresh JSON report to this explicitly selected path")
    args = parser.parse_args()
    started = time.perf_counter()
    report = {
        "schema_version": 1,
        "environment": {"python": platform.python_version(), "numpy": np.__version__,
                        "scipy": scipy.__version__},
        "canonical_projection": check_canonical_projection(),
        "lower_family": check_lower_family(),
        "spectator_reconstruction": check_spectator_reconstruction(),
        "uniform_stability": check_uniform_stability(),
        "finite_shots": check_finite_shots(),
        "status": "pass",
    }
    payload = json.dumps(report, indent=2, sort_keys=True) + "\n"
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(payload)
    last = report["finite_shots"]["results"][-1]
    summary = {
        "status": report["status"],
        "elapsed_seconds": round(time.perf_counter() - started, 3),
        "canonical_projection_max_error": report["canonical_projection"]["block_average_max_error"],
        "gauge_boost_max_error": report["lower_family"]["gauge_boost_max_error"],
        "controlled_probability_max_error": report["lower_family"]["controlled_probability_max_error"],
        "finite_shot_largest_budget": last["total_shots_per_repetition"],
        "finite_shot_largest_budget_rmse_to_infinite_data_estimator": last["rmse_to_infinite_data_estimator"],
        "fresh_report": str(args.output) if args.output else None,
    }
    print(json.dumps(summary, indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(main())
