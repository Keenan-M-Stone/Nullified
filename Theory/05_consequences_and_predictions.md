# Consequences and Predictions of SCN-Filtered QFT

> **Major revision:** This document has been updated to reflect the formulation comparison framework ([scn_formulations.ipynb](scn_formulations.ipynb)), which established that **Physical SCN** is the only non-trivial viable formulation. All predictions below are stated in terms of Physical SCN unless otherwise noted.

## 1. Summary of Physical SCN's Effects

Physical SCN is equivalent to the **skeleton expansion** of perturbative QFT: compute self-energy contributions using only skeleton (2PI) diagrams with bare propagators $G_0$; do not resum via the Dyson equation.

| Feature | Standard QFT | Physical SCN (1-loop) | Physical SCN (≥ 2-loop) |
|---------|-------------|----------------------|------------------------|
| Self-energy corrections | Present, renormalized | **Identical** to standard | Nested SE insertions **nullified** |
| Vacuum polarization | Present | Present (unchanged) | Present (unchanged) |
| Vertex corrections | Present | Present (unchanged) | Skeleton vertices survive; SE-inserted vertices nullified |
| Mass renormalization | $m_{\text{bare}} \neq m_{\text{phys}}$ | $\delta m^{(1)} \neq 0$ (standard) | $\delta m$ from nested SE = 0 |
| Field renormalization $Z_2$ | $\neq 1$ | $Z_2^{(1)} \neq 1$ (standard) | Higher-order $Z_2$ reduced |
| Ward identity $Z_1 = Z_2$ | Non-trivial check | Standard ✓ | Preserved (skeleton expansion inherits from $\Gamma$) |

**Critical distinction from earlier versions of this document:** Physical SCN does NOT nullify 1-loop self-energy. The earlier claim "Nullified at all orders" was for the Diagrammatic formulation, which is **ruled out** by the Lamb shift.

---

## 2. Formulation Comparison Results

Four interpretations of self-containment were tested against experiment in [scn_formulations.ipynb](scn_formulations.ipynb):

| Formulation | Lamb shift | QCD AF | g-2 (1-loop) | Verdict |
|-------------|-----------|--------|--------------|---------|
| **Literal** | 1057 MHz ✓ | ✓ | ✓ | TRIVIAL (= standard QFT) |
| **Structural** | 40 MHz ✗ | Lost ✗ | ✓ | **RULED OUT** |
| **Diagrammatic** | 40 MHz ✗ | Lost ✗ | ✓ | **RULED OUT** |
| **Physical** | 1057 MHz ✓ | ✓ | ✓ | **★ VIABLE** |

Soft variants (momentum-dependent suppression) cannot rescue Structural/Diagrammatic: saving the Lamb shift requires $\Lambda_{\text{SCN}} \ll m_e$, making the suppression invisible at all accessible scales.

---

## 3. Concrete Predictions under Physical SCN

### 3.1 Prediction: Standard 1-Loop QED — CONFIRMED ✓

At 1-loop, Physical SCN is identical to standard QFT. All 1-loop diagrams use bare propagators and survive the self-containment filter.

| Observable | Physical SCN | Standard QED | Experiment | Status |
|-----------|-------------|-------------|------------|--------|
| $a_e$ (Schwinger) | $\alpha/(2\pi)$ | $\alpha/(2\pi)$ | $0.00115965\ldots$ | ✓ Identical |
| Lamb shift | 1057 MHz | 1057 MHz | 1057 MHz | ✓ Identical |
| Running $\alpha$ | Standard | Standard | $\alpha(M_Z) \approx 1/128$ | ✓ Identical |
| $\sigma(e^+e^- \to \mu^+\mu^-)$ | Standard | Standard | PEP/PETRA data | ✓ Identical |
| QCD $\beta_0$ | $(11C_A - 4T_F n_f)/3$ | $(11C_A - 4T_F n_f)/3$ | AF confirmed | ✓ Identical |

**Honest caveat (Risk 3):** The fact that Physical SCN agrees at 1-loop is NOT evidence for the theory. Physical SCN was defined so that 1-loop diagrams survive (because they use bare propagators). The physics argument is sound (bare vs. dressed propagators is a real distinction), but citing 1-loop agreement as validation is circular reasoning.

### 3.2 Prediction: Modified $C_2$ at Two-Loop — 🔬 TO BE COMPUTED

This is the **make-or-break test** for Physical SCN.

The electron $g-2$ expansion:

$$a_e = C_1\frac{\alpha}{\pi} + C_2\left(\frac{\alpha}{\pi}\right)^2 + C_3\left(\frac{\alpha}{\pi}\right)^3 + \cdots$$

Under Physical SCN, diagrams with nested self-energy insertions are nullified at 2-loop. The 7 two-loop QED vertex diagrams classify as:

| Diagram | Physical SCN | Reason |
|---------|-------------|--------|
| I(a): SE on external leg (before) | **NULLIFIED** | Contains 1-loop SE subdiagram (uses $G_1$) |
| I(b): SE on external leg (after) | **NULLIFIED** | Contains 1-loop SE subdiagram (uses $G_1$) |
| I(c): SE on internal line | **NULLIFIED** | Contains 1-loop SE subdiagram (uses $G_1$) |
| II: VP insertion on photon line | SURVIVES | Skeleton diagram (unique 2-loop topology) |
| III(a): Crossed-photon vertex | SURVIVES | Skeleton diagram (new topology, all $G_0$) |
| III(b): Ladder (uncrossed double) | SURVIVES | Skeleton diagram (new topology, all $G_0$) |
| III(c): Light-by-light insertion | SURVIVES | Skeleton diagram (new topology, all $G_0$) |

**Result:** $C_2^{\text{PHY}} = \sum_{\text{skeleton}} C_{2,i}$ — the sum of only skeleton diagram contributions.

**Quantitative impact:**
- $C_2^{\text{std}} = -0.328\,478\,965\,579\ldots$
- The 2-loop contribution to $a_e$: $|C_2|(\alpha/\pi)^2 \approx 1.8 \times 10^{-6}$
- Experimental precision: $\delta a_e^{\text{exp}} \approx 1.3 \times 10^{-13}$
- **Any $\mathcal{O}(0.1)$ change in $C_2$ would be detectable at $10^5\sigma$**

This means Physical SCN either:
- **(a)** Predicts $C_2^{\text{PHY}} \approx C_2^{\text{std}}$ to high precision — viable, but the SE-insertion contribution must be very small
- **(b)** Predicts $C_2^{\text{PHY}} \neq C_2^{\text{std}}$ by an $\mathcal{O}(1)$ amount — **falsified**

Computing $C_2^{\text{PHY}}$ requires looking up or computing the individual skeleton diagram contributions. This is the primary objective of the simulation engine.

### 3.3 Prediction: Unmodified Running of $\alpha$ — ✓ CONFIRMED

Since vacuum polarization survives in all formulations:

$$\alpha(q^2) = \frac{\alpha}{1 - \frac{\alpha}{3\pi}\ln\frac{q^2}{m_e^2}}$$

Identical to standard QED at all orders where VP is the dominant effect.

### 3.4 Prediction: QCD Asymptotic Freedom Preserved — ✓ CONFIRMED (under Physical SCN)

Under Physical SCN, the QCD $\beta$-function at 1-loop is standard:

$$\beta_0 = \frac{11C_A - 4T_F n_f}{3} = 11 - \frac{2n_f}{3}$$

because all 1-loop gluon self-energy diagrams use bare propagators and survive.

**Contrast with ruled-out formulations:** Structural and Diagrammatic SCN give $\beta_0 = C_A/3 - 4T_F n_f/3 = 1 - 2n_f/3$, which loses asymptotic freedom for $n_f \geq 2$. This was a major contributing factor in ruling them out.

See [scn_formulations.ipynb](scn_formulations.ipynb), §2–3 for the quantitative comparison and $\alpha_s$ running plots.

### 3.5 Prediction: No Mass Renormalization at ≥ 2-Loop (Nested) — Testable

Under Physical SCN, nested self-energy insertions at 2+ loops are nullified. This means:
- The 1-loop mass correction $\delta m^{(1)}$ is present (standard)
- The 2-loop correction from diagrams that insert $\Sigma_1$ into another SE loop is nullified
- Only skeleton 2-loop self-energy topologies contribute to $\delta m^{(2)}$

This is testable via the 2-loop Lamb shift, which receives 2-loop SE contributions.

### 3.6 Qualitative: Confinement Selection Rule

SCN provides a structural argument for confinement: self-interacting color-charged states achieve self-containment through gluon self-interaction and nullify. Only color-neutral combinations avoid this.

**Status:** Qualitative narrative only. Not a quantitative prediction. Independent of which SCN formulation is used (the argument applies at the conceptual level).

---

## 4. Hierarchy of Confidence (Updated)

| Prediction | Confidence | Agreement with experiment | Note |
|-----------|-----------|--------------------------|------|
| Tree-level QED | ★★★★★ | Perfect | Trivially unaffected |
| One-loop $a_e$ (Schwinger) | ★★★★★ | Perfect | Circular (by construction) |
| Lamb shift (Physical SCN) | ★★★★★ | Perfect | Circular at 1-loop |
| Running $\alpha$ | ★★★★★ | Consistent | VP unaffected by SCN |
| QCD $\beta_0$ (Physical SCN) | ★★★★★ | Consistent | Circular at 1-loop |
| Ward identities (1-loop) | ★★★★★ | Consistent | Trivially preserved |
| Ward identities (2-loop) | ★★★★☆ | Expected OK | Skeleton expansion argument |
| Two-loop $a_e$ ($C_2^{\text{PHY}}$) | ★★☆☆☆ | **Unknown** | The decisive test |
| 2-loop Lamb shift | ★★☆☆☆ | **Unknown** | Testable prediction |
| Unitarity (2-loop) | ★★★☆☆ | Expected OK | Skeleton argument |
| Confinement mechanism | ★☆☆☆☆ | Qualitative only | Not quantitative |
| Hierarchy problem | ☆☆☆☆☆ | Not solved | 1-loop SE survives |

**Key change from previous version:** We no longer claim ★★★★☆ for items that are trivially true by construction. The honest confidence for predictions that haven't been tested at the level where Physical SCN diverges from standard QFT is ★★☆☆☆.

---

## 5. The Fork in the Road (Updated)

### Fork 1: The Two-Loop $g-2$ — STILL OPEN, NOW PRECISELY DEFINED

If $C_2^{\text{PHY}} \neq C_2^{\text{std}}$ and experiment matches $C_2^{\text{std}}$ (which it does to sub-ppb), then Physical SCN is falsified at two-loop QED.

There is **no option (b)** here — the skeleton expansion is already the most conservative, most physically motivated formulation. There is no further refinement available without abandoning the core idea.

$C_2^{\text{PHY}}$ is the single most important number for this project.

### Fork 2: QCD Asymptotic Freedom — RESOLVED ✓

Physical SCN preserves asymptotic freedom. This fork is closed.

---

## 6. The Skeleton Expansion Interpretation

### 6.1 Precise Statement

**Physical SCN prescription:** In perturbative QFT, compute the self-energy $\Sigma$ using only **skeleton diagrams** (diagrams that cannot be decomposed by cutting a single propagator line of the same type as the external legs). Use bare propagators $G_0$ in all internal lines. Do not solve the Dyson equation $G = G_0 + G_0 \Sigma G$ self-consistently.

This is equivalent to:
- At each loop order $n$, include only diagrams where all internal propagators are bare ($G_0$)
- Exclude diagrams that can be obtained by inserting lower-order self-energy corrections into lower-order diagrams (i.e., replacing $G_0$ with $G_{n' < n}$)

### 6.2 Relationship to Standard QFT

In standard QFT, the perturbative expansion naturally includes both skeleton and non-skeleton diagrams. The Dyson resummation then organizes these into the dressed propagator. Physical SCN removes the second step (resummation) and restricts the first step (include only skeleton diagrams in the self-energy).

The skeleton expansion is a standard concept in QFT textbooks (Weinberg Ch.12, Zinn-Justin Ch.9). What is novel about Physical SCN is the **motivation**: the set-theoretic axiom $\forall S: S \in S \Rightarrow S = \emptyset$ provides a principled reason for this particular truncation of the perturbative series.

### 6.3 Gauge Invariance

The 1PI effective action $\Gamma[\phi]$ satisfies Slavnov-Taylor identities by construction. The skeleton expansion is derived from $\Gamma$ by computing self-energies as functional derivatives of $\Gamma$ with respect to bare propagators. Since $\Gamma$ is gauge-invariant, the skeleton expansion inherits this property.

**Caveat:** This argument is cleanest in the background field formalism. In the standard formalism, explicit verification at 2-loop would strengthen the case.

### 6.4 Honest Relationship to the Axiom

The SCN axiom $\forall S: S \in S \Rightarrow S = \emptyset$ does NOT logically force the skeleton expansion interpretation. The connection is:

1. The axiom identifies self-reference as the thing to eliminate
2. In QFT, the Dyson equation $G = G_0 + G_0 \Sigma G$ is the canonical self-reference
3. The skeleton expansion is the natural prescription for avoiding Dyson self-reference while preserving perturbative content

Step 3 is a **choice** motivated by the axiom, not a deduction from it. We must be transparent about this. The axiom is the inspiration; the skeleton expansion is the implementation.

---

## 7. What Physical SCN Is NOT

For intellectual honesty, we list things often conflated with SCN in this project but which are independent:

### 7.1 The Koide Formula and θ₀ = 2/9

The Koide formula ($Q = 2/3$) and the discovery that $\theta_0 = 2/9$ reproduces all three lepton masses to < 60 ppm are **phenomenological observations** about lepton masses. They work identically with or without SCN. The Z₃ nesting-depth narrative provides a suggestive connection but not a derivation.

**Status:** Interesting independent discovery. Potentially publishable on its own. Not an SCN result.

### 7.2 Z₃ Generation Structure

The prediction of exactly three generations from $\mathbb{Z}_3$ periodicity (nesting depth 4 wraps to depth 1) is a narrative connection, not a calculation. No SCN computation produces this result.

**Status:** Suggestive motivation. Not a prediction.

### 7.3 SCN Operator Algebra

The SCN operator's idempotency ($N^2 = N$), dual number isomorphism, and BRST parallel ([scn_foundations.ipynb](scn_foundations.ipynb)) describe the **algebraic structure** of the nullification operation. They do not, by themselves, predict physical quantities. They are mathematical infrastructure.

---

## 8. Experimental Targets for Simulation Engine

Priority list, updated to focus on Physical SCN's testable predictions:

| Priority | Observable | What it tests | Status |
|----------|-----------|---------------|--------|
| 1 | **$C_2^{\text{PHY}}$ (2-loop $g-2$)** | The decisive test | 🔬 Requires simulation engine |
| 2 | $e^+e^- \to \mu^+\mu^-$ at 1-loop | Baseline validation | ✅ Done ([scn_formulations.ipynb](scn_formulations.ipynb), §7) |
| 3 | 2-loop Lamb shift | Secondary test | 🔬 Requires 2-loop diagram generation |
| 4 | $R$-ratio at NLO | QCD validation | 🔬 Requires extending to QCD |
| 5 | $\alpha_s(M_Z)$ running | QCD consistency | ✅ Done at 1-loop (standard result) |
