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
│   └── 06_open_questions.md             # Discussion points
├── src/                                 # Simulation code
│   ├── particles.py                     # Particle state representations
│   ├── diagrams.py                      # Feynman diagram graph model
│   ├── scn_filter.py                    # SCN self-containment detection
│   ├── cross_sections.py               # Observable calculations
│   ├── experimental_data.py            # Measured values for comparison
│   └── run_comparison.py               # Main analysis script
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
| g-2 at 2-loop | **Different** | Testable |
| QCD asymptotic freedom | **Lost** | ⚠ Critical issue |
| Confinement | Qualitative explanation | Promising |

## Status

This is an **exploratory/theoretical** project. The framework shows promise in QED but faces serious challenges in QCD. See `Theory/06_open_questions.md` for the roadmap.
