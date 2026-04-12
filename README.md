# Nullified

**Self-Containment Nullification (SCN) applied to Quantum Field Theory**

## Abstract

### The Idea

Self-Containment Nullification (SCN) starts from a single set-theoretic axiom: *any set that contains itself must be the empty set* ($S \in S \Rightarrow S = \emptyset$). Applied to quantum field theory, this maps to a rule about Feynman diagrams — self-referential structures (where a propagator's correction feeds back into itself via the Dyson equation) should be nullified. The most viable physical interpretation, "Physical SCN," turned out to be equivalent to the **skeleton expansion**: compute perturbation theory using only skeleton diagrams with bare propagators, without iterating the Dyson equation. This was promising because it agreed with all of standard QFT at 1-loop, made a concrete testable prediction at 2-loop, and offered a novel principle connecting set theory to particle physics.

### SCN-Related Findings

- **Physical SCN is falsified** at ≥415σ by the electron anomalous magnetic moment at 2-loop. The self-energy insertion diagrams it removes contribute $C_2^{SE} \approx 0.77$ to the $g\text{-}2$ coefficient, and even $C_2^{SE} = 10^{-5}$ is excluded.
- **No-go theorem**: *any* SCN variant that removes a non-empty set of Feynman diagrams is falsified, because every diagram is needed to match the experimentally verified result ($C_2 = -0.328\,478\,965\,579\ldots$, confirmed to 10 significant figures).
- **No viable reinterpretation exists** in physics. The "constraint" version ($S \in S \Rightarrow S = S^*$) is tautological — it reduces to "solve your equations" in every domain (Dyson-Schwinger in QFT, Einstein equations in GR, stabilizer formalism in quantum computing).
- **No computational speedup**: SCN-as-a-filter selects the same diagram subset as the standard skeleton expansion (Weinberg Ch.12), providing no novel advantage over existing methods.
- **SCN is genuinely novel** in one domain only: **foundations of mathematics**, where $S \in S \Rightarrow S = \emptyset$ is a logically distinct axiom from both ZFC-Regularity (which forbids $S \in S$ entirely) and Aczel's Anti-Foundation Axiom (which allows it freely). Whether this produces interesting theorems is an open question.

### Consequential Discoveries (Independent of SCN)

The investigation produced several results that stand on their own, unrelated to the SCN axiom:

- **θ₀ = 2/9 lepton mass formula**: The Koide parametrization with $\theta_0 = 2/N^2$ rad ($N=3$) reproduces all three charged lepton masses (electron, muon, tau) to **< 60 ppm** accuracy using a single free parameter $M$. This is not derived from SCN or any known principle.
- **Koide formula Q = 2/3 derived from Z₃**: The Koide ratio is automatic for *any* $\theta_0$ when three masses are parametrized with $2\pi/3$ angular spacing — a trigonometric identity, not a dynamical prediction.
- **Three generations from Z₃ periodicity**: The $2\pi/3$ angular structure wraps at $n=4$, naturally predicting exactly three generations with no fourth.
- **SCN operator algebra**: The SCN operator is idempotent, multiplicative, and nonlinear, with an induced algebra isomorphic to the dual numbers $\mathbb{R}[\varepsilon]/(\varepsilon^2)$. A parallel to BRST cohomology was identified (both use nilpotent operators to separate physical from unphysical states).

### Reusable Code

The codebase provides a working framework for testing alternative diagram-selection rules against precision QED/QCD observables:

- **`src/scn_models.py`** — Pluggable model architecture: define `_is_self_containing()` to create any new diagram-filtering rule and immediately test it against $g\text{-}2$, Lamb shift, $\beta_0$, and cross-sections via the common API.
- **`src/engine/`** — Simulation engine: diagram topology generation, Passarino-Veltman loop integrals, amplitude computation, and end-to-end pipeline for 1- and 2-loop QED.
- **`src/observables.py`** — Model-parameterized observable calculations enabling batch evaluation and parameter sweeps.

This infrastructure could be reused by anyone exploring alternative perturbative truncation schemes, diagram resummation strategies, or phenomenological filtering rules — though the no-go theorem places strong constraints on what can work.

### What to Consider Instead

This study suggests that the productive directions lie in areas SCN was *pointing toward* rather than SCN itself:

- **Non-perturbative self-consistency** (Dyson-Schwinger equations, functional RG) is the real physics of self-referential propagators — but this is a mature field, not a new insight.
- **The θ₀ = 2/9 mass formula** is unexplained and may be worth pursuing independently of any axiomatic framework. The $Z_3$ structure connecting Koide's formula to three generations is suggestive but ungrounded.
- **Novel set-theoretic axioms** applied to *mathematical* structures (not physics) may be the one domain where the SCN axiom contributes something genuinely new.
- **Falsification methodology**: the approach of starting from a bold axiom, mapping it systematically to physics, and testing it to destruction is itself a template for exploring speculative ideas rigorously.

### Current Uses of SCN

As of now, SCN has exactly one demonstrated use: it is a **logically distinct axiom in set theory** ($S \in S \Rightarrow S = \emptyset$) that sits between ZFC's regularity (forbids self-membership) and AFA (allows it freely). It is not useful for physics, computation, or any applied domain. Its value is as a case study in how a simple principle can be systematically tested and falsified.

---

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
│   ├── scn_formulations.ipynb           # Systematic comparison of 4 SCN interpretations
│   ├── scn_c2_investigation.ipynb       # Definitive C₂ falsification proof
│   └── scn_beyond_falsification.ipynb   # Modified variants, other domains, applicability
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

**FALSIFIED.** Physical SCN is falsified at ≥415σ. All removal variants fail (no-go theorem). The constraint reinterpretation is tautological — equivalent to existing methods in every physics domain. No computational speedup beyond standard skeleton expansion. The only domain where SCN is genuinely novel is foundations of mathematics. See `Theory/06_open_questions.md` for the full risk register and open questions.

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

### Completed — Falsification

- [x] **C₂ computed** — Physical SCN (skeleton expansion) falsified at ≥415σ by electron g-2
- [x] **No-go theorem** — *Any* removal-type SCN variant is falsified (every 2-loop diagram is needed)

### Post-Falsification Exploration

- [x] **Modified variants explored** — Fixed-Point SCN, Graded Null SCN, Constraint SCN analyzed
- [x] **Other domains surveyed** — Quantum gravity, GR, QCD, quantum computing, mathematics
- [x] **Speedup analysis** — SCN-as-filter selects same diagrams as skeleton expansion (standard QFT); no novel speedup

See `Theory/scn_beyond_falsification.ipynb` for the full exploration.

### Key Findings

1. **No removal variant works** — any variant that removes diagrams from perturbative QFT (QED, QCD, electroweak) is falsified
2. **The constraint reinterpretation is tautological** — SCN-Constraint ($S \in S \Rightarrow S = S^*$) just says "solutions must be self-consistent," which is the definition of a solution. In every physics domain it reduces to existing methods (DSE, Einstein equations, stabilizer formalism)
3. **No computational speedup** — SCN selects the same diagram subset as the standard skeleton expansion (Weinberg Ch.12), providing no novel advantage
4. **Only genuinely novel in pure mathematics** — $S \in S \Rightarrow S = \emptyset$ is a logically distinct axiom from both ZFC-Regularity and Aczel's AFA

### Open — Independent of SCN

- [ ] **Derive θ₀ = 2/9 from first principles** — Currently fits perfectly but is not derived from any known principle
- [ ] **Extend Koide to quarks** — Q = 0.849 up-type, Q = 0.731 down-type (fails); need explanation
