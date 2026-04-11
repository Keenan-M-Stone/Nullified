"""
Observable calculations parameterised by SCN model.

Wraps the physics from cross_sections.py but lets the caller swap in
any SCNModel so the same function computes standard QFT, hard-Literal,
soft-Diagrammatic, etc., without code duplication.
"""

from __future__ import annotations

from typing import Optional

import numpy as np

from .scn_models import SCNModel, SCNVerdict
from .diagrams import (
    make_electron_self_energy,
    make_vacuum_polarization,
    make_vertex_correction,
    make_quark_self_energy,
    make_gluon_self_energy_quark_loop,
    make_gluon_self_energy_gluon_loop,
    make_gluon_self_energy_ghost_loop,
    get_all_one_loop_qed,
    get_all_one_loop_qcd,
)

# ── Physical constants ──────────────────────────────────────

ALPHA = 1.0 / 137.035999
ALPHA_S_MZ = 0.1179
M_E = 0.000511       # GeV
M_MU = 0.10566       # GeV
M_Z = 91.1876        # GeV
GEV2_TO_NB = 0.3894e6
N_C = 3
C_A = 3.0
T_F = 0.5


# ── Diagram classification table ───────────────────────────

def diagram_classification_table(
    models: list[SCNModel],
    mu: Optional[float] = None,
) -> dict:
    """
    Classify all built-in 1-loop QED + QCD diagrams under each model.

    Returns:
        {diagram_name: {model_short_name: SCNResult, ...}, ...}
    """
    diagrams = get_all_one_loop_qed() + get_all_one_loop_qcd()
    table: dict = {}
    for d in diagrams:
        row = {}
        for m in models:
            row[m.short_name] = m.classify(d, mu)
        table[d.name] = row
    return table


# ── Running couplings ──────────────────────────────────────

def alpha_running(q2: float) -> float:
    """Running α(q²) at 1-loop.  VP always survives, so model-independent."""
    if q2 <= M_E ** 2:
        return ALPHA
    leptons = [(M_E, 1.0), (M_MU, 1.0), (1.777, 1.0)]
    quarks = [
        (0.0022, 2 / 3), (0.0047, 1 / 3), (0.095, 1 / 3),
        (1.275, 2 / 3), (4.18, 1 / 3), (173.0, 2 / 3),
    ]
    delta = 0.0
    for mass, charge in leptons + quarks:
        if q2 > 4 * mass ** 2 and mass > 0:
            nc = 1.0 if mass in (M_E, M_MU, 1.777) else N_C
            delta += nc * charge ** 2 * np.log(q2 / mass ** 2)
    delta *= ALPHA / (3 * np.pi)
    return ALPHA / (1 - delta)


def alpha_s_running(q2: float, model: SCNModel, nf: int | None = None) -> float:
    """Running αs(q²) at 1-loop using β₀ from the given SCN model."""
    if q2 <= 1.0:
        return np.nan  # non-perturbative
    if nf is None:
        sq = np.sqrt(q2)
        if sq < 1.5:
            nf = 3
        elif sq < 4.5:
            nf = 4
        elif sq < 175:
            nf = 5
        else:
            nf = 6
    beta_0 = model.beta_0_qcd(nf)
    denom = 1.0 + (beta_0 * ALPHA_S_MZ) / (2 * np.pi) * np.log(q2 / M_Z ** 2)
    if denom <= 0:
        return np.nan
    return ALPHA_S_MZ / denom


# ── e+e- → μ+μ- ────────────────────────────────────────────

def sigma_ee_mumu(s: float, model: SCNModel, mu: float | None = None) -> float:
    """
    e⁺e⁻ → μ⁺μ⁻ cross-section (nb) at 1-loop under the given model.
    """
    if s <= 4 * M_MU ** 2:
        return 0.0

    beta = np.sqrt(1 - 4 * M_MU ** 2 / s)
    alpha_q = alpha_running(s)

    # Classify the three 1-loop QED diagrams
    se_w = model.classify(make_electron_self_energy(), mu).amplitude_weight
    vc_w = model.classify(make_vertex_correction(), mu).amplitude_weight

    delta_vertex = (3 * ALPHA) / (4 * np.pi) * vc_w
    delta_se = (ALPHA / (2 * np.pi)) * se_w

    sigma = (4 * np.pi * alpha_q ** 2) / (3 * s) * beta * (1 + 2 * M_MU ** 2 / s)
    sigma *= (1 + delta_vertex + delta_se)
    return sigma * GEV2_TO_NB


# ── Electron g-2 ───────────────────────────────────────────

def g_minus_2(model: SCNModel, loop_order: int = 1) -> dict:
    """
    Compute electron anomalous magnetic moment a_e under model.

    Returns dict with component breakdown and total.
    """
    comps = model.g2_components(loop_order)
    alpha = ALPHA

    if loop_order == 1:
        # Schwinger term: α/(2π) from vertex correction
        vertex_w = comps["vertex"]["weight"]
        a_vertex = (alpha / (2 * np.pi)) * vertex_w

        # Self-energy correction to external legs (Z₂)
        se_w = comps["self_energy"]["weight"]
        # Z₂ enters as a multiplicative wave-function renormalisation;
        # at 1-loop the *net* effect on a_e is zero after on-shell
        # renormalisation in standard QED, but the self-energy diagram
        # still contributes to intermediate steps.  For a_e the
        # diagrams that matter are vertex corrections and VP insertions
        # in the photon line.
        a_vp = 0.0  # VP contributes starting at 2-loop for a_e

        a_total = a_vertex + a_vp
        return {
            "loop_order": 1,
            "a_vertex": a_vertex,
            "a_vp": a_vp,
            "a_total": a_total,
            "vertex_survives": comps["vertex"]["survives"],
            "se_survives": comps["self_energy"]["survives"],
            "note": "a_e = α/(2π) from vertex; VP starts at 2-loop",
        }

    return {"loop_order": loop_order, "components": comps}


# ── Lamb shift ─────────────────────────────────────────────

def lamb_shift(model: SCNModel, mu: float | None = None) -> dict:
    """
    Estimate Lamb shift (2S₁/₂ − 2P₁/₂ in hydrogen) under model.

    Uses standard 1-loop contributions scaled by survival weights.
    """
    comps = model.lamb_shift_components()
    result = {}
    total = 0.0
    for key, info in comps.items():
        std_mhz = info["standard_MHz"]
        w = info["weight"]
        # If soft and we have μ, re-classify for the self-energy piece
        if not info["survives"] and model.soft and mu is not None:
            w = model._soft_factor(mu)
        contrib = std_mhz * w
        total += contrib
        result[key] = {
            "standard_MHz": std_mhz,
            "weight": w,
            "scn_MHz": contrib,
            "survives": info["survives"],
        }
    result["total_standard_MHz"] = 1057.0
    result["total_scn_MHz"] = total
    result["deviation_MHz"] = total - 1057.0
    result["deviation_pct"] = (total - 1057.0) / 1057.0 * 100
    return result


# ── QCD β-function ─────────────────────────────────────────

def beta_function_table(models: list[SCNModel],
                        nf_values: list[int] | None = None) -> dict:
    """
    Compute β₀ for each model across different n_f.

    Returns: {model_short_name: {nf: {"beta_0": ..., "AF": bool}, ...}}
    """
    if nf_values is None:
        nf_values = [2, 3, 4, 5, 6]
    table = {}
    for m in models:
        row = {}
        for nf in nf_values:
            b0 = m.beta_0_qcd(nf)
            row[nf] = {"beta_0": b0, "AF": b0 > 0}
        table[m.short_name] = row
    return table


# ── R-ratio ────────────────────────────────────────────────

def r_ratio(s: float, model: SCNModel, nf: int | None = None) -> float:
    """
    R = σ(e⁺e⁻ → hadrons) / σ(e⁺e⁻ → μ⁺μ⁻) at 1-loop.
    """
    sqrt_s = np.sqrt(s)
    quark_thresholds = [
        (0.0044, 2 / 3), (0.0094, 1 / 3), (0.190, 1 / 3),
        (2.55, 2 / 3), (8.36, 1 / 3), (346.0, 2 / 3),
    ]
    if nf is None:
        active = [(m, q) for m, q in quark_thresholds if sqrt_s > m]
    else:
        active = quark_thresholds[:nf]

    r0 = N_C * sum(q ** 2 for _, q in active)
    as_val = alpha_s_running(s, model)
    if np.isnan(as_val):
        return r0
    # The 1-loop coefficient is 1 in standard, but under models that
    # nullify the quark self-energy the coefficient is reduced.
    se = model.classify(make_quark_self_energy()).amplitude_weight
    coeff = 1.0 - 0.5 * (1.0 - se)
    return r0 * (1 + coeff * as_val / np.pi)


# ── Summary report ─────────────────────────────────────────

def full_comparison(models: list[SCNModel] | None = None,
                    mu: float | None = None) -> dict:
    """
    Run all observables for all models and return a unified dict.
    """
    from .scn_models import make_all_models
    if models is None:
        models = make_all_models()

    return {
        "classification": diagram_classification_table(models, mu),
        "beta_0": beta_function_table(models),
        "g2": {m.short_name: g_minus_2(m) for m in models},
        "lamb_shift": {m.short_name: lamb_shift(m, mu) for m in models},
    }
