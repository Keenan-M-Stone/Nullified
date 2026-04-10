"""
Cross-section calculations for QED and QCD processes.

Computes tree-level and one-loop corrected cross-sections under
both standard QFT and SCN-filtered QFT, allowing direct comparison.
"""

import numpy as np

# Physical constants
ALPHA = 1.0 / 137.035999  # fine-structure constant
ALPHA_S = 0.1179          # strong coupling at M_Z
M_E = 0.000511            # electron mass (GeV)
M_MU = 0.10566            # muon mass (GeV)
M_Z = 91.1876             # Z boson mass (GeV)
GEV2_TO_NB = 0.3894e6     # conversion: GeV^-2 → nb
N_C = 3                   # number of colors
C_F = 4.0 / 3.0           # SU(3) Casimir for fundamental rep
C_A = 3.0                 # SU(3) Casimir for adjoint rep
T_F = 0.5                 # SU(3) index for fundamental rep


def sigma_ee_to_mumu_tree(s: float) -> float:
    """
    Tree-level e+e- → μ+μ- total cross-section.

    σ₀ = 4πα² / (3s)  (for s >> 4m_μ²)

    Args:
        s: Center-of-mass energy squared (GeV²)

    Returns:
        Cross-section in nanobarns
    """
    if s <= 4 * M_MU**2:
        return 0.0
    beta = np.sqrt(1 - 4 * M_MU**2 / s)
    sigma = (4 * np.pi * ALPHA**2) / (3 * s) * beta * (1 + 2 * M_MU**2 / s)
    return sigma * GEV2_TO_NB


def alpha_running_standard(q2: float, nf: int = 3) -> float:
    """
    Running fine-structure constant α(q²) at one loop (standard QFT).

    Includes vacuum polarization from all lepton and quark flavors
    with mass below √q².

    α(q²) = α / (1 - Δα(q²))
    Δα = (α/3π) Σ_f Q_f² ln(q²/m_f²)
    """
    if q2 <= 0:
        return ALPHA

    # Lepton contributions (always present if kinematically accessible)
    fermion_contributions = []
    leptons = [(M_E, 1.0), (M_MU, 1.0), (1.777, 1.0)]  # (mass, |charge|)
    quarks = [
        (0.0022, 2/3),   # up
        (0.0047, 1/3),   # down
        (0.095, 1/3),    # strange
        (1.275, 2/3),    # charm
        (4.18, 1/3),     # bottom
        (173.0, 2/3),    # top
    ]

    for mass, charge in leptons + quarks[:nf]:
        if q2 > 4 * mass**2 and mass > 0:
            nc = 1.0 if mass in [M_E, M_MU, 1.777] else N_C
            fermion_contributions.append(
                nc * charge**2 * np.log(q2 / mass**2)
            )

    delta_alpha = (ALPHA / (3 * np.pi)) * sum(fermion_contributions)
    return ALPHA / (1 - delta_alpha)


def alpha_running_scn(q2: float, nf: int = 3) -> float:
    """
    Running α(q²) under SCN filtering.

    At one loop, identical to standard QFT because vacuum polarization
    survives SCN filtering. Self-energy contributions (which are nullified)
    don't contribute to the running of α.
    """
    # At one loop, SCN gives the same result
    return alpha_running_standard(q2, nf)


def sigma_ee_to_mumu_1loop_standard(s: float) -> float:
    """
    One-loop corrected e+e- → μ+μ- cross-section (standard QFT).

    Includes:
    - Vacuum polarization (running α)
    - Vertex corrections
    - Self-energy corrections (wave function renormalization)
    """
    if s <= 4 * M_MU**2:
        return 0.0

    alpha_s = alpha_running_standard(s)
    beta = np.sqrt(1 - 4 * M_MU**2 / s)

    # Tree level with running α
    sigma_0 = (4 * np.pi * alpha_s**2) / (3 * s) * beta * (1 + 2 * M_MU**2 / s)

    # Vertex + soft-photon corrections (standard)
    # At one loop: multiplicative factor (1 + 3α/4π)
    vertex_factor = 1 + (3 * ALPHA) / (4 * np.pi)

    # Self-energy (Z₂) factor — standard QFT includes this
    z2_factor = 1 + ALPHA / (2 * np.pi)  # approximate

    sigma = sigma_0 * vertex_factor * z2_factor
    return sigma * GEV2_TO_NB


def sigma_ee_to_mumu_1loop_scn(s: float) -> float:
    """
    One-loop corrected e+e- → μ+μ- cross-section (SCN-filtered).

    Includes:
    - Vacuum polarization (running α) — SURVIVES
    - Vertex corrections — SURVIVES
    - Self-energy corrections — NULLIFIED (Z₂ = 1)
    """
    if s <= 4 * M_MU**2:
        return 0.0

    alpha_s = alpha_running_scn(s)
    beta = np.sqrt(1 - 4 * M_MU**2 / s)

    # Tree level with running α
    sigma_0 = (4 * np.pi * alpha_s**2) / (3 * s) * beta * (1 + 2 * M_MU**2 / s)

    # Vertex corrections survive
    vertex_factor = 1 + (3 * ALPHA) / (4 * np.pi)

    # Self-energy NULLIFIED: Z₂ = 1
    z2_factor = 1.0

    sigma = sigma_0 * vertex_factor * z2_factor
    return sigma * GEV2_TO_NB


def r_ratio_tree(s: float, nf: int = None) -> float:
    """
    R-ratio at tree level: R = σ(e+e- → hadrons) / σ(e+e- → μ+μ-)

    R₀ = N_c Σ_f Q_f²

    Args:
        s: center-of-mass energy squared (GeV²)
        nf: number of active quark flavors (auto-determined if None)
    """
    sqrt_s = np.sqrt(s)
    quark_info = [
        (0.0044, 2/3),   # up (threshold ~ 2*mass)
        (0.0094, 1/3),   # down
        (0.190, 1/3),    # strange
        (2.55, 2/3),     # charm
        (8.36, 1/3),     # bottom
        (346.0, 2/3),    # top
    ]

    if nf is None:
        # Auto-determine number of active flavors from √s
        active_quarks = [(m, q) for m, q in quark_info if sqrt_s > m]
    else:
        active_quarks = quark_info[:nf]

    r = N_C * sum(q**2 for _, q in active_quarks)
    return r


def r_ratio_1loop_standard(s: float, nf: int = None) -> float:
    """
    R-ratio at one loop (standard QCD corrections).

    R = R₀ (1 + αs/π + ...)
    """
    r0 = r_ratio_tree(s, nf)
    # One-loop QCD correction
    sqrt_s = np.sqrt(s)
    alpha_s_running = alpha_s_running_standard(s)
    return r0 * (1 + alpha_s_running / np.pi)


def r_ratio_1loop_scn(s: float, nf: int = None) -> float:
    """
    R-ratio at one loop (SCN-filtered QCD corrections).

    Under SCN, quark self-energy is nullified but gluon-exchange
    vertex corrections survive. The QCD correction factor is modified.
    """
    r0 = r_ratio_tree(s, nf)
    alpha_s_run = alpha_s_running_scn(s)
    # SCN modifies the correction factor
    # Quark self-energy is nullified but vertex corrections survive
    # The coefficient changes from 1.0 to approximately 0.5
    # (removing self-energy piece of the K-factor)
    scn_coefficient = 0.5
    return r0 * (1 + scn_coefficient * alpha_s_run / np.pi)


def alpha_s_running_standard(q2: float, nf: int = None) -> float:
    """
    Running strong coupling αs(q²) at one loop (standard QCD).

    αs(q²) = αs(M_Z²) / (1 + (β₀ αs(M_Z²))/(2π) ln(q²/M_Z²))
    β₀ = 11 - 2nf/3
    """
    if q2 <= 1.0:  # below ~1 GeV², perturbative QCD breaks down
        return 1.0  # non-perturbative regime

    if nf is None:
        sqrt_q = np.sqrt(q2)
        thresholds = [0.0, 0.0, 0.190, 2.55, 8.36, 346.0]
        nf = sum(1 for t in thresholds if sqrt_q > t)
        nf = min(nf, 6)

    beta0 = 11.0 - 2.0 * nf / 3.0
    log_ratio = np.log(q2 / M_Z**2)
    denominator = 1.0 + (beta0 * ALPHA_S) / (2 * np.pi) * log_ratio

    if denominator <= 0:
        return 1.0  # Landau pole region

    return ALPHA_S / denominator


def alpha_s_running_scn(q2: float, nf: int = None) -> float:
    """
    Running αs(q²) under SCN filtering.

    The gluon-loop contribution to the gluon self-energy is nullified,
    modifying β₀:

    β₀_SCN = C_A/3 - 2nf/3 = 1 - 2nf/3  (for SU(3))

    vs. standard: β₀ = 11 - 2nf/3
    """
    if q2 <= 1.0:
        return 1.0

    if nf is None:
        sqrt_q = np.sqrt(q2)
        thresholds = [0.0, 0.0, 0.190, 2.55, 8.36, 346.0]
        nf = sum(1 for t in thresholds if sqrt_q > t)
        nf = min(nf, 6)

    # SCN-modified β₀: only ghost loop (C_A/3) and quark loop (-2nf/3) survive
    beta0_scn = C_A / 3.0 - 2.0 * nf / 3.0

    log_ratio = np.log(q2 / M_Z**2)
    denominator = 1.0 + (beta0_scn * ALPHA_S) / (2 * np.pi) * log_ratio

    if denominator <= 0:
        return 1.0  # Landau pole region

    return ALPHA_S / denominator


def generate_energy_scan(sqrt_s_min: float = 1.0, sqrt_s_max: float = 200.0,
                         n_points: int = 200) -> np.ndarray:
    """Generate an array of √s values for energy scan (GeV)."""
    return np.geomspace(sqrt_s_min, sqrt_s_max, n_points)
