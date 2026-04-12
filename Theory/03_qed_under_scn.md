# QED Under SCN: Detailed Analysis

> **⚠️ Formulation Update (important):** The analysis below was originally written under the "Diagrammatic SCN" interpretation, which nullifies ALL self-energy diagrams. Systematic testing (`scn_formulations.ipynb`) showed that Diagrammatic SCN is **ruled out** — it predicts a Lamb shift of ~40 MHz vs the measured 1057 MHz. The only viable interpretation is **Physical SCN** (skeleton expansion), which preserves all 1PI self-energy diagrams at 1-loop. See §7 below for the corrected classification. Sections 2–6 are retained for historical context but the conclusions in §3.1 are superseded.
>
> **❌ Falsification (definitive):** Physical SCN has itself been **falsified at ≥415σ** by the 2-loop electron $g-2$ coefficient $C_2$. The skeleton expansion omits SE-insertion diagrams that contribute $C_2^{SE} \approx 0.77$ — even $C_2^{SE} = 10^{-5}$ is excluded at 415σ. A no-go theorem establishes that *any* SCN variant removing a non-empty set of Feynman diagrams is falsified. See `scn_c2_investigation.ipynb` for the full computation and `scn_beyond_falsification.ipynb` for post-falsification analysis. The analysis below is retained for intellectual completeness.

## 1. QED Review

Quantum Electrodynamics describes the interaction of charged fermions (electrons, muons, etc.) with photons via the Lagrangian:

$$\mathcal{L}_{\text{QED}} = \bar{\psi}(i\gamma^\mu D_\mu - m)\psi - \frac{1}{4}F_{\mu\nu}F^{\mu\nu}$$

where $D_\mu = \partial_\mu + ieA_\mu$ is the covariant derivative.

The Feynman rules give three building blocks:
- **Fermion propagator:** $\frac{i(\not{p} + m)}{p^2 - m^2 + i\epsilon}$
- **Photon propagator:** $\frac{-ig_{\mu\nu}}{k^2 + i\epsilon}$ (Feynman gauge)
- **QED vertex:** $-ie\gamma^\mu$

---

## 2. Tree-Level Processes (Unaffected by SCN)

Tree-level diagrams have no loops and therefore no possibility of self-containment. All tree-level QED predictions are **identical** under SCN and standard QED.

Key tree-level results that survive unchanged:
- $e^+e^- \to \mu^+\mu^-$ cross-section
- $e^+e^- \to e^+e^-$ (Bhabha scattering)
- Compton scattering $e\gamma \to e\gamma$
- Pair annihilation $e^+e^- \to \gamma\gamma$

---

## 3. One-Loop Analysis

### 3.1 Electron Self-Energy — NULLIFIED

The one-loop electron self-energy:

```
    e ——→——●——→—— e
              |  ↑
              γ  |
              ↓  |
         e ——→——●
```

The diagram corrects the electron propagator. Internally, between the two QED vertices, an electron propagator appears. This is self-containment: the electron propagator correction *uses* the electron propagator.

**Under SCN:** This diagram is nullified. $\Sigma^{(1)}(p) = 0$.

**Physical consequences:**
- No one-loop mass renormalization: $\delta m^{(1)} = 0$
- No one-loop field-strength renormalization: $Z_2^{(1)} = 1$
- The pole mass equals the bare mass at one-loop order

### 3.2 Vacuum Polarization — SURVIVES

The one-loop vacuum polarization:

```
    γ ~~~~●——→——●~~~~ γ  
              ↑  |
              |  ↓
              ←——
           (e⁺e⁻ loop)
```

The diagram corrects the photon propagator. Internally, the loop consists of electron and positron propagators — no photon propagator appears inside.

**Under SCN:** This diagram **survives**. $\Pi^{(1)}(q^2) \neq 0$.

**Physical consequences:**
- The photon propagator receives radiative corrections
- The fine-structure constant runs: $\alpha(q^2)$ increases at higher energies
- The Uehling potential (QED correction to Coulomb potential) is present
- Contributes to the Lamb shift

### 3.3 Vertex Correction — SURVIVES

The one-loop vertex correction (Schwinger term):

```
         γ
         |
    e ——→——●——→—— e
         |       |
         γ(virtual)
         |       |
    e ——→——●——→—— e
```

More precisely, the triangle diagram adds a virtual photon connecting the two fermion lines of the tree-level vertex. The correction is to the QED vertex, and internally it contains:
- Two fermion propagators
- One photon propagator
- Two QED vertices

Does this contain a QED vertex correction internally? No — the internal structure is a photon exchange, not a nested vertex correction. The two internal QED vertices are *tree-level* vertices, not corrected vertices.

**Under SCN:** This diagram **survives**. $\Lambda^{(1)\mu} \neq 0$.

**Physical consequences (verified in [scn_investigations.ipynb](scn_investigations.ipynb), §1):**
- The anomalous magnetic moment receives its one-loop contribution:

$$a_e^{(1)} = \frac{\alpha}{2\pi} \approx 0.0011614$$

- This matches the Schwinger result, which agrees with experiment to high precision

### 3.4 Summary at One Loop

| Diagram | SCN Status | Standard QFT contribution | SCN contribution |
|---------|-----------|--------------------------|------------------|
| Electron self-energy $\Sigma$ | Nullified | Divergent → renormalized | $0$ |
| Vacuum polarization $\Pi$ | Survives | Divergent → renormalized | Must evaluate (see §4) |
| Vertex correction $\Lambda$ | Survives | $\alpha/(2\pi)$ (finite) | $\alpha/(2\pi)$ |

---

## 4. The Vacuum Polarization Integral Under SCN

The vacuum polarization tensor at one loop:

$$\Pi^{\mu\nu}(q) = -e^2 \int \frac{d^4k}{(2\pi)^4} \text{Tr}\left[\gamma^\mu \frac{\not{k}+m}{k^2-m^2}\gamma^\nu \frac{\not{k}-\not{q}+m}{(k-q)^2-m^2}\right]$$

This integral is **logarithmically divergent** in standard QFT ($D = 0$ superficial degree of divergence).

### 4.1 The SCN Perspective on This Divergence

SCN does NOT modify the integral — it only eliminates entire diagrams. Since vacuum polarization passes the SCN filter, we must evaluate it as-is.

**Option A: Accept the divergence and renormalize normally.** SCN acts alongside standard renormalization, reducing the number of counterterms needed.

**Option B: Argue that SCN implies a physical interpretation of the divergence.** Since self-energy corrections (which would normally absorb the vacuum polarization divergence via Ward identities) are nullified, the vacuum polarization must be independently finite or we have a problem.

### 4.2 The Ward Identity Issue

The Ward–Takahashi identity relates vertex and self-energy corrections:

$$q_\mu \Lambda^\mu(p, p+q) = \Sigma(p) - \Sigma(p+q)$$

With $\Sigma^{(1)} = 0$ (nullified) and $\Lambda^{(1)} \neq 0$ (survives):

$$q_\mu \Lambda^{(1)\mu} = 0 - 0 = 0$$

Is $q_\mu \Lambda^{(1)\mu} = 0$ actually true? Yes! The vertex correction satisfies $q_\mu \Lambda^{(1)\mu} = 0$ **on its own** because the vertex correction, evaluated between on-shell spinors, satisfies the Ward identity independently. The magnetic form factor (which gives $g-2$) is transverse and satisfies this.

More precisely, the full vertex can be decomposed:

$$\Lambda^\mu = F_1(q^2)\gamma^\mu + \frac{i\sigma^{\mu\nu}q_\nu}{2m}F_2(q^2)$$

The Ward identity constrains $F_1$: $F_1(0) = 1$ (with proper normalization accounting for $Z_1 = Z_2$). With $Z_2 = 1$ (no electron self-energy), the Ward identity requires $F_1^{(1)}(0) = 0$, which is indeed the case at one loop: the one-loop $F_1$ at $q^2 = 0$ is related to $Z_2 - 1 = 0$.

**The Ward identity is preserved at one loop under SCN.** ✓

This is a non-trivial consistency check. The Ward identity $Z_1 = Z_2$ becomes $1 = 1$ under SCN, trivially satisfied.

---

## 5. Higher-Order Analysis

### 5.1 Two-Loop Diagrams

At two loops, new self-containment scenarios arise:

**Nested self-energy:** An electron self-energy with another self-energy inserted on the internal electron line. Both the outer and inner self-energies are self-containing → nullified. ✓

**Overlapping corrections:** A two-loop diagram where one loop is a self-energy and another is a vertex correction. The self-energy sub-loop causes the whole diagram to be self-containing → nullified. ✓

**Double vacuum polarization:** Two vacuum polarization insertions in the photon line. Neither is self-containing → both survive. ✓

**Vacuum polarization with self-energy insertion:** A VP loop where the internal electron line has a self-energy insertion. The self-energy sub-diagram is self-containing → the whole diagram is nullified. ✓

### 5.2 Pattern at Higher Orders

The SCN filter creates a systematic pattern:
- **Survives:** Any diagram that can be factored into VP loops and vertex corrections without self-energy subdiagrams
- **Nullified:** Any diagram containing a self-energy insertion anywhere in its structure

This dramatically reduces the number of contributing diagrams at each order.

---

## 6. SCN-QED Predictions vs. Standard QED

### 6.1 Anomalous Magnetic Moment

Standard QED: $a_e = \frac{\alpha}{2\pi} - 0.32848\left(\frac{\alpha}{\pi}\right)^2 + 1.181\left(\frac{\alpha}{\pi}\right)^3 - \cdots$

Under SCN, terms involving self-energy subdiagrams are removed. The Schwinger term ($\alpha/2\pi$) survives. At two loops, some diagrams are nullified. The SCN prediction will differ from standard QED starting at $\mathcal{O}(\alpha^2)$.

The two-loop coefficient in standard QED ($-0.32848...$) includes contributions from:
- Diagrams with self-energy insertions: **nullified**
- Pure vertex-correction and VP-type diagrams: **survive**

Computing the SCN-filtered two-loop coefficient is a key numerical target.

### 6.2 Cross-Section: $e^+e^- \to \mu^+\mu^-$

At tree level (identical under both):

$$\sigma_0 = \frac{4\pi\alpha^2}{3s}$$

At one loop:
- VP correction to the photon propagator: **survives** → gives running $\alpha(s)$
- Vertex corrections: **survive** → give form-factor modifications
- Self-energy corrections: **nullified** → absent

The SCN prediction differs from standard QED by the **absence of fermion self-energy corrections** to external legs (LSZ factors). In standard QED, these contribute $Z_2 - 1$ factors that are absorbed into the definition of physical fields. Under SCN, $Z_2 = 1$ identically, simplifying the LSZ prescription.

### 6.3 Quantitative Comparison

The deviations between SCN-QED and standard QED at one-loop level are:

For the $e^+e^- \to \mu^+\mu^-$ total cross-section:
$$\frac{\sigma_{\text{SCN}} - \sigma_{\text{std}}}{\sigma_{\text{std}}} \sim \mathcal{O}\left(\frac{\alpha}{\pi}\right) \approx 0.2\%$$

This is within the precision of many experiments but could be distinguishable in high-precision measurements.

---

## 7. Physical SCN: The Corrected Classification

The systematic formulation comparison (`scn_formulations.ipynb`) tested four SCN interpretations against experiment. Only **Physical SCN** (skeleton expansion) survives:

**Definition:** Physical SCN computes perturbation theory using 1PI self-energy diagrams with bare propagators only, without Dyson resummation. Equivalently: use the skeleton expansion (Weinberg Ch.12, Zinn-Justin Ch.9).

### 7.1 Corrected One-Loop Classification

| Diagram | Diagrammatic SCN (§3) | Physical SCN (correct) |
|---------|----------------------|----------------------|
| Electron self-energy $\Sigma^{(1)}$ | Nullified | **SURVIVES** (1PI diagram) |
| Vacuum polarization $\Pi^{(1)}$ | Survives | **SURVIVES** (1PI diagram) |
| Vertex correction $\Lambda^{(1)}$ | Survives | **SURVIVES** |

Under Physical SCN, **all 1-loop QED diagrams survive** — the theory is identical to standard QED at 1-loop by construction. This is why the Lamb shift (1057 MHz) and Schwinger g-2 (α/2π) are reproduced exactly.

> **Honesty note:** 1-loop agreement is a consistency check, not evidence for Physical SCN. The definition was chosen to agree at 1-loop.

### 7.2 Two-Loop Classification Under Physical SCN

At two loops, Physical SCN differs from standard QED. Of the 7 two-loop QED vertex diagrams contributing to $a_e$:

| Diagram | Description | Physical SCN |
|---------|-------------|-------------|
| I(a) | SE insertion on upper fermion | **NULLIFIED** (non-1PI SE insertion) |
| I(b) | SE insertion on lower fermion | **NULLIFIED** |
| I(c) | SE insertion on internal fermion | **NULLIFIED** |
| II | VP insertion on internal photon | **SURVIVES** (skeleton) |
| III(a) | Crossed photon exchange | **SURVIVES** (skeleton) |
| III(b) | Ladder diagram | **SURVIVES** (skeleton) |
| III(c) | Light-by-light scattering | **SURVIVES** (skeleton) |

The 4 surviving diagrams are exactly the **skeleton diagrams** — those with no self-energy subdiagram insertions.

### 7.3 The Make-or-Break Test

The two-loop coefficient in standard QED:

$$C_2^{\text{std}} = -0.328478965579\ldots$$

Under Physical SCN, only the 4 skeleton diagrams contribute to $C_2^{\text{PHY}}$. The experimental precision on $a_e$ (0.24 ppb) means any O(0.1) change in $C_2$ would be visible at ~10⁵σ. Computing $C_2^{\text{PHY}}$ is **the decisive test** of Physical SCN.

### 7.4 Gauge Invariance Under Physical SCN

The 1PI effective action $\Gamma[\phi]$ satisfies Slavnov-Taylor identities by construction. Physical SCN = "use $\Gamma$, don't iterate the Dyson equation" inherits gauge invariance from this. In background field formalism, individual skeleton diagrams are gauge-invariant. An explicit 2-loop computation would provide definitive confirmation but is not yet done.

### 7.5 Skeleton Expansion Connection

Physical SCN is equivalent to the **skeleton expansion** in standard QFT:
- All propagators are bare $G_0$
- All self-energy insertions are 1PI (no iteration)
- The coupling constant is the renormalized coupling (from VP, which is 1PI)

This means Physical SCN is not a new physics, but rather a different organizational scheme for perturbation theory. The non-trivial question is whether this scheme produces the same results order by order — which is answered by computing $C_2^{\text{PHY}}$.
