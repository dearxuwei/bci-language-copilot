from __future__ import annotations

from pathlib import Path
import sys

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import FancyArrowPatch, FancyBboxPatch

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from bci_language_copilot.language.phrase_bank import PhraseBankPredictor
from bci_language_copilot.metrics.input_efficiency import compute_efficiency

plt.rcParams["font.family"] = "sans-serif"
plt.rcParams["font.sans-serif"] = ["Arial", "DejaVu Sans", "Liberation Sans"]
plt.rcParams["svg.fonttype"] = "none"
plt.rcParams["font.size"] = 8
plt.rcParams["axes.linewidth"] = 0.8

COLORS = {
    "ink": "#1F2933",
    "muted": "#667085",
    "line": "#D5DAE1",
    "bg": "#F7F9FC",
    "blue": "#2F6DB2",
    "cyan": "#35A6B8",
    "violet": "#7C6CCF",
    "amber": "#D98B2B",
    "green": "#3C8C5A",
    "red": "#B84A4A",
}


def clean(ax):
    ax.set_xticks([])
    ax.set_yticks([])
    for spine in ax.spines.values():
        spine.set_visible(False)


def panel_label(ax, label):
    ax.text(
        -0.03,
        1.04,
        label,
        transform=ax.transAxes,
        fontsize=11,
        fontweight="bold",
        ha="left",
        va="bottom",
        color=COLORS["ink"],
    )


def box(ax, xy, wh, title, body, fc="#FFFFFF", ec=None, title_color=None):
    x, y = xy
    w, h = wh
    patch = FancyBboxPatch(
        (x, y),
        w,
        h,
        boxstyle="round,pad=0.012,rounding_size=0.018",
        fc=fc,
        ec=ec or COLORS["line"],
        lw=1.0,
    )
    ax.add_patch(patch)
    ax.text(
        x + 0.025,
        y + h - 0.055,
        title,
        fontsize=9,
        fontweight="bold",
        color=title_color or COLORS["ink"],
        ha="left",
        va="top",
    )
    ax.text(
        x + 0.025,
        y + h - 0.125,
        body,
        fontsize=7.2,
        color=COLORS["muted"],
        ha="left",
        va="top",
        linespacing=1.25,
    )
    return patch


def arrow(ax, start, end, color=COLORS["muted"], rad=0.0):
    ax.add_patch(
        FancyArrowPatch(
            start,
            end,
            arrowstyle="-|>",
            mutation_scale=10,
            lw=1.1,
            color=color,
            connectionstyle=f"arc3,rad={rad}",
        )
    )


def draw_pipeline(ax):
    clean(ax)
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.text(
        0.01,
        0.95,
        "BCI-Language Copilot: method route from sparse neural evidence to phrase-level communication",
        fontsize=15,
        fontweight="bold",
        color=COLORS["ink"],
        ha="left",
        va="top",
    )
    ax.text(
        0.01,
        0.855,
        "Figure 1 style schematic. The current repository implements the mock decoder, constrained phrase bank, and input-efficiency metric; hardware classifiers and LLM providers are extension points.",
        fontsize=8.5,
        color=COLORS["muted"],
        ha="left",
        va="top",
    )
    stages = [
        ("1 EEG epoch", "P300 / SSVEP\ncandidate evidence", COLORS["cyan"]),
        ("2 Decoder", "posterior over\nintent tokens", COLORS["blue"]),
        ("3 Stop rule", "confidence threshold\nand trial budget", COLORS["violet"]),
        ("4 Language layer", "context phrase bank\nor local LLM", COLORS["amber"]),
        ("5 Output", "ranked phrases\n+ efficiency report", COLORS["green"]),
    ]
    xs = np.linspace(0.02, 0.79, len(stages))
    for idx, (title, body, color) in enumerate(stages):
        box(ax, (xs[idx], 0.29), (0.15, 0.34), title, body, fc="#FFFFFF", ec=color, title_color=color)
        if idx < len(stages) - 1:
            arrow(ax, (xs[idx] + 0.15, 0.46), (xs[idx + 1] - 0.01, 0.46), color=color)
    box(
        ax,
        (0.825, 0.035),
        (0.15, 0.19),
        "Safety boundary",
        "assistive research;\nnot emergency use",
        fc="#FFF8EF",
        ec=COLORS["amber"],
        title_color=COLORS["amber"],
    )
    arrow(ax, (0.865, 0.29), (0.865, 0.225), color=COLORS["amber"])
    ax.text(
        0.02,
        0.13,
        "Design references: P300 speller literature, ChatBCI / ChatBCI-Assist, dynamic language-model BCI typing, and Nature/IEEE graphical-abstract conventions.",
        fontsize=7.5,
        color=COLORS["muted"],
        ha="left",
    )


def draw_signal(ax):
    panel_label(ax, "a")
    ax.set_title("Simulated event-related EEG evidence", loc="left", fontsize=10, fontweight="bold")
    t = np.linspace(-0.2, 0.8, 400)
    rng = np.random.default_rng(3)
    for i in range(7):
        baseline = 0.1 * rng.normal(size=t.size) + 0.22 * np.sin(2 * np.pi * (4 + i * 0.2) * t)
        offset = i * 1.05
        ax.plot(t, baseline + offset, color="#B8C1CC", lw=0.8)
    p300 = 0.22 * rng.normal(size=t.size) + 1.25 * np.exp(-((t - 0.31) ** 2) / 0.012)
    ax.plot(t, p300 + 7.35, color=COLORS["cyan"], lw=2.2)
    ax.axvspan(0.24, 0.42, color=COLORS["cyan"], alpha=0.12)
    ax.text(0.29, 8.75, "P300 window", color=COLORS["cyan"], fontsize=8)
    ax.set_xlabel("time from stimulus (s)")
    ax.set_ylabel("channels")
    ax.set_yticks([])
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)


def draw_decoder(ax):
    panel_label(ax, "b")
    ax.set_title("Decoder posterior and adaptive stopping", loc="left", fontsize=10, fontweight="bold")
    labels = ["water", "pain", "rest"]
    probs = np.array([0.72, 0.18, 0.10])
    bars = ax.barh(labels, probs, color=[COLORS["blue"], "#AAB7C4", "#C8CED6"], height=0.58)
    ax.axvline(0.70, color=COLORS["red"], lw=1.2, ls="--")
    ax.text(0.705, 2.45, "stop threshold", color=COLORS["red"], fontsize=7, ha="left")
    for b, p in zip(bars, probs):
        ax.text(p + 0.02, b.get_y() + b.get_height() / 2, f"{p:.2f}", va="center", fontsize=8)
    ax.set_xlim(0, 1)
    ax.set_xlabel("posterior probability")
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)


def draw_language(ax):
    panel_label(ax, "c")
    ax.set_title("Constrained phrase ranking", loc="left", fontsize=10, fontweight="bold")
    predictor = PhraseBankPredictor()
    suggestions = predictor.suggest("water", context="clinical", top_k=3)
    y = np.arange(3)
    scores = [s.score for s in suggestions]
    ax.barh(y, scores, color=[COLORS["amber"], "#E6BE83", "#EAD5B6"], height=0.55)
    ax.set_yticks(y)
    ax.set_yticklabels([s.text for s in suggestions], fontsize=7)
    ax.invert_yaxis()
    ax.set_xlim(0, 1.1)
    ax.set_xlabel("rank score")
    for yy, s in zip(y, suggestions):
        ax.text(1.03, yy, s.source, fontsize=7, va="center", ha="right", color=COLORS["muted"])
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)


def draw_efficiency(ax):
    panel_label(ax, "d")
    ax.set_title("Output and input-efficiency accounting", loc="left", fontsize=10, fontweight="bold")
    metric = compute_efficiency("water", "I need some water.")
    clean(ax)
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    box(
        ax,
        (0.05, 0.58),
        (0.9, 0.27),
        "Selected phrase",
        "\"I need some water.\"\ninput: water -> completed phrase",
        fc="#FFFFFF",
        ec=COLORS["green"],
        title_color=COLORS["green"],
    )
    values = [
        ("selected chars", metric.selected_characters, COLORS["blue"]),
        ("completed chars", metric.completed_characters, COLORS["amber"]),
        ("saved chars", metric.characters_saved, COLORS["green"]),
    ]
    for idx, (label, value, color) in enumerate(values):
        x = 0.07 + idx * 0.30
        ax.text(x, 0.38, str(value), fontsize=22, fontweight="bold", color=color, ha="left")
        ax.text(x, 0.27, label, fontsize=7.2, color=COLORS["muted"], ha="left")
    ax.text(
        0.07,
        0.11,
        f"repository demo metric: {metric.keystroke_saving_rate:.1%} keystroke saving",
        fontsize=8,
        color=COLORS["ink"],
        ha="left",
    )


def draw_method_matrix(ax):
    panel_label(ax, "e")
    ax.set_title("Implemented modules vs. planned extensions", loc="left", fontsize=10, fontweight="bold")
    clean(ax)
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    rows = [
        ("implemented", "MockBCIDecoder", "PhraseBankPredictor", "InputEfficiency"),
        ("extension", "P300 / SSVEP classifier", "local LLM provider", "online latency + top-k"),
        ("guardrail", "offline prototype", "constrained phrases", "not emergency use"),
    ]
    cols = ["status", "decoder", "language", "evaluation"]
    x0 = [0.03, 0.24, 0.50, 0.75]
    widths = [0.18, 0.23, 0.22, 0.21]
    for x, w, col in zip(x0, widths, cols):
        ax.text(x, 0.86, col, fontsize=7.5, fontweight="bold", color=COLORS["ink"], ha="left")
        ax.plot([x, x + w], [0.82, 0.82], color=COLORS["line"], lw=1)
    for r, row in enumerate(rows):
        y = 0.68 - r * 0.22
        color = [COLORS["green"], COLORS["blue"], COLORS["amber"]][r]
        for x, w, text in zip(x0, widths, row):
            ax.add_patch(FancyBboxPatch((x, y), w, 0.14, boxstyle="round,pad=0.007,rounding_size=0.012", fc="#FFFFFF", ec=COLORS["line"], lw=0.7))
            ax.text(x + 0.01, y + 0.07, text, fontsize=7.0, color=color if x == x0[0] else COLORS["muted"], va="center", ha="left")


def main():
    out = Path(__file__).with_name("cover-bci-language-copilot-v5.svg")
    fig = plt.figure(figsize=(16, 9), facecolor="white", constrained_layout=False)
    gs = fig.add_gridspec(
        nrows=3,
        ncols=4,
        height_ratios=[1.05, 1.25, 1.1],
        width_ratios=[1.15, 1.0, 1.15, 1.2],
        left=0.045,
        right=0.985,
        top=0.94,
        bottom=0.08,
        wspace=0.36,
        hspace=0.62,
    )
    draw_pipeline(fig.add_subplot(gs[0, :]))
    draw_signal(fig.add_subplot(gs[1, 0]))
    draw_decoder(fig.add_subplot(gs[1, 1]))
    draw_language(fig.add_subplot(gs[1, 2:]))
    draw_efficiency(fig.add_subplot(gs[2, 0:2]))
    draw_method_matrix(fig.add_subplot(gs[2, 2:]))
    fig.text(
        0.047,
        0.025,
        "Original methods figure. Literature anchors: P300 speller, dynamic NLP-assisted BCI spelling, ChatBCI, ChatBCI-Assist. Research prototype only.",
        fontsize=7.5,
        color=COLORS["muted"],
    )
    fig.savefig(out, format="svg")
    print(out)


if __name__ == "__main__":
    main()
