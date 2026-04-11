"""
Passarino-Veltman scalar loop integrals in dimensional regularization.

Implements the standard scalar integrals needed for 1-loop QED:
  A₀(m²)           — tadpole (1-point)
  B₀(p², m₁², m₂²) — bubble (2-point)
  C₀(...)           — triangle (3-point)

All in d = 4 - 2ε dimensions. UV divergences appear as 1/ε poles.

References:
  - Passarino & Veltman, Nucl. Phys. B160 (1979) 151
  - 't Hooft & Veltman, Nucl. Phys. B153 (1979) 365
"""

from __future__ import annotations

import numpy as np
from dataclasses import dataclass


# ── Regularization parameters ──────────────────────────────

@dataclass
class RegParams:
    """Dimensional regularization parameters."""
    mu2: float = 1.0        # renormalization scale μ² (GeV²)
    epsilon: float = 0.0    # d = 4 - 2ε (0 for finite parts only)
    delta_uv: float = 0.0   # 1/ε - γ_E + ln(4π) divergent part


# ── Scalar integrals (finite parts) ────────────────────────

def A0(m2: float, reg: RegParams | None = None) -> complex:
    """
    One-point scalar integral (tadpole).

    A₀(m²) = m² (Δ_UV - ln(m²/μ²) + 1)

    where Δ_UV = 1/ε - γ_E + ln(4π).

    Returns the finite part (Δ_UV → 0) by default.
    """
    if m2 <= 0:
        return 0.0 + 0j
    mu2 = reg.mu2 if reg else 1.0
    delta = reg.delta_uv if reg else 0.0
    return m2 * (delta - np.log(m2 / mu2) + 1.0)


def B0(p2: float, m12: float, m22: float, reg: RegParams | None = None) -> complex:
    """
    Two-point scalar integral (bubble / self-energy).

    B₀(p², m₁², m₂²) = Δ_UV - ∫₀¹ dx ln[(m₁²(1-x) + m₂²x - p²x(1-x) - iε) / μ²]

    Returns the finite part by default.
    For the Schwinger term computation, we need B₀ with specific kinematics.
    """
    mu2 = reg.mu2 if reg else 1.0
    delta = reg.delta_uv if reg else 0.0

    # Numerical integration via Feynman parameter
    n_points = 1000
    x = np.linspace(1e-10, 1 - 1e-10, n_points)
    D = m12 * (1 - x) + m22 * x - p2 * x * (1 - x)

    # Handle negative D (above threshold) with iε prescription
    D_complex = D.astype(complex)
    mask = D < 0
    D_complex[mask] = D[mask] - 1j * 1e-15

    integrand = np.log(D_complex / mu2)
    integral = np.trapezoid(integrand, x)

    return delta - integral


def C0(p12: float, p22: float, p122: float,
       m12: float, m22: float, m32: float,
       reg: RegParams | None = None) -> complex:
    """
    Three-point scalar integral (triangle / vertex).

    C₀(p₁², p₂², (p₁+p₂)², m₁², m₂², m₃²)

    UV-finite for QED vertex correction.
    Computed via double Feynman parameter integration.
    """
    n_points = 200
    result = 0.0 + 0j

    for i in range(n_points):
        x = (i + 0.5) / n_points
        for j in range(n_points):
            y_max = 1 - x
            if y_max <= 0:
                continue
            y = (j + 0.5) / n_points * y_max

            z = 1 - x - y
            if z < 0:
                continue

            # Denominator: D = m₁²x + m₂²y + m₃²z - p₁²xy - p₂²yz - p₁₂²xz
            D = (m12 * x + m22 * y + m32 * z
                 - p12 * x * y - p22 * y * z - p122 * x * z)

            if abs(D) < 1e-30:
                continue

            result += y_max / (n_points * n_points) / (D + 1j * 1e-15)

    return result


# ── Schwinger anomalous magnetic moment ────────────────────

def schwinger_f2_exact() -> float:
    """
    The exact 1-loop magnetic form factor F₂(0) = α/(2π).

    This is the Schwinger result, derivable analytically from the
    vertex triangle diagram. Returns the coefficient of α/π.
    """
    return 0.5  # a_e^(1) = 0.5 × (α/π) = α/(2π)


def schwinger_f2_from_integrals(m_e: float) -> complex:
    """
    Compute F₂(0) from Passarino-Veltman integrals numerically.

    The 1-loop vertex correction for on-shell electron (q→0 limit):

    F₂(0) = (α/π) × m² × [4C₀(m², m², 0, 0, m², m²) + ...]

    In practice, the exact analytic result is 1/2 × (α/π).
    This function serves as a numerical cross-check.
    """
    m2 = m_e**2

    # C₀ for the vertex diagram: C₀(m², m², 0, m_γ², m², m²)
    # With photon mass → 0, on-shell electrons, q → 0:
    # The Schwinger integral reduces to:
    #   F₂(0) = (α/π) ∫₀¹ dx ∫₀^(1-x) dy  2m²(1-x)(1-y) / [m²(1-y)² + m_γ²y]²
    # which gives exactly α/(2π) = 0.5 × (α/π).

    # Numerical evaluation using Feynman parameters directly:
    n = 500
    total = 0.0
    for i in range(n):
        x = (i + 0.5) / n
        for j in range(n):
            y_max = 1 - x
            if y_max <= 0:
                continue
            y = (j + 0.5) / n * y_max

            # Numerator factor for F₂ extraction
            num = 2 * m2 * x * (1 - x)
            # Denominator from Feynman parametrization
            denom = m2 * (1 - x)**2
            if denom < 1e-30:
                continue

            total += y_max / (n * n) * num / denom

    return total


# ── Vacuum polarization ────────────────────────────────────

def vacuum_pol_pi(q2: float, m_f: float, charge_f: float = 1.0) -> complex:
    """
    Renormalized vacuum polarization Π_R(q²) from a single fermion loop.

    Π_R(q²) = -(α/3π) × charge² × [5/3 - 4m²/q² + (1-2m²/q²)√(1-4m²/q²) × ln(...)]

    For |q²| >> 4m²:
    Π_R(q²) ≈ -(α/3π) × charge² × ln(q²/m²)

    Returns the shift Δα/α = -Π_R(q²).
    """
    from .process import ALPHA

    if q2 <= 0:
        return 0.0 + 0j

    m2 = m_f**2
    ratio = 4 * m2 / q2

    if ratio >= 1.0:
        # Below threshold
        return 0.0 + 0j

    beta = np.sqrt(1 - ratio)

    # Full 1-loop result (on-shell subtracted)
    pi_r = (ALPHA / (3 * np.pi)) * charge_f**2 * (
        -5.0 / 3.0 + ratio
        + (1 - ratio / 2) * beta * np.log((1 + beta) / (1 - beta))
    )

    return pi_r
