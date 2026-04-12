"""
Amplitude computation from diagram topologies.

Computes QED scattering amplitudes from classified diagrams,
supporting both standard QFT and Physical SCN.
"""

from __future__ import annotations

import numpy as np
from dataclasses import dataclass
from typing import Optional

from .process import ALPHA, ALPHA_OVER_PI, ELECTRON, MUON
from .topology import DiagramTopology, qed_vertex_diagrams
from .classify import classify_physical_scn, Verdict
from .integrals import (
    schwinger_f2_exact,
    vacuum_pol_pi,
)


@dataclass
class G2Result:
    """Result of g-2 computation."""
    loop_order: int
    a_e_standard: float       # standard QFT result
    a_e_physical_scn: float   # Physical SCN result
    coefficient_standard: float    # C_n in standard QFT
    coefficient_physical_scn: float  # C_n under Physical SCN
    diagrams_total: int
    diagrams_surviving: int
    diagrams_nullified: int
    diagram_details: list[dict]

    @property
    def delta_a_e(self) -> float:
        return self.a_e_physical_scn - self.a_e_standard

    @property
    def relative_deviation(self) -> float:
        if self.a_e_standard == 0:
            return 0.0
        return self.delta_a_e / self.a_e_standard


def compute_g2_1loop() -> G2Result:
    """
    Compute 1-loop anomalous magnetic moment.

    Under Physical SCN, ALL 1-loop diagrams survive (by construction).
    Result: a_e = α/(2π) = 0.5 × (α/π), identical to standard QFT.
    """
    diagrams = qed_vertex_diagrams(1)
    details = []

    for d in diagrams:
        result = classify_physical_scn(d)
        details.append({
            "name": d.name,
            "verdict": result.verdict.value,
            "reason": result.reason,
            "contribution": d.standard_contribution,
        })

    C1 = 0.5  # Schwinger coefficient
    a_e = C1 * ALPHA_OVER_PI

    return G2Result(
        loop_order=1,
        a_e_standard=a_e,
        a_e_physical_scn=a_e,    # identical at 1-loop
        coefficient_standard=C1,
        coefficient_physical_scn=C1,
        diagrams_total=len(diagrams),
        diagrams_surviving=len(diagrams),
        diagrams_nullified=0,
        diagram_details=details,
    )


def compute_g2_2loop() -> G2Result:
    """
    Classify 2-loop g-2 diagrams and compute C₂ under Physical SCN.

    Standard: C₂ = -0.328478965579...
    Physical SCN: removes SE-insertion diagrams (I(a), I(b), I(c)).

    The skeleton contribution C₂^PHY is computed as:
      C₂^PHY = C₂^std - (SE insertion contribution)

    NOTE: The SE-insertion contribution is the combined finite result
    of diagrams I(a-c) PLUS their counterterms (mass and wavefunction).
    Under Physical SCN, Z₂ = 1 and δm = 0 at 1-loop are NOT enforced
    (since 1-loop SE survives), but the SE-insertion vertex diagrams
    are removed because they use corrected (non-bare) propagators.

    The precise value of C₂^PHY requires careful treatment of the
    counterterm structure. This computation has been completed —
    Physical SCN is FALSIFIED at ≥415σ. See scn_c2_investigation.ipynb.
    """
    C2_STANDARD = -0.328478965579

    # The SE-insertion contribution (I(a) + I(b) + I(c) + counterterms)
    # is known from the literature. In the on-shell scheme:
    #
    # From Petermann (1957) and subsequent analyses:
    # - The combined SE insertions + mass/wavefunction CTs contribute
    #   a finite amount to C₂.
    #
    # IMPORTANT: This decomposition is gauge- and scheme-dependent.
    # The value below is from the Feynman gauge, on-shell scheme,
    # and serves as our best estimate. The simulation engine's
    # ultimate goal is to compute this independently.
    #
    # From Laporta's analysis: the SE-related contribution is
    # approximately +0.7714 in units of (α/π)²
    SE_CONTRIBUTION = 0.7714  # approximate, from literature

    C2_PHY = C2_STANDARD - SE_CONTRIBUTION  # ≈ -1.0999

    diagrams = qed_vertex_diagrams(2)
    surviving = 0
    nullified = 0
    details = []

    for d in diagrams:
        result = classify_physical_scn(d)
        if result.survives:
            surviving += 1
        else:
            nullified += 1
        details.append({
            "name": d.name,
            "verdict": result.verdict.value,
            "reason": result.reason,
            "is_skeleton": d.is_skeleton,
        })

    a_e_2_standard = C2_STANDARD * ALPHA_OVER_PI**2
    a_e_2_phy = C2_PHY * ALPHA_OVER_PI**2

    return G2Result(
        loop_order=2,
        a_e_standard=a_e_2_standard,
        a_e_physical_scn=a_e_2_phy,
        coefficient_standard=C2_STANDARD,
        coefficient_physical_scn=C2_PHY,
        diagrams_total=len(diagrams),
        diagrams_surviving=surviving,
        diagrams_nullified=nullified,
        diagram_details=details,
    )


@dataclass
class CrossSectionResult:
    """Result of cross-section computation."""
    process_label: str
    sqrt_s: float
    sigma_tree: float        # nanobarns
    sigma_1loop_std: float   # nanobarns
    sigma_1loop_scn: float   # nanobarns
    alpha_running: float     # α(s)
    vp_correction: float     # Δα/α from VP

    @property
    def nlo_k_factor_std(self) -> float:
        return self.sigma_1loop_std / self.sigma_tree if self.sigma_tree > 0 else 0.0

    @property
    def nlo_k_factor_scn(self) -> float:
        return self.sigma_1loop_scn / self.sigma_tree if self.sigma_tree > 0 else 0.0


def compute_ee_mumu_cross_section(sqrt_s: float) -> CrossSectionResult:
    """
    Compute e+e- → μ+μ- cross-section at tree and 1-loop level.

    At 1-loop, Physical SCN and standard QFT give identical results
    (both preserve VP and vertex corrections). The only difference
    is in the treatment of external-leg corrections (LSZ factors),
    which cancel in the cross-section ratio.
    """
    GEV2_TO_NB = 0.3894e6
    s = sqrt_s**2
    m_mu = MUON.mass

    if s <= 4 * m_mu**2:
        return CrossSectionResult(
            process_label=f"e+e- → μ+μ- at √s={sqrt_s:.1f} GeV",
            sqrt_s=sqrt_s, sigma_tree=0, sigma_1loop_std=0,
            sigma_1loop_scn=0, alpha_running=ALPHA, vp_correction=0,
        )

    beta = np.sqrt(1 - 4 * m_mu**2 / s)

    # Tree-level
    sigma_tree = (4 * np.pi * ALPHA**2) / (3 * s) * beta * GEV2_TO_NB

    # 1-loop: VP correction gives running α
    # Sum over all fermion flavors below √s
    delta_alpha = 0.0
    fermions = [
        (ELECTRON.mass, 1.0),   # electron
        (MUON.mass, 1.0),       # muon
        (1.777, 1.0),           # tau
        (0.0022, 2/3),          # up
        (0.0047, 1/3),          # down
        (0.095, 1/3),           # strange
        (1.275, 2/3),           # charm
        (4.18, 1/3),            # bottom
    ]
    for m_f, q_f in fermions:
        if sqrt_s > 2 * m_f and m_f > 0:
            nc = 3.0 if q_f != 1.0 else 1.0
            vp = vacuum_pol_pi(s, m_f, q_f)
            delta_alpha += nc * float(vp.real) if isinstance(vp, complex) else nc * float(vp)

    alpha_s = ALPHA / (1 - delta_alpha)
    sigma_1loop = (4 * np.pi * alpha_s**2) / (3 * s) * beta * GEV2_TO_NB

    # Under Physical SCN at 1-loop: identical (VP survives, vertex correction
    # contributes to forward-backward asymmetry but not total cross-section)
    sigma_1loop_scn = sigma_1loop

    return CrossSectionResult(
        process_label=f"e+e- → μ+μ- at √s={sqrt_s:.1f} GeV",
        sqrt_s=sqrt_s,
        sigma_tree=sigma_tree,
        sigma_1loop_std=sigma_1loop,
        sigma_1loop_scn=sigma_1loop_scn,
        alpha_running=alpha_s,
        vp_correction=delta_alpha,
    )
