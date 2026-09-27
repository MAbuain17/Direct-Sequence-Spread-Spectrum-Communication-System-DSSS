"""Reproduce the multiuser CDMA receiver comparison and figures."""
from pathlib import Path
import csv
import sys

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))
from dsss_lab.cdma import trial


def main():
    root = Path(__file__).resolve().parents[1] / "results"
    root.mkdir(exist_ok=True)
    (root / "figures").mkdir(exist_ok=True)
    rows = []
    for family, offset in (("walsh", 0), ("walsh", 1), ("pn_shift", 0)):
        for power in (0, 6, 12, 18, 24):
            for method in ("matched", "decorrelator", "mmse"):
                rows.append(trial(users=4, family=family, chip_offset=offset,
                                  near_far_db=power, ebn0_db=8, symbols=12000,
                                  method=method, seed=20260927))
    with (root / "cdma_near_far.csv").open("w", newline="") as f:
        writer = csv.DictWriter(f, rows[0]); writer.writeheader(); writer.writerows(rows)
    fig, axes = plt.subplots(1, 3, figsize=(12, 3.7), sharey=True)
    for ax, (family, offset, title) in zip(axes, (("walsh", 0, "Walsh · aligned"),
                                                    ("walsh", 1, "Walsh · 1-chip phase"),
                                                    ("pn_shift", 0, "PN shifts · aligned"))):
        for method in ("matched", "decorrelator", "mmse"):
            subset = [r for r in rows if r["family"] == family and
                      r["chip_offset"] == offset and r["method"] == method]
            ax.plot([r["near_far_db"] for r in subset],
                    [max(r["ber"], .5/r["symbols"]) for r in subset], "o-", label=method)
        ax.set(title=title, xlabel="Interferer power / desired power (dB)",
               xticks=[0, 6, 12, 18, 24], ylim=(.5/12000, 1), yscale="log")
        ax.grid(True, which="both", alpha=.2)
    axes[0].set_ylabel("Desired-user BER")
    axes[-1].legend(loc="upper left", fontsize=8)
    fig.suptitle("Four-user DS-CDMA · 8 dB desired Eb/N0 · 12,000 bits per point")
    fig.tight_layout()
    fig.savefig(root / "figures" / "cdma_near_far.png", dpi=180)
    print(f"Wrote {len(rows)} receiver comparisons to {root}")


if __name__ == "__main__":
    main()
