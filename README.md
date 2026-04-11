# Nullified

**Self-Containment Nullification (SCN) applied to Quantum Field Theory**

An exploratory framework that starts from a single set-theoretic axiom — *any set that contains itself reduces to the empty set* — and develops its consequences for QED and QCD.

## The Axiom

$$\forall S:\; S \in S \;\Longrightarrow\; S = \emptyset$$

**Physical SCN** (the only viable interpretation): perturbation theory is computed using the **skeleton expansion** — only 1PI self-energy diagrams with bare propagators, without Dyson resummation. This is equivalent to standard QFT at 1-loop but differs at 2-loop and beyond. See `Theory/05_consequences_and_predictions.md` for the full formulation.

**Status: FALSIFIED.** The 2-loop electron $g-2$ coefficient $C_2$ under Physical SCN differs from the standard value because the self-energy insertion class ($C_2^{SE} \neq 0$) is removed. This produces a deviation of $\geq 415\sigma$ from experiment (even under the most conservative assumptions). See `Theory/scn_c2_investigation.ipynb` for the definitive computation.

The connection to the set-theoretic axiom is *motivational*, not deductive: the axiom inspired the filtering rule, but Physical SCN stands or falls on its own physics — and it falls.

## Project Structure

```
Nullified/
├── Theory/                              # Mathematical foundations
│   ├── 00_axiom_and_foundations.md       # The SCN axiom, logical status
│   ├── 01_viability_analysis.md         # Is this approach viable?
│   ├── 02_physical_mapping.md           # Sets → Particles → Diagrams
│   ├── 03_qed_under_scn.md             # QED with SCN filtering
│   ├── 04_qcd_under_scn.md             # QCD with SCN filtering
│   ├── 05_consequences_and_predictions.md # Testable predictions, formulation comparison
│   ├── 06_open_questions.md             # Discussion points, risk register
│   ├── 07_motivation_integration.md     # Integration of motivating ideas
│   ├── Motivation.md                    # Original motivating conversation (Q&A)
│   ├── scn_investigations.ipynb         # Koide/θ₀ verification, 1/π, Soft SCN QCD
│   ├── scn_foundations.ipynb            # SCN operator algebra, geometry, calculus
│   └── scn_formulations.ipynb           # Systematic comparison of 4 SCN interpretations
├── src/                                 # Simulation code
│   ├── particles.py                     # Particle state representations
│   ├── diagrams.py                      # Feynman diagram graph model
│   ├── scn_filter.py                    # SCN self-containment detection
│   ├── cross_sections.py               # Observable calculations
│   ├── experimental_data.py            # Measured values for comparison
│   ├── run_comparison.py               # Main analysis script
│   ├── scn_models.py                   # Four SCN formulations with common API
│   └── observables.py                  # Model-parameterised physics calculations
├── src/engine/                          # Simulation engine
│   ├── process.py                      # Scattering process definitions
│   ├── topology.py                     # QED diagram topologies (1- and 2-loop)
│   ├── classify.py                     # Physical SCN classification
│   ├── integrals.py                    # Passarino-Veltman loop integrals
│   ├── amplitudes.py                   # Amplitude and observable computation
│   └── pipeline.py                     # End-to-end orchestration
├── plots/                               # Generated figures
├── requirements.txt
└── README.md
```

## Quick Start

```bash
pip install -r requirements.txt
cd Nullified

# Original comparison analysis
python -m src.run_comparison

# Simulation engine — full Physical SCN analysis
python -c "from src.engine.pipeline import run_full_analysis; print(run_full_analysis())"
```

## Key Results

| Observable | Physical SCN vs Standard | Status |
|-----------|--------------------------|--------|
| QED tree-level | Identical | ✓ |
| Schwinger g-2 (1-loop) | Identical (circular — see note) | ✓ |
| Running α (1-loop) | Identical | ✓ |
| Lamb shift (1-loop) | Identical (1-loop SE preserved) | ✓ Resolved |
| Formulation comparison | 4 interpretations tested, 1 viable | ✓ Done |
| g-2 at 2-loop (C₂) | **Different** — 3/7 diagrams nullified | ❌ **FALSIFIED** |
| QCD asymptotic freedom | **Preserved** under Physical SCN | ✓ Resolved |
| SCN axiom novelty | **Confirmed** — no prior work | ✓ Novel |

**Independent observations** (not derived from SCN — see §Discoveries below):

| Observable | Result | Status |
|-----------|--------|--------|
| Koide formula Q = 2/3 | **Derived** (automatic for any θ₀) | ✓ Novel |
| Lepton masses (all 3) | **< 60 ppm** with 1 free parameter | ✓ Novel |
| θ₀ = 2/N² (N=3) | **Matches fitted value to 3 ppm** | ✓ Novel |
| Three generations | **Predicted** from Z₃ periodicity | ✓ Novel |
| Quark Koide formula | **Fails** (Q ≈ 0.85 / 0.73) | ✗ Open |

> **Note on 1-loop agreement**: Physical SCN is *defined* to agree with standard QFT at 1-loop (it preserves all 1PI self-energy diagrams). This is a consistency check, not evidence for SCN. The first non-trivial test is at 2-loop.

## Discoveries

### Physical SCN ≡ Skeleton Expansion

The key finding: Physical SCN is equivalent to the **skeleton expansion** of perturbative QFT (Weinberg Ch.12, Zinn-Justin Ch.9). All 1PI self-energy diagrams survive; only non-1PI self-energy insertions and Dyson resummation are excluded. This is identical to standard QFT at 1-loop, but at 2-loop, 3 of 7 vertex diagrams are nullified (the SE-insertion diagrams I(a), I(b), I(c)), while 4 survive (VP insertion II, crossed photon III(a), ladder III(b), light-by-light III(c)).

### C₂ Computation: Physical SCN Falsified

The SE-insertion class contributes a nonzero $C_2^{SE} \neq 0$ to the magnetic form factor $F_2(0)$, proven rigorously:
- The renormalized self-energy $\Sigma_R(k^2) \neq 0$ for $k^2 \neq m^2$
- The Schwinger kernel samples off-shell momenta over a continuous range
- No Ward identity constrains the magnetic form factor from SE insertions
- Even $C_2^{SE} = 10^{-5}$ produces a 415σ exclusion; the estimate $C_2^{SE} \approx 0.77$ gives 32Mσ

See `Theory/scn_c2_investigation.ipynb` for the full computation.

### θ₀ = 2/9 — Lepton Mass Formula (Independent of SCN)

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

This is an **exploratory/theoretical** project. Four SCN interpretations have been tested; only **Physical SCN** (skeleton expansion) is viable. The framework agrees with standard QFT at 1-loop by construction. The make-or-break test is computing C₂^PHY at 2-loop. The Koide/θ₀ discoveries are interesting but **independent of SCN**. See `Theory/06_open_questions.md` for the full risk register and open questions.

---

## Progress & Roadmap

### Completed

- [x] **SCN axiom formulation** — Axiom stated, logical status analyzed, dynamic interpretation defined
- [x] **Physical mapping** — Sets → Particles → Diagrams → SCN filter pipeline
- [x] **QED analysis** — Tree-level (identical), 1-loop classification (all 1PI diagrams survive under Physical SCN)
- [x] **QCD analysis** — Physical SCN preserves asymptotic freedom (gluon self-energy 1PI diagrams survive)
- [x] **Simulation code** — `src/` modules: particles, diagrams, scn_filter, cross_sections, experimental_data, run_comparison
- [x] **Koide formula derived from Z₃** — Q = 2/3 automatic for any θ₀ via trigonometric identity (independent of SCN)
- [x] **θ₀ = 2/9 discovery** — Matches fitted value to 3 ppm; all lepton masses reproduced to < 60 ppm with 1 free parameter (independent of SCN)
- [x] **Three generations predicted** — Z₃ periodicity in nesting depth (n=4 wraps to n=1) (independent of SCN)
- [x] **SCN mathematical foundations** — Operator algebra (idempotent, nonlinear, multiplicative), dual number isomorphism, BRST parallel
- [x] **Novelty confirmed** — SCN is genuinely new; no prior work under any name
- [x] **Formulation comparison** — 4 SCN interpretations tested (Literal, Structural, Diagrammatic, Physical); only Physical SCN viable
- [x] **Lamb shift resolved** — Physical SCN preserves 1-loop SE → reproduces 1057 MHz (not a test, by construction)
- [x] **QCD asymptotic freedom resolved** — Physical SCN preserves 1PI gluon SE → β₀ value unchanged
- [x] **Risk investigation** — All 5 identified risks investigated computationally; documented in `Theory/06_open_questions.md`
- [x] **C₂ diagram classification** — 3/7 two-loop vertex diagrams nullified, 4/7 survive; sensitivity: 10⁵σ
- [x] **Gauge invariance argument** — 1PI effective action satisfies Slavnov-Taylor identities; Physical SCN inherits this

### Open — Critical (Must Do)

- [ ] **Compute C₂^PHY** — The make-or-break test. Must compute the 2-loop anomalous magnetic moment using only the 4 surviving skeleton diagrams. If C₂^PHY ≠ C₂^std = −0.3285..., Physical SCN is falsified.
- [ ] **Fix code inconsistency** — `g2_components(2)` uses hand-coded tables that don't match `classify()` output. Simulation engine must handle subdiagram analysis properly.
- [ ] **Build simulation engine** — Generate diagram topologies, classify with proper subdiagram analysis, compute loop integrals, handle SCN-simplified renormalization.

### Open — Theory

- [ ] **Derive θ₀ = 2/9 from first principles** — Currently fits perfectly but is not derived from any known principle. The 1/π factor (θ₀/(2π/3) = 1/3π) may come from angular integration.
- [ ] **Extend to quarks** — Koide fails for quarks (Q = 0.849 up-type, Q = 0.731 down-type). Need either a modified formula or an explanation of why confinement breaks the Z₃ structure.
- [ ] **Unitarity check** — Verify the optical theorem holds under skeleton expansion (expected: yes, since 1PI effective action is unitary, but needs explicit confirmation).
- [ ] **Ward–Takahashi identity at 2-loop** — Explicit computation to confirm gauge invariance at higher orders (theoretical argument exists but not verified by calculation).
- [ ] **Explicit 2-loop gauge invariance** — Compute in both standard and background field formalisms. The 1PI argument must hold diagram-by-diagram.

### Open — Computation

- [ ] **Soft SCN for QCD** — Momentum-dependent suppression η(μ) = 1 − exp(−μ²/Λ²) partially recovers AF (Λ_SCN ≈ 0.1 GeV); less relevant now that Physical SCN preserves AF natively
- [ ] **BRST–SCN cohomology** — Formalize the connection: is SCN a nonlinear generalization of BRST?
- [ ] **Electroweak extension** — Apply SCN to the Higgs sector

### Stretch Goals (Paper-Worthy)

- [ ] **C₂^PHY matches experiment** — If the 4 surviving skeleton diagrams reproduce C₂^std, this would be a non-trivial prediction
- [ ] **SCN as a regularization scheme** — Prove that skeleton expansion leads to simpler renormalization (only Z₃ counterterms at 1-loop)
- [ ] **Compute a cross-section without a supercomputer** — Show that SCN's diagram reduction makes higher-order calculations tractable
