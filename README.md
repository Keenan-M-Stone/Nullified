# Nullified

**Self-Containment Nullification (SCN) applied to Quantum Field Theory**

An exploratory framework that starts from a single set-theoretic axiom — *any set that contains itself reduces to the empty set* — and develops its consequences for QED and QCD.

## The Axiom

$$\forall S:\; S \in S \;\Longrightarrow\; S = \emptyset$$

Applied to physics: Feynman diagrams whose radiative corrections internally reference the same propagator type being corrected are **nullified** (contribute zero amplitude).

## Project Structure

```
Nullified/
├── Theory/                              # Mathematical foundations
│   ├── 00_axiom_and_foundations.md       # The SCN axiom, logical status
│   ├── 01_viability_analysis.md         # Is this approach viable?
│   ├── 02_physical_mapping.md           # Sets → Particles → Diagrams
│   ├── 03_qed_under_scn.md             # QED with SCN filtering
│   ├── 04_qcd_under_scn.md             # QCD with SCN filtering
│   ├── 05_consequences_and_predictions.md # Testable predictions
│   ├── 06_open_questions.md             # Discussion points
│   ├── 07_motivation_integration.md     # Integration of motivating ideas
│   ├── Motivation.md                    # Original motivating conversation (Q&A)
│   ├── scn_investigations.ipynb         # Koide/θ₀ verification, 1/π, Soft SCN QCD
│   └── scn_foundations.ipynb            # SCN operator algebra, geometry, calculus
├── src/                                 # Simulation code
│   ├── particles.py                     # Particle state representations
│   ├── diagrams.py                      # Feynman diagram graph model
│   ├── scn_filter.py                    # SCN self-containment detection
│   ├── cross_sections.py               # Observable calculations
│   ├── experimental_data.py            # Measured values for comparison
│   └── run_comparison.py               # Main analysis script
├── plots/                               # Generated figures
├── requirements.txt
└── README.md
```

## Quick Start

```bash
pip install -r requirements.txt
cd Nullified
python -m src.run_comparison
```

This runs the full comparison: diagram classification, g-2 analysis, cross-sections, running couplings, and generates plots in `plots/`.

## Key Results

| Observable | SCN vs Standard | Status |
|-----------|----------------|--------|
| QED tree-level | Identical | ✓ |
| Schwinger g-2 (1-loop) | Identical | ✓ |
| Running α | Identical at 1-loop | ✓ |
| Koide formula Q = 2/3 | **Derived** (automatic for any θ₀) | ✓ Novel |
| Lepton masses (all 3) | **< 60 ppm** with 1 free parameter | ✓ Novel |
| θ₀ = 2/N² (N=3) | **Matches fitted value to 3 ppm** | ✓ Novel |
| Three generations only | **Predicted** from Z₃ periodicity | ✓ Novel |
| SCN axiom novelty | **Confirmed** — no prior work under any name | ✓ Novel |
| g-2 at 2-loop | **Different** | Testable |
| QCD asymptotic freedom | **Lost** (hard SCN) / **Partially recovered** (soft SCN) | ⚠ Open |
| Confinement | Qualitative explanation | Promising |
| Quark Koide formula | **Fails** (Q ≈ 0.85 / 0.73) | ✗ Open |

## Discoveries

### θ₀ = 2/9 — Lepton Mass Formula

The Koide parametrization $\sqrt{m_n} = M(1 + \sqrt{2}\cos(\theta_0 + 2\pi n/3))$ with the choice $\theta_0 = 2/N^2$ rad (where $N = 3$ is the Z₃ rank) reproduces all three charged lepton masses with **one free parameter** $M$:

| Lepton | Predicted (MeV) | Measured (MeV) | Error |
|--------|----------------|----------------|-------|
| e | 0.51099 | 0.51100 | ~27 ppm |
| μ | 105.656 | 105.658 | ~17 ppm |
| τ | 1776.94 | 1776.86 | ~44 ppm |

See `Theory/scn_investigations.ipynb` §1–2 for the full computation.

### SCN Mathematical Foundations

The SCN operator has been characterized as idempotent, multiplicative, and nonlinear. The induced algebra is isomorphic to the dual numbers R[ε]/(ε²). A deep parallel to BRST cohomology has been identified (both use nilpotent operators to separate physical/unphysical states). See `Theory/scn_foundations.ipynb` for the full analysis.

## Status

This is an **exploratory/theoretical** project. The framework shows promise in QED but faces serious challenges in QCD. See `Theory/06_open_questions.md` for discussion.

---

## Progress & Roadmap

### Completed

- [x] **SCN axiom formulation** — Axiom stated, logical status analyzed, dynamic interpretation defined
- [x] **Physical mapping** — Sets → Particles → Diagrams → SCN filter pipeline
- [x] **QED analysis** — Tree-level (identical), 1-loop classification (self-energy nullified, VP and vertex survive)
- [x] **QCD analysis** — Gluon loop nullified, quark loop and ghost loop survive; asymptotic freedom impact assessed
- [x] **Simulation code** — `src/` modules: particles, diagrams, scn_filter, cross_sections, experimental_data, run_comparison
- [x] **Koide formula derived from Z₃** — Q = 2/3 automatic for any θ₀ via trigonometric identity
- [x] **θ₀ = 2/9 discovery** — Matches fitted value to 5 ppm; all lepton masses reproduced to < 60 ppm with 1 free parameter
- [x] **Three generations predicted** — Z₃ periodicity in nesting depth (n=4 wraps to n=1)
- [x] **SCN mathematical foundations** — Operator algebra (idempotent, nonlinear, multiplicative), dual number isomorphism, BRST parallel
- [x] **Novelty confirmed** — SCN is genuinely new; no prior work under any name (literature search: Aczel, Barwise & Moss, Forti & Honsell, Finsler, Boffa, Quine NF, Positive Set Theory)
- [x] **Soft SCN for QCD** — Momentum-dependent suppression η(μ) = 1 − exp(−μ²/Λ²) partially recovers asymptotic freedom (Λ_SCN ≈ 0.1 GeV)

### Open — Theory

- [ ] **Derive θ₀ = 2/9 from first principles** — Currently fits perfectly but is not derived from the SCN algebra. The 1/π factor (θ₀/(2π/3) = 1/3π) likely comes from angular integration but needs a rigorous argument.
- [ ] **Extend to quarks** — Koide fails for quarks (Q = 0.849 up-type, Q = 0.731 down-type). Need either a modified formula or an explanation of why confinement breaks the Z₃ structure.
- [ ] **Lamb shift under SCN** — The dominant contribution (electron self-energy) is nullified. Must compute the SCN prediction and compare to the measured 1057 MHz. This is likely the most decisive test.
- [ ] **Two-loop g−2 coefficient C₂** — Compute C₂^SCN by classifying which 2-loop diagrams survive. Compare to the measured value (experimental precision: 0.24 ppb).
- [ ] **Unitarity check** — Verify the optical theorem holds when self-energy diagrams are removed.
- [ ] **Ward–Takahashi identity at 2-loop** — Confirm gauge invariance is preserved at higher orders.
- [ ] **Formalize SCN process algebra** — Define states, transitions, and composition rules (CCS or π-calculus).

### Open — Computation

- [ ] **QCD running coupling under Soft SCN** — Implement full RGE with η(μ) suppression and compare to lattice QCD / experimental α_s(M_Z).
- [ ] **Hadron spectrum from Soft SCN** — Can the soft model reproduce meson/baryon masses?
- [ ] **BRST–SCN cohomology** — Formalize the connection: is SCN a nonlinear generalization of BRST?
- [ ] **Electroweak extension** — Apply SCN to the Higgs sector; does it naturally solve the hierarchy problem?

### Stretch Goals (Paper-Worthy)

- [ ] **Koide-like formula for quarks** — Find a Z₃ (or Z₃ × Z₃) mass formula that works for quark generations
- [ ] **SCN as a regularization scheme** — Prove that SCN-filtered QED is finite to all orders (no renormalization needed)
- [ ] **Confinement from SCN** — Derive the string tension σ ≈ 0.18 GeV² from SCN principles
- [ ] **Compute a cross-section without a supercomputer** — Show that SCN's diagram reduction makes a higher-order QFT calculation tractable by hand or on a laptop
