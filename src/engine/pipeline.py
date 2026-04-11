"""
End-to-end simulation pipeline.

Orchestrates the full computation:
  process → diagrams → classify → integrate → observables

Provides high-level functions for computing g-2, cross-sections,
and generating comparison reports between standard QFT and Physical SCN.
"""

from __future__ import annotations

import numpy as np

from .process import ALPHA, ALPHA_OVER_PI, ELECTRON
from .amplitudes import (
    compute_g2_1loop,
    compute_g2_2loop,
    compute_ee_mumu_cross_section,
    G2Result,
    CrossSectionResult,
)
from .topology import qed_vertex_diagrams
from .classify import classify_all


def compute_g2(max_loop_order: int = 2) -> dict:
    """
    Compute the anomalous magnetic moment through the specified loop order.

    Returns a dict with:
        'loop_1': G2Result for 1-loop
        'loop_2': G2Result for 2-loop (if max_loop_order >= 2)
        'a_e_total_std': cumulative a_e (standard)
        'a_e_total_scn': cumulative a_e (Physical SCN)
        'a_e_experiment': experimental value
        'summary': text summary
    """
    results = {}

    # Experimental value
    a_e_exp = 0.00115965218059

    # 1-loop
    r1 = compute_g2_1loop()
    results["loop_1"] = r1
    a_e_std = r1.a_e_standard
    a_e_scn = r1.a_e_physical_scn

    summary_lines = [
        "=" * 60,
        "Anomalous Magnetic Moment: Physical SCN vs Standard QFT",
        "=" * 60,
        "",
        f"1-loop (Schwinger):",
        f"  C₁ = {r1.coefficient_standard}",
        f"  a_e^(2) = {r1.a_e_standard:.10e}",
        f"  Diagrams: {r1.diagrams_total} total, "
        f"{r1.diagrams_surviving} survive, {r1.diagrams_nullified} nullified",
        f"  Physical SCN = Standard QFT at 1-loop: YES",
        "",
    ]

    if max_loop_order >= 2:
        r2 = compute_g2_2loop()
        results["loop_2"] = r2
        a_e_std += r2.a_e_standard
        a_e_scn += r2.a_e_physical_scn

        summary_lines += [
            f"2-loop:",
            f"  C₂^std = {r2.coefficient_standard:.12f}",
            f"  C₂^PHY = {r2.coefficient_physical_scn:.4f} (approximate)",
            f"  a_e^(4) std = {r2.a_e_standard:.10e}",
            f"  a_e^(4) PHY = {r2.a_e_physical_scn:.10e}",
            f"  Diagrams: {r2.diagrams_total} total, "
            f"{r2.diagrams_surviving} survive, {r2.diagrams_nullified} nullified",
            "",
            "  Diagram classification:",
        ]
        for d in r2.diagram_details:
            mark = "✓" if d["verdict"] == "survives" else "✗"
            skel = " [skeleton]" if d.get("is_skeleton") else ""
            summary_lines.append(
                f"    {mark} {d['name']:8s} — {d['verdict']}{skel}"
            )
        summary_lines.append("")

    results["a_e_total_std"] = a_e_std
    results["a_e_total_scn"] = a_e_scn
    results["a_e_experiment"] = a_e_exp

    delta = a_e_scn - a_e_std
    exp_uncertainty = 1.3e-13

    summary_lines += [
        "-" * 60,
        f"Cumulative (through {max_loop_order}-loop):",
        f"  a_e (standard)     = {a_e_std:.12e}",
        f"  a_e (Physical SCN) = {a_e_scn:.12e}",
        f"  a_e (experiment)   = {a_e_exp:.12e}",
        f"  Δa_e (SCN - std)   = {delta:.4e}",
        f"  Exp uncertainty    = {exp_uncertainty:.1e}",
        f"  |Δ|/σ_exp          = {abs(delta)/exp_uncertainty:.0f}σ",
        "",
        "⚠  C₂^PHY value is approximate (from literature decomposition).",
        "   The precise computation requires evaluating the 4 skeleton",
        "   diagrams independently — this is the make-or-break test.",
        "=" * 60,
    ]

    results["summary"] = "\n".join(summary_lines)
    return results


def compute_cross_section(sqrt_s_values: list[float] | None = None) -> dict:
    """
    Compute e+e- → μ+μ- cross-sections at various energies.

    Returns a dict with results at each energy and a summary.
    """
    if sqrt_s_values is None:
        sqrt_s_values = [1.0, 10.0, 91.2, 200.0, 500.0]

    results = {}

    summary_lines = [
        "=" * 70,
        "Cross-section: e+e- → μ+μ-  |  Physical SCN vs Standard QFT",
        "=" * 70,
        "",
        f"{'√s (GeV)':>10} {'σ_tree (nb)':>14} {'σ_NLO (nb)':>14} "
        f"{'K-factor':>10} {'α(s)':>12} {'Δα/α':>10}",
        "-" * 70,
    ]

    for sqrt_s in sqrt_s_values:
        r = compute_ee_mumu_cross_section(sqrt_s)
        results[sqrt_s] = r

        summary_lines.append(
            f"{sqrt_s:10.1f} {r.sigma_tree:14.6f} {r.sigma_1loop_std:14.6f} "
            f"{r.nlo_k_factor_std:10.6f} {r.alpha_running:12.8f} "
            f"{r.vp_correction:10.6f}"
        )

    summary_lines += [
        "-" * 70,
        "",
        "Note: Physical SCN = Standard QFT at 1-loop (VP + vertex corrections",
        "      both survive). Differences appear at 2-loop and beyond.",
        "=" * 70,
    ]

    results["summary"] = "\n".join(summary_lines)
    return results


def classification_report(loop_order: int = 2) -> str:
    """
    Generate a detailed classification report for all diagrams.
    """
    diagrams = qed_vertex_diagrams(loop_order)
    classifications = classify_all(diagrams)

    lines = [
        f"Physical SCN Classification Report — {loop_order}-loop QED vertex diagrams",
        "=" * 65,
        "",
    ]

    surviving = sum(1 for c in classifications if c.survives)
    nullified = len(classifications) - surviving

    lines.append(f"Total diagrams: {len(diagrams)}")
    lines.append(f"Surviving (skeleton): {surviving}")
    lines.append(f"Nullified (SE insertions): {nullified}")
    lines.append("")

    for d, c in zip(diagrams, classifications):
        mark = "✓ SURVIVES" if c.survives else "✗ NULLIFIED"
        lines.append(f"  {d.name:8s}  {mark}")
        lines.append(f"           {c.reason}")
        if d.description:
            lines.append(f"           {d.description}")
        lines.append("")

    return "\n".join(lines)


def run_full_analysis() -> str:
    """
    Run the complete simulation engine analysis and return a text report.
    """
    sections = []

    # Section 1: Classification
    sections.append(classification_report(2))

    # Section 2: g-2
    g2 = compute_g2(max_loop_order=2)
    sections.append(g2["summary"])

    # Section 3: Cross-sections
    xs = compute_cross_section()
    sections.append(xs["summary"])

    # Section 4: Experimental comparison
    g2_1 = g2["loop_1"]
    exp_a_e = 0.00115965218059
    schwinger = g2_1.a_e_standard

    sections.append("\n".join([
        "=" * 60,
        "Experimental Comparison Summary",
        "=" * 60,
        "",
        f"  Schwinger (1-loop):  {schwinger:.10e}",
        f"  Experiment:          {exp_a_e:.10e}",
        f"  Agreement at 1-loop: {abs(schwinger/exp_a_e - 1)*100:.4f}%",
        "",
        "  Physical SCN agrees with standard QFT at 1-loop by construction.",
        "  The 2-loop coefficient C₂^PHY is the decisive test.",
        "",
        f"  If C₂^PHY = C₂^std = {g2['loop_2'].coefficient_standard:.6f}:",
        "    → Physical SCN is equivalent to standard QFT (skeleton expansion",
        "      reproduces full result — non-trivial if true)",
        "",
        f"  If C₂^PHY ≠ C₂^std:",
        "    → Physical SCN is falsified (detectable at ~10⁵σ)",
        "=" * 60,
    ]))

    return "\n\n".join(sections)
