"""
Graded SCN: depth-weighted perturbation theory.

Implements the attenuation operator N_λ(x) = λ^{-σ(x)} x from
Expansions/01_graded_scn_foundations.md applied to QED perturbation
theory, where σ = loop order.

The standard perturbative expansion:
    a_e = Σ_n C_n (α/π)^n

becomes under attenuation:
    a_e(λ) = Σ_n C_n (α/π)^n λ^{-n}

or equivalently, using α_eff = α / (π λ):
    a_e(λ) = Σ_n C_n α_eff^n

The threshold operator N_k zeroes all terms with loop order ≥ k:
    a_e^{(k)} = Σ_{n=0}^{k-1} C_n (α/π)^n
"""

from __future__ import annotations

from dataclasses import dataclass, field

import numpy as np


# ── Physical constants ──────────────────────────────────────

ALPHA = 1.0 / 137.035999206
ALPHA_OVER_PI = ALPHA / np.pi

# Experimental value: Hanneke, Fogwell, Gabrielse (2008); Fan et al. (2023)
A_E_EXPERIMENT = 0.00115965218059
A_E_UNCERTAINTY = 0.00000000000013


# ── QED g-2 coefficients by loop order ──────────────────────
#
# a_e = Σ_n C_n (α/π)^n
#
# Sources:
#   C_1: Schwinger (1948) — exact
#   C_2: Petermann (1957), Sommerfield (1957) — exact
#   C_3: Laporta & Remiddi (1996) — exact analytical
#   C_4: Aoyama, Kinoshita, Nio (2012, 2015) — numerical
#   C_5: Aoyama, Kinoshita, Nio (2019) — numerical
#
# These are the FULL coefficients including all diagrams at each order.

QED_G2_COEFFICIENTS: dict[int, dict] = {
    1: {
        "value": 0.5,
        "uncertainty": 0.0,
        "source": "Schwinger (1948)",
        "n_diagrams": 1,
    },
    2: {
        "value": -0.328478965579193,
        "uncertainty": 0.0,
        "source": "Petermann (1957), Sommerfield (1957)",
        "n_diagrams": 7,
    },
    3: {
        "value": 1.181241456587,
        "uncertainty": 0.000000000004,
        "source": "Laporta & Remiddi (1996)",
        "n_diagrams": 72,
    },
    4: {
        "value": -1.9113,
        "uncertainty": 0.0038,
        "source": "Aoyama, Kinoshita, Nio (2015)",
        "n_diagrams": 891,
    },
    5: {
        "value": 6.737,
        "uncertainty": 0.159,
        "source": "Aoyama, Kinoshita, Nio (2019)",
        "n_diagrams": 12672,
    },
}


# ── Skeleton (SE-removed) coefficients at 2-loop ────────────
#
# At 2-loop, 3 of 7 diagrams (I(a), I(b), I(c)) contain SE insertions.
# Binary SCN removes these. The remaining 4 skeleton diagrams give:

C2_SKELETON = -0.328478965579193 - 0.7714  # SE contribution removed
# This is the value that was falsified at ≥415σ.


@dataclass
class GradedG2Result:
    """Result of a graded SCN g-2 computation."""

    lambda_val: float
    max_loop: int
    a_e_weighted: float
    a_e_standard: float
    a_e_experiment: float = A_E_EXPERIMENT
    terms: dict[int, float] = field(default_factory=dict)

    @property
    def delta_from_experiment(self) -> float:
        return self.a_e_weighted - self.a_e_experiment

    @property
    def delta_sigma(self) -> float:
        """Deviation from experiment in units of experimental uncertainty."""
        return self.delta_from_experiment / A_E_UNCERTAINTY

    @property
    def delta_from_standard(self) -> float:
        return self.a_e_weighted - self.a_e_standard

    @property
    def relative_deviation_pct(self) -> float:
        return (self.delta_from_experiment / self.a_e_experiment) * 100


def compute_g2_standard(max_loop: int = 5) -> float:
    """Standard QED a_e to given loop order."""
    total = 0.0
    for n in range(1, max_loop + 1):
        if n in QED_G2_COEFFICIENTS:
            total += QED_G2_COEFFICIENTS[n]["value"] * ALPHA_OVER_PI**n
    return total


def compute_g2_attenuated(lambda_val: float, max_loop: int = 5) -> GradedG2Result:
    """
    Compute a_e with attenuation operator N_λ.

    Each loop order n is weighted by λ^{-n}:
        a_e(λ) = Σ_n C_n (α/π)^n λ^{-n}

    λ = 1 recovers standard QED.
    λ → ∞ kills all loop corrections (tree-level).
    """
    terms = {}
    total = 0.0
    for n in range(1, max_loop + 1):
        if n in QED_G2_COEFFICIENTS:
            coeff = QED_G2_COEFFICIENTS[n]["value"]
            weight = lambda_val ** (-n)
            term = coeff * ALPHA_OVER_PI**n * weight
            terms[n] = term
            total += term

    return GradedG2Result(
        lambda_val=lambda_val,
        max_loop=max_loop,
        a_e_weighted=total,
        a_e_standard=compute_g2_standard(max_loop),
        terms=terms,
    )


def compute_g2_threshold(k: int) -> GradedG2Result:
    """
    Compute a_e with threshold operator N_k.

    Retains only loop orders < k (kills loops ≥ k).
    k=1: tree-level only (a_e = 0)
    k=2: 1-loop (Schwinger)
    k=6: all 5 loops
    """
    terms = {}
    total = 0.0
    for n in range(1, 6):
        if n < k and n in QED_G2_COEFFICIENTS:
            coeff = QED_G2_COEFFICIENTS[n]["value"]
            term = coeff * ALPHA_OVER_PI**n
            terms[n] = term
            total += term

    return GradedG2Result(
        lambda_val=float("inf"),
        max_loop=min(k - 1, 5),
        a_e_weighted=total,
        a_e_standard=compute_g2_standard(5),
        terms=terms,
    )


def fit_lambda_to_experiment(
    max_loop: int = 5,
    lambda_range: tuple[float, float] = (0.5, 10.0),
    n_points: int = 10000,
) -> dict:
    """
    Find the λ value that minimizes |a_e(λ) - a_e_experiment|.

    Returns dict with optimal λ, residual, and diagnostic info.
    """
    lambdas = np.linspace(lambda_range[0], lambda_range[1], n_points)
    residuals = np.empty(n_points)

    for i, lam in enumerate(lambdas):
        result = compute_g2_attenuated(lam, max_loop)
        residuals[i] = abs(result.delta_from_experiment)

    best_idx = np.argmin(residuals)
    best_lambda = lambdas[best_idx]
    best_result = compute_g2_attenuated(best_lambda, max_loop)

    return {
        "lambda_optimal": best_lambda,
        "a_e_at_optimal": best_result.a_e_weighted,
        "residual": residuals[best_idx],
        "residual_sigma": best_result.delta_sigma,
        "result": best_result,
        "lambdas": lambdas,
        "residuals": residuals,
    }


def consistency_test(max_loop_values: list[int] | None = None) -> dict:
    """
    Test whether a single λ can fit across different truncation orders.

    For each max_loop in [2, 3, 4, 5], find the optimal λ.
    If graded SCN is consistent, the optimal λ should stabilize
    as max_loop increases.
    """
    if max_loop_values is None:
        max_loop_values = [2, 3, 4, 5]

    results = {}
    for ml in max_loop_values:
        fit = fit_lambda_to_experiment(max_loop=ml)
        results[ml] = {
            "lambda_optimal": fit["lambda_optimal"],
            "residual_sigma": fit["residual_sigma"],
            "a_e": fit["a_e_at_optimal"],
        }

    return results


def attenuated_series_analysis(lambda_val: float, max_loop: int = 5) -> dict:
    """
    Analyze the structure of the attenuated series at given λ.

    Returns per-term breakdown showing how attenuation changes
    the relative importance of each loop order.
    """
    standard = compute_g2_standard(max_loop)
    result = compute_g2_attenuated(lambda_val, max_loop)

    analysis = {}
    for n in range(1, max_loop + 1):
        if n not in QED_G2_COEFFICIENTS:
            continue
        coeff = QED_G2_COEFFICIENTS[n]["value"]
        std_term = coeff * ALPHA_OVER_PI**n
        att_term = result.terms.get(n, 0.0)

        analysis[n] = {
            "C_n": coeff,
            "standard_term": std_term,
            "attenuated_term": att_term,
            "attenuation_factor": lambda_val ** (-n),
            "fraction_of_standard_total": std_term / standard if standard != 0 else 0,
            "fraction_of_attenuated_total": (
                att_term / result.a_e_weighted
                if result.a_e_weighted != 0
                else 0
            ),
        }

    return {
        "lambda": lambda_val,
        "max_loop": max_loop,
        "a_e_standard": standard,
        "a_e_attenuated": result.a_e_weighted,
        "per_loop": analysis,
    }


# ═══════════════════════════════════════════════════════════════
# QCD: Depth-weighted perturbation theory
# ═══════════════════════════════════════════════════════════════
#
# Key QCD observables where the perturbative series converges
# POORLY compared to QED, making attenuation potentially useful.

ALPHA_S_MZ = 0.1179      # αs(M_Z) — PDG 2023
M_Z = 91.1876             # Z mass (GeV)
M_TAU = 1.77686           # τ mass (GeV)
N_C = 3
C_A = 3.0
T_F = 0.5

# ── QCD β-function coefficients (MS-bar) ────────────────────
#
# β(αs) = -β_0 αs²/(2π) - β_1 αs³/(4π²) - ...
# β_0 = 11 - 2n_f/3
# β_1 = 102 - 38n_f/3
#
# Under binary SCN (gluon self-energy loop nullified):
# β_0^SCN = 1 - 2n_f/3  (loses asymptotic freedom for n_f ≥ 2)
#
# Gluon SE contribution to β_0: 10/3 C_A = 10 (from gluon loop)
# Ghost contribution to β_0:    1/3 C_A = 1 (from ghost loop)
# Quark contribution to β_0:   -2n_f T_F = -n_f/3 × 2
# Total standard: (10 + 1) - 2n_f/3 = 11 - 2n_f/3

BETA0_GLUON_LOOP = 10.0   # gluon loop contribution to β_0
BETA0_GHOST_LOOP = 1.0     # ghost loop contribution to β_0
BETA0_QUARK_PER_NF = -2.0 / 3.0  # per-flavor quark contribution


def beta0_standard(nf: int) -> float:
    """Standard 1-loop β_0 = 11 - 2n_f/3."""
    return BETA0_GLUON_LOOP + BETA0_GHOST_LOOP + BETA0_QUARK_PER_NF * nf


def beta0_attenuated(nf: int, lambda_val: float) -> float:
    """
    β_0 under nesting-depth attenuation.

    The gluon self-energy loop (σ_nest = 1, self-referential: gluon
    correcting gluon with internal gluon) is weighted by λ^{-1}.
    Ghost loop and quark loops (vacuum polarisation, σ_nest = 0) keep
    full weight.

    β_0(λ) = 10/λ + 1 + (-2/3)n_f
    """
    return BETA0_GLUON_LOOP / lambda_val + BETA0_GHOST_LOOP + BETA0_QUARK_PER_NF * nf


def alpha_s_running_1loop(q2: float, nf: int, beta_0: float) -> float:
    """
    1-loop running αs(q²) with given β_0.

    With β_0 = 11 - 2n_f/3 (our convention), the exact 1-loop solution is:
    αs(q²) = αs(M_Z²) / (1 + β_0 αs(M_Z²)/(4π) ln(q²/M_Z²))
    """
    if q2 <= 0:
        return np.nan
    log_ratio = np.log(q2 / M_Z**2)
    denom = 1.0 + (beta_0 * ALPHA_S_MZ) / (4 * np.pi) * log_ratio
    if denom <= 0:
        return np.nan  # Landau pole
    return ALPHA_S_MZ / denom


# ── R-ratio perturbative coefficients ────────────────────────
#
# R(s) = R_0 (1 + Σ_{n=1} r_n (αs/π)^n)
#
# For the electromagnetic R-ratio in e+e- → hadrons:
#   r_1 = 1           (exact, 1-loop)
#   r_2 = 1.9857 - 0.1153 n_f     (Chetyrkin, Kataev, Tkachov 1979)
#   r_3 = -6.6368 - 1.2001 n_f - 0.0052 n_f² + 1.2395 (Gorishnii et al.)
#          revised: see Baikov, Chetyrkin, Kühn 2008
#   r_4 = known (Baikov, Chetyrkin, Kühn 2012)
#
# We use the n_f=3 values for the light-quark region (below charm).

def r_ratio_coefficients(nf: int) -> dict[int, float]:
    """
    Perturbative coefficients r_n for R = R_0(1 + Σ r_n (αs/π)^n).

    Sources:
        r_1: exact
        r_2: Chetyrkin, Kataev, Tkachov (1979)
        r_3: Gorishnii, Kataev, Larin (1991); Surguladze, Samuel (1991)
        r_4: Baikov, Chetyrkin, Kühn (2008, 2012)
    """
    return {
        1: 1.0,
        2: 1.9857 - 0.1153 * nf,
        3: -6.6368 - 1.2001 * nf - 0.0052 * nf**2 + 1.2395,
        4: -156.61 + 18.775 * nf - 0.7974 * nf**2 + 0.0215 * nf**3,
    }


# ── R_τ (hadronic τ decay ratio) ────────────────────────────
#
# R_τ = Γ(τ → hadrons ν_τ) / Γ(τ → e ν_e ν_τ)
#     = N_c |V_ud|² S_EW (1 + δ_pert + δ_NP)
#
# δ_pert = Σ_{n=1} K_n (αs(m_τ)/π)^n
#
# This series is POORLY convergent because αs(m_τ) ≈ 0.32 is large.

R_TAU_EXPERIMENT = 3.4771     # PDG 2023
R_TAU_UNCERTAINTY = 0.0110

V_UD_SQ = 0.97373**2         # |V_ud|²
S_EW = 1.0201                # short-distance EW correction


def r_tau_coefficients() -> dict[int, float]:
    """
    Perturbative coefficients K_n for δ_pert = Σ K_n (αs/π)^n.

    In fixed-order perturbation theory (FOPT):
        K_1 = 1
        K_2 = 5.2023    (for n_f = 3)
        K_3 = 26.366
        K_4 = 127.079   (Baikov, Chetyrkin, Kühn 2008)

    The rapid growth K_1 → K_2 → K_3 → K_4 signals poor convergence.
    """
    return {
        1: 1.0,
        2: 5.2023,
        3: 26.366,
        4: 127.079,
    }


def r_tau_tree() -> float:
    """Tree-level R_τ = N_c |V_ud|² S_EW."""
    return N_C * V_UD_SQ * S_EW


def compute_r_tau_standard(alpha_s_mtau: float, max_order: int = 4) -> dict:
    """
    Compute R_τ in fixed-order perturbation theory.

    Args:
        alpha_s_mtau: αs(m_τ²) value
        max_order: truncation order (1-4)

    Returns:
        dict with δ_pert, R_τ, per-term breakdown
    """
    coeffs = r_tau_coefficients()
    a = alpha_s_mtau / np.pi

    delta_pert = 0.0
    terms = {}
    for n in range(1, max_order + 1):
        term = coeffs[n] * a**n
        terms[n] = term
        delta_pert += term

    r_tau = r_tau_tree() * (1 + delta_pert)
    return {
        "alpha_s_mtau": alpha_s_mtau,
        "delta_pert": delta_pert,
        "r_tau": r_tau,
        "r_tau_tree": r_tau_tree(),
        "terms": terms,
        "max_order": max_order,
    }


def compute_r_tau_attenuated(
    alpha_s_mtau: float,
    lambda_val: float,
    max_order: int = 4,
) -> dict:
    """
    Compute R_τ with loop-order attenuation.

    Each perturbative order n is weighted by λ^{-n}:
        δ_pert(λ) = Σ K_n (αs/π)^n λ^{-n}

    Equivalent to evaluating at effective coupling αs_eff = αs/λ.
    """
    coeffs = r_tau_coefficients()
    a = alpha_s_mtau / np.pi

    delta_pert = 0.0
    terms = {}
    for n in range(1, max_order + 1):
        weight = lambda_val**(-n)
        term = coeffs[n] * a**n * weight
        terms[n] = term
        delta_pert += term

    r_tau = r_tau_tree() * (1 + delta_pert)
    return {
        "lambda_val": lambda_val,
        "alpha_s_mtau": alpha_s_mtau,
        "delta_pert": delta_pert,
        "r_tau": r_tau,
        "r_tau_tree": r_tau_tree(),
        "terms": terms,
        "max_order": max_order,
    }


def compute_r_tau_nesting_attenuated(
    alpha_s_mtau: float,
    lambda_val: float,
    max_order: int = 4,
) -> dict:
    """
    R_τ with nesting-depth attenuation applied to β_0.

    Instead of attenuating the perturbative coefficients K_n directly,
    we attenuate the self-referential part of the running: the gluon
    self-energy loop contribution to β_0.

    This modifies αs(m_τ²) itself by changing β_0:
        β_0(λ) = 10/λ + 1 - 2n_f/3

    Then R_τ is computed with standard K_n coefficients but
    the modified αs(m_τ²).
    """
    nf = 3  # below charm
    b0 = beta0_attenuated(nf, lambda_val)
    alpha_s_eff = alpha_s_running_1loop(M_TAU**2, nf, b0)

    if np.isnan(alpha_s_eff):
        return {
            "lambda_val": lambda_val,
            "beta0": b0,
            "alpha_s_mtau": np.nan,
            "r_tau": np.nan,
            "note": "Landau pole — β_0 too small or negative",
        }

    result = compute_r_tau_standard(alpha_s_eff, max_order)
    result["lambda_val"] = lambda_val
    result["beta0"] = b0
    result["beta0_standard"] = beta0_standard(nf)
    return result


def fit_lambda_r_tau(
    lambda_range: tuple[float, float] = (0.5, 20.0),
    n_points: int = 10000,
    max_order: int = 4,
) -> dict:
    """
    Find λ that minimizes |R_τ(λ) - R_τ^exp| using nesting-depth
    attenuation of β_0.
    """
    # Standard αs(m_τ) from running down from M_Z
    nf = 3
    alpha_s_mtau_std = alpha_s_running_1loop(M_TAU**2, nf, beta0_standard(nf))

    lambdas = np.linspace(lambda_range[0], lambda_range[1], n_points)
    residuals = np.full(n_points, np.inf)

    for i, lam in enumerate(lambdas):
        result = compute_r_tau_nesting_attenuated(alpha_s_mtau_std, lam, max_order)
        if not np.isnan(result.get("r_tau", np.nan)):
            residuals[i] = abs(result["r_tau"] - R_TAU_EXPERIMENT)

    best_idx = np.argmin(residuals)
    best_lambda = lambdas[best_idx]
    best_result = compute_r_tau_nesting_attenuated(alpha_s_mtau_std, best_lambda, max_order)

    return {
        "lambda_optimal": best_lambda,
        "r_tau_at_optimal": best_result.get("r_tau", np.nan),
        "residual": residuals[best_idx],
        "residual_sigma": residuals[best_idx] / R_TAU_UNCERTAINTY,
        "result": best_result,
        "alpha_s_mtau_standard": alpha_s_mtau_std,
        "lambdas": lambdas,
        "residuals": residuals,
    }


# ── Adler function / R-ratio at given energy ────────────────

def compute_r_ratio(
    sqrt_s: float,
    nf: int,
    lambda_val: float = 1.0,
    max_order: int = 4,
    mode: str = "nesting",
) -> dict:
    """
    Compute R(s) with attenuation.

    mode='loop': attenuate perturbative coefficients r_n by λ^{-n}
    mode='nesting': attenuate β_0 gluon loop by λ^{-1}, use standard r_n
    """
    s = sqrt_s**2
    coeffs = r_ratio_coefficients(nf)

    # Quark charges
    charges = [2/3, 1/3, 1/3, 2/3, 1/3, 2/3]
    r0 = N_C * sum(charges[i]**2 for i in range(nf))

    if mode == "nesting":
        b0 = beta0_attenuated(nf, lambda_val)
        alpha_s = alpha_s_running_1loop(s, nf, b0)
    else:
        b0 = beta0_standard(nf)
        alpha_s = alpha_s_running_1loop(s, nf, b0)

    if np.isnan(alpha_s):
        return {"sqrt_s": sqrt_s, "R": r0, "R0": r0, "alpha_s": np.nan}

    a = alpha_s / np.pi
    delta = 0.0
    terms = {}
    for n in range(1, max_order + 1):
        if mode == "loop":
            weight = lambda_val**(-n)
        else:
            weight = 1.0
        term = coeffs[n] * a**n * weight
        terms[n] = term
        delta += term

    return {
        "sqrt_s": sqrt_s,
        "R": r0 * (1 + delta),
        "R0": r0,
        "alpha_s": alpha_s,
        "beta0": b0,
        "delta": delta,
        "terms": terms,
    }
