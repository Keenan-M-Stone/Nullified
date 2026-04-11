# QED Under SCN: Detailed Analysis

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

## 7. Key Takeaway

SCN-filtered QED is a **consistent, gauge-invariant** theory at one loop that:
1. Preserves the Schwinger anomalous magnetic moment
2. Preserves the running of $\alpha$ from vacuum polarization
3. Eliminates mass renormalization (bare mass = physical mass at one loop)
4. Satisfies Ward identities
5. Makes distinct predictions from standard QED at $\mathcal{O}(\alpha^2)$ and beyond

The framework is testable and the deviations are computable.
