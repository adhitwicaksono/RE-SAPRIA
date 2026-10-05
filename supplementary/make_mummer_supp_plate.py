#!/usr/bin/env python3

from pathlib import Path
import argparse
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.collections import LineCollection
from matplotlib.lines import Line2D
from matplotlib.ticker import FuncFormatter, MaxNLocator


# ============================================================
# EDIT FILENAMES HERE ONLY IF YOUR LOCAL NAMES ARE DIFFERENT
# ============================================================

COMPARISONS = [
    {
        "label": "Cai fixed-on-Guo",
        "strict_f": "Guo-on-Cai_fixed_mapped_1.fplot",
        "strict_r": "Guo-on-Cai_fixed_mapped_1.rplot",
        "many_f":   "Guo-on-Cai_fixed_mapped_m.fplot",
        "many_r":   "Guo-on-Cai_fixed_mapped_m.rplot",
    },
    {
        "label": "Cai published",
        "strict_f": "Guo-on-Cai_1.fplot",
        "strict_r": "Guo-on-Cai_1.rplot",
        "many_f":   "Guo-on-Cai_m.fplot",
        "many_r":   "Guo-on-Cai_m.rplot",
    },
    {
        "label": "Cai min1250",
        "strict_f": "Guo-on-Cai_minlen1250_1.fplot",
        "strict_r": "Guo-on-Cai_minlen1250_1.rplot",
        "many_f":   "Guo-on-Cai_minlen1250_m.fplot",
        "many_r":   "Guo-on-Cai_minlen1250_m.rplot",
    },
    {
        "label": "Cai Flye-HyPo",
        "strict_f": "Guo-on-Cai_HyPo_1.fplot",
        "strict_r": "Guo-on-Cai_HyPo_1.rplot",
        "many_f":   "Guo-on-Cai_HyPo_m.fplot",
        "many_r":   "Guo-on-Cai_HyPo_m.rplot",
    },
]


# ============================================================
# READ MUMMERPLOT FILES
# ============================================================

def parse_plot_file(filename):
    """
    Read MUMmer mummerplot .fplot or .rplot files.

    Returns:
        segments : numpy array, shape (N, 2, 2)
        max_x
        max_y
    """

    segments = []
    block = []

    max_x = 0.0
    max_y = 0.0

    def flush_block():
        nonlocal block

        if len(block) >= 2:

            for a, b in zip(block[:-1], block[1:]):

                # Ignore the 0,0 mummerplot sentinel
                if (
                    a[0] == 0 and a[1] == 0
                    and b[0] == 0 and b[1] == 0
                ):
                    continue

                segments.append(
                    [
                        [a[0], a[1]],
                        [b[0], b[1]]
                    ]
                )

        block = []

    with open(filename, "r", encoding="utf-8", errors="replace") as handle:

        for raw_line in handle:

            line = raw_line.strip()

            if not line:
                flush_block()
                continue

            if line.startswith("#"):
                continue

            fields = line.split()

            if len(fields) < 2:
                continue

            try:
                x = float(fields[0])
                y = float(fields[1])

            except ValueError:
                continue

            max_x = max(max_x, x)
            max_y = max(max_y, y)

            block.append((x, y))

    flush_block()

    if segments:

        segments = np.asarray(
            segments,
            dtype=np.float64
        )

    else:

        segments = np.empty(
            (0, 2, 2),
            dtype=np.float64
        )

    return segments, max_x, max_y


def load_panel(forward_file, reverse_file):

    forward, fx, fy = parse_plot_file(forward_file)
    reverse, rx, ry = parse_plot_file(reverse_file)

    return {
        "forward": forward,
        "reverse": reverse,
        "max_x": max(fx, rx),
        "max_y": max(fy, ry),
    }


# ============================================================
# FIND ALIGNMENTS UNIQUE TO MANY-TO-MANY
# ============================================================

def canonical_segment(segment):
    """
    Convert an alignment segment into a hashable tuple.

    Segment direction along the line is ignored so:
    A -> B == B -> A
    """

    a = tuple(segment[0])
    b = tuple(segment[1])

    if a <= b:
        return a + b

    return b + a


def subtract_segments(many_segments, strict_segments):
    """
    Keep only segments present in many-to-many but absent
    from the strict one-to-one set.
    """

    strict_set = {
        canonical_segment(segment)
        for segment in strict_segments
    }

    extra = [
        segment
        for segment in many_segments
        if canonical_segment(segment) not in strict_set
    ]

    if extra:

        return np.asarray(
            extra,
            dtype=np.float64
        )

    return np.empty(
        (0, 2, 2),
        dtype=np.float64
    )


def make_extra_panel(strict, many):

    return {
        "forward": subtract_segments(
            many["forward"],
            strict["forward"]
        ),

        "reverse": subtract_segments(
            many["reverse"],
            strict["reverse"]
        ),

        "max_x": max(
            strict["max_x"],
            many["max_x"]
        ),

        "max_y": max(
            strict["max_y"],
            many["max_y"]
        ),
    }


# ============================================================
# FORMATTING
# ============================================================

def format_gb(value, position):

    return f"{value / 1e9:g}"


def draw_panel(ax, panel):

    # Use Matplotlib's default colour cycle
    colours = (
        plt.rcParams["axes.prop_cycle"]
        .by_key()["color"]
    )

    forward_colour = colours[0]
    reverse_colour = colours[1]

    if len(panel["forward"]) > 0:

        collection = LineCollection(
            panel["forward"],
            linewidths=0.45,
            alpha=0.75,
            colors=forward_colour,
            rasterized=True,
        )

        ax.add_collection(collection)

    if len(panel["reverse"]) > 0:

        collection = LineCollection(
            panel["reverse"],
            linewidths=0.55,
            alpha=0.75,
            colors=reverse_colour,
            rasterized=True,
        )

        ax.add_collection(collection)

    ax.set_xlim(
        0,
        panel["max_x"] * 1.005
        if panel["max_x"] > 0 else 1
    )

    ax.set_ylim(
        0,
        panel["max_y"] * 1.005
        if panel["max_y"] > 0 else 1
    )

    ax.xaxis.set_major_locator(
        MaxNLocator(
            nbins=5,
            min_n_ticks=3
        )
    )

    ax.yaxis.set_major_locator(
        MaxNLocator(
            nbins=5,
            min_n_ticks=3
        )
    )

    ax.xaxis.set_major_formatter(
        FuncFormatter(format_gb)
    )

    ax.yaxis.set_major_formatter(
        FuncFormatter(format_gb)
    )

    ax.tick_params(
        labelsize=8
    )

    ax.grid(False)


# ============================================================
# FILE CHECK
# ============================================================

def check_files(directory):

    missing = []

    for comparison in COMPARISONS:

        for key in [
            "strict_f",
            "strict_r",
            "many_f",
            "many_r"
        ]:

            filename = (
                directory
                / comparison[key]
            )

            if not filename.exists():
                missing.append(filename)

    if missing:

        print("\nMissing files:\n")

        for filename in missing:
            print(filename)

        raise SystemExit(
            "\nEdit COMPARISONS at the top "
            "of the script if filenames differ."
        )


# ============================================================
# MAIN FIGURE
# ============================================================

def main():

    parser = argparse.ArgumentParser()

    parser.add_argument(
        "--input-dir",
        default=".",
        help=(
            "Directory containing all "
            ".fplot/.rplot files"
        ),
    )

    parser.add_argument(
        "--output",
        default=(
            "Supplementary_Fig_S1_MUMmer"
        ),
    )

    parser.add_argument(
        "--dpi",
        type=int,
        default=400,
    )

    args = parser.parse_args()

    input_dir = Path(
        args.input_dir
    ).resolve()

    check_files(input_dir)

    loaded_rows = []

    # --------------------------------------------------------
    # LOAD ALL FOUR COMPARISONS
    # --------------------------------------------------------

    for comparison in COMPARISONS:

        print(
            "\nLoading:",
            comparison["label"]
        )

        strict = load_panel(
            input_dir
            / comparison["strict_f"],

            input_dir
            / comparison["strict_r"],
        )

        many = load_panel(
            input_dir
            / comparison["many_f"],

            input_dir
            / comparison["many_r"],
        )

        extra = make_extra_panel(
            strict,
            many
        )

        # Same plotting extent for both columns
        max_x = max(
            strict["max_x"],
            many["max_x"]
        )

        max_y = max(
            strict["max_y"],
            many["max_y"]
        )

        strict["max_x"] = max_x
        strict["max_y"] = max_y

        extra["max_x"] = max_x
        extra["max_y"] = max_y

        print(
            "  Strict forward:",
            f"{len(strict['forward']):,}"
        )

        print(
            "  Strict reverse:",
            f"{len(strict['reverse']):,}"
        )

        print(
            "  Additional many-to-many forward:",
            f"{len(extra['forward']):,}"
        )

        print(
            "  Additional many-to-many reverse:",
            f"{len(extra['reverse']):,}"
        )

        print(
            "  Plot extent:",
            f"{max_x / 1e9:.3f} Gb × "
            f"{max_y / 1e9:.3f} Gb"
        )

        loaded_rows.append(
            (
                comparison,
                strict,
                extra
            )
        )

    # --------------------------------------------------------
    # CREATE 4 × 2 PLATE
    # --------------------------------------------------------

    fig, axes = plt.subplots(
        nrows=4,
        ncols=2,
        figsize=(12, 15),
    )

    panel_letters = iter(
        "ABCDEFGH"
    )

    # --------------------------------------------------------
    # DRAW PANELS
    # --------------------------------------------------------

    for row_index, (
        comparison,
        strict,
        extra
    ) in enumerate(loaded_rows):

        panels = [
            strict,
            extra
        ]

        for column_index, panel in enumerate(
            panels
        ):

            ax = axes[
                row_index,
                column_index
            ]

            draw_panel(
                ax,
                panel
            )

            letter = next(
                panel_letters
            )

            ax.text(
                0.02,
                0.98,
                letter,
                transform=ax.transAxes,
                ha="left",
                va="top",
                fontsize=13,
                fontweight="bold",
            )

            ax.set_ylabel(
                "Guo published coordinate (Gb)",
                fontsize=9,
            )

            if row_index == 3:

                ax.set_xlabel(
                    "Cai representation coordinate (Gb)",
                    fontsize=9,
                )

    # --------------------------------------------------------
    # COLUMN TITLES
    # --------------------------------------------------------

    axes[0, 0].set_title(
        "Strict one-to-one alignment",
        fontsize=12,
        pad=10,
    )

    axes[0, 1].set_title(
        "Additional many-to-many alignments",
        fontsize=12,
        pad=10,
    )

    # --------------------------------------------------------
    # ROW LABELS
    # --------------------------------------------------------

    row_positions = [
        0.835,
        0.625,
        0.415,
        0.205,
    ]

    for position, comparison in zip(
        row_positions,
        COMPARISONS
    ):

        fig.text(
            0.018,
            position,
            comparison["label"],
            rotation=90,
            va="center",
            ha="center",
            fontsize=10,
            fontweight="bold",
        )

    # --------------------------------------------------------
    # SHARED LEGEND
    # --------------------------------------------------------

    colours = (
        plt.rcParams["axes.prop_cycle"]
        .by_key()["color"]
    )

    legend_handles = [

        Line2D(
            [0],
            [0],
            color=colours[0],
            lw=1.5,
            label="Forward orientation",
        ),

        Line2D(
            [0],
            [0],
            color=colours[1],
            lw=1.5,
            label="Reverse orientation",
        ),
    ]

    fig.legend(
        handles=legend_handles,
        loc="upper center",
        ncol=2,
        frameon=False,
        bbox_to_anchor=(
            0.5,
            0.982
        ),
    )

    # --------------------------------------------------------
    # FIGURE TITLE
    # --------------------------------------------------------

    fig.suptitle(
    r"Whole-genome alignment geometry across alternative "
    r"$\it{Sapria\ himalayana}$ representations",
    fontsize=14,
    y=0.997,
    )   

    # --------------------------------------------------------
    # SPACING
    # --------------------------------------------------------

    fig.subplots_adjust(
        left=0.105,
        right=0.985,
        top=0.945,
        bottom=0.055,
        hspace=0.23,
        wspace=0.20,
    )

    # --------------------------------------------------------
    # SAVE
    # --------------------------------------------------------

    output = Path(
        args.output
    )

    png_file = output.with_suffix(
        ".png"
    )

    pdf_file = output.with_suffix(
        ".pdf"
    )

    svg_file = output.with_suffix(
        ".svg"
    )

    fig.savefig(
        png_file,
        dpi=args.dpi,
        bbox_inches="tight",
    )

    fig.savefig(
        pdf_file,
        bbox_inches="tight",
    )

    fig.savefig(
        svg_file,
        bbox_inches="tight",
    )

    plt.close(fig)

    print("\nDONE")
    print("PNG:", png_file)
    print("PDF:", pdf_file)
    print("SVG:", svg_file)


if __name__ == "__main__":
    main()
