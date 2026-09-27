#!/usr/bin/env python3
"""Draw the tutorial's disk-and-retention illustration, not a proof certificate.

Requires matplotlib. Run from any directory; --output may select SVG or PNG.
"""
from argparse import ArgumentParser
from pathlib import Path
import math

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Wedge, Rectangle


def draw(output: Path) -> None:
    plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 12,
                         "svg.fonttype": "none", "svg.hashsalt": "qic-learning-geometry"})
    fig = plt.figure(figsize=(9, 6.5), facecolor="white")
    ax = fig.add_axes([0.10, 0.16, 0.53, 0.72])
    ax.set_aspect("equal")
    ax.add_patch(Wedge((0, 0), 1, 0, 90, facecolor="#e0efe7",
                       edgecolor="#527d68", linewidth=1.8))
    ax.add_patch(Rectangle((0, 0), 1, 1, fill=False, edgecolor="#80908b",
                           linestyle=(0, (4, 4)), linewidth=1.2))
    a = 1 / math.sqrt(2)
    c = (1 + a) / 2
    ax.plot([a, 1], [a, 1], color="#3d5f9a", linewidth=2.2)
    ax.plot([0, c], [0, c], color="#a4adb3", linestyle=":", linewidth=1)
    for name, v, color, offset in [
        ("A", a, "#527d68", (-20, -4)),
        ("C", c, "#3d5f9a", (-22, 7)),
        ("B", 1, "#835d89", (8, 2)),
    ]:
        ax.scatter([v], [v], s=75, color=color, edgecolor="white", linewidth=1,
                   zorder=5, clip_on=False)
        ax.annotate(name, (v, v), xytext=offset, textcoords="offset points",
                    color=color, fontweight="bold", fontsize=14)
    ax.text(0.27, 0.38, "Classical memory", color="#365f4c", fontsize=13)
    ax.text(0.36, 0.28, r"$x^2+z^2\leq 1$", color="#365f4c", fontsize=16)
    ax.set(xlim=(0, 1.04), ylim=(0, 1.04), xlabel="X contrast  x", ylabel="Z contrast  z")
    ax.set_xticks([0, 0.5, 1]); ax.set_yticks([0, 0.5, 1])
    ax.spines[["top", "right"]].set_visible(False)
    for s in ["left", "bottom"]:
        ax.spines[s].set_color("#65716d")
    ax.tick_params(colors="#47534e")
    fig.text(0.10, 0.94, "Sharing one memory qubit between two inputs",
             fontsize=17, fontweight="bold", color="#203a30")
    fig.text(0.69, 0.75, "A  Measure the site", color="#365f4c", fontsize=13,
             fontweight="bold")
    fig.text(0.69, 0.69, r"$x=z=1/\sqrt{2}$", fontsize=15, color="#34453e")
    fig.text(0.69, 0.59, "B  Retain the site", color="#835d89", fontsize=13,
             fontweight="bold")
    fig.text(0.69, 0.53, r"$x=z=1$", fontsize=15, color="#34453e")
    fig.text(0.69, 0.43, "C  Half of each", color="#3d5f9a", fontsize=13,
             fontweight="bold")
    fig.text(0.69, 0.37, r"$x=z=(1+1/\sqrt{2})/2$", fontsize=13, color="#34453e")
    fig.text(0.69, 0.23, "One site is retained\nin every branch.\nThe retained site is random.",
             fontsize=11, linespacing=1.5, color="#47534e")
    fig.text(0.10, 0.045, "The plot shows each site's effective contrasts after averaging over the classical flag.",
             fontsize=10.5, color="#47534e")
    output.parent.mkdir(parents=True, exist_ok=True)
    metadata = {"Date": None} if output.suffix.lower() == ".svg" else {}
    fig.savefig(output, dpi=160, facecolor="white", metadata=metadata)
    plt.close(fig)
    if output.suffix.lower() == ".svg":
        output.write_text("\n".join(line.rstrip() for line in output.read_text().splitlines()) + "\n")


if __name__ == "__main__":
    parser = ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path,
                        default=Path(__file__).resolve().parents[1] / "docs/figures/retention_geometry.svg")
    draw(parser.parse_args().output)
