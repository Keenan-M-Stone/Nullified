# Consequences and Predictions of SCN-Filtered QFT

## 1. Summary of SCN's Effects

The SCN axiom, applied to QFT through the Feynman diagram self-containment filter, produces the following structural changes:

| Feature | Standard QFT | SCN-Filtered QFT |
|---------|-------------|-------------------|
| Self-energy corrections | Present, divergent, renormalized | Nullified at all orders |
| Vacuum polarization | Present | Present (unchanged) |
| Vertex corrections | Present | Present (unchanged) |
| Mass renormalization | Required ($m_{\text{bare}} \neq m_{\text{phys}}$) | Absent ($m_{\text{bare}} = m_{\text{phys}}$) |
| Field renormalization $Z_2$ | $\neq 1$ | $= 1$ |
| Ward identity $Z_1 = Z_2$ | Non-trivial check | Trivially $1 = 1$ |
| Coupling renormalization | From VP + vertex + SE | From VP + vertex only |

---

## 2. Concrete Predictions

### 2.1 Prediction: Bare Mass = Physical Mass

**Standard QFT:** The electron mass receives radiative corrections:

$$m_{\text{phys}} = m_{\text{bare}} + \delta m, \quad \delta m = \frac{3\alpha}{4\pi}m\ln\frac{\Lambda^2}{m^2} + \cdots$$

This correction is absorbed into the definition of the physical mass via renormalization.

**SCN-QFT:** Self-energy is nullified, so $\delta m = 0$ and $m_{\text{bare}} = m_{\text{phys}}$ at all orders.

**Consequence:** The bare parameters in the Lagrangian are directly physical. No fine-tuning is needed between bare and physical masses. This is reminiscent of the finite-QFT programs explored by various authors.

**Testability:** This is not directly testable (bare parameters are not observable), but it affects the structure of higher-order calculations and the relationship between parameters.

### 2.2 Prediction: Modified Anomalous Magnetic Moment at Higher Orders

The electron $g-2$ at various orders:

$$a_e = C_1\frac{\alpha}{\pi} + C_2\left(\frac{\alpha}{\pi}\right)^2 + C_3\left(\frac{\alpha}{\pi}\right)^3 + \cdots$$

**Standard QED:**
- $C_1 = 1/2$ (Schwinger, survives SCN)
- $C_2 = -0.328\,478\,965\ldots$ (includes self-energy insertions)
- $C_3 = 1.181\,241\,456\ldots$

**SCN-QED:** $C_1^{\text{SCN}} = 1/2$ (identical).

For $C_2^{\text{SCN}}$: the two-loop diagrams fall into categories:
1. Diagrams with electron self-energy insertions → **nullified**
2. Diagrams with only vertex corrections and vacuum polarization → **survive**

The 7 two-loop vertex diagrams in standard QED include:
- (a) SE insertion on external leg → nullified
- (b) SE insertion on internal leg → nullified  
- (c) VP insertion on internal photon → survives
- (d) Crossed-photon vertex → survives
- (e) Uncrossed double-vertex → survives
- (f,g) Light-by-light type → survives

Rough estimate: $C_2^{\text{SCN}} \approx -0.17$ (removal of SE-containing diagrams shifts the coefficient toward zero).

**Experimental precision:** $a_e$ is measured to $0.24 \text{ ppb}$. The two-loop contribution is $\sim 1.1 \times 10^{-6}$, so a change in $C_2$ of order $0.16$ would shift $a_e$ by $\Delta a_e \sim 0.16 \times (\alpha/\pi)^2 \approx 8.6 \times 10^{-8}$.

This is **orders of magnitude larger than experimental uncertainty**. If $C_2^{\text{SCN}} \neq C_2^{\text{std}}$, the theory is testable and potentially falsifiable.

### 2.3 Prediction: Unmodified Running of $\alpha$

Since vacuum polarization survives SCN filtering:

$$\alpha(q^2) = \frac{\alpha}{1 - \frac{\alpha}{3\pi}\ln\frac{q^2}{m_e^2}}$$

at one loop, identical to standard QED. The running of $\alpha$ from $\alpha(0) \approx 1/137.036$ to $\alpha(M_Z) \approx 1/128$ is preserved.

**Testability:** Consistent with experiment ✓

### 2.4 Prediction: Modified QCD Coupling Evolution

As derived in [04_qcd_under_scn.md](04_qcd_under_scn.md), the SCN-filtered $\beta$-function may lose the gluon-loop contribution:

$$\beta_0^{\text{SCN}} = \frac{C_A}{3} - \frac{4T_Fn_f}{3}$$

For $SU(3)$ with $n_f = 6$: $\beta_0^{\text{SCN}} = 1 - 4 = -3$ (vs. standard $\beta_0 = 11 - 4 = 7$).

This predicts $\alpha_s$ **increases** with energy, contradicting deep inelastic scattering data, jet rates at LEP/LHC, and lattice QCD.

**Status:** This is a **falsifying prediction** unless Resolution C or D from the QCD analysis applies.

### 2.5 Prediction: Natural Confinement Selection Rule

SCN provides a structural reason for confinement: self-interacting color-charged states are self-containing and nullify. Only color-neutral combinations avoid this.

**Testability:** Qualitatively consistent with observation. Quantitative predictions (hadron spectrum, string tension) require further development.

---

## 3. Hierarchy of Confidence

Based on the analysis:

| Prediction | Confidence | Agreement with experiment |
|-----------|-----------|--------------------------|
| Tree-level QED cross-sections | ★★★★★ | Perfect (trivially) |
| One-loop $a_e$ (Schwinger) | ★★★★★ | Perfect |
| Running $\alpha$ | ★★★★☆ | Consistent |
| Ward identities preserved | ★★★★☆ | Consistent |
| No mass renormalization needed | ★★★☆☆ | Not directly testable |
| Two-loop $a_e$ | ★★☆☆☆ | Likely disagrees — critical test |
| Confinement mechanism | ★★☆☆☆ | Qualitatively consistent |
| QCD asymptotic freedom | ★☆☆☆☆ | Likely disagrees — major issue |

---

## 4. The Fork in the Road

The SCN framework reaches a decision point at two places:

### Fork 1: The Two-Loop $g-2$

If $C_2^{\text{SCN}} \neq C_2^{\text{std}}$ and experiment matches $C_2^{\text{std}}$ (which it does), then either:
- **(a)** SCN is falsified at two-loop QED, OR
- **(b)** The self-containment criterion must be refined so that the relevant two-loop diagrams are NOT classified as self-containing

Option (b) is possible but must not be ad hoc — the refined criterion must follow from a clear principle.

### Fork 2: QCD Asymptotic Freedom

If SCN-QCD lacks asymptotic freedom, then either:
- **(a)** SCN is falsified for QCD, OR
- **(b)** The self-containment criterion must be resolution-dependent (applying differently at different scales), OR
- **(c)** SCN applies only to physical observables, not individual diagrams, and the gauge-invariant combination preserves asymptotic freedom

Option (c) is the most promising and most physically motivated.

---

## 5. The "Physical Observable" Resolution

### 5.1 Principle

**Refined SCN:** Self-containment is not a property of individual Feynman diagrams (which are gauge-dependent) but of gauge-invariant combinations contributing to physical observables.

A physical observable $\mathcal{O}$ is self-containing if its perturbative expansion at order $n$ references $\mathcal{O}$ itself at order $n' < n$. This happens in the Dyson equation for dressed propagators but NOT in the perturbative expansion of cross-sections (which are computed order-by-order from bare parameters).

### 5.2 Implications

Under this refined principle:
- Individual self-energy diagrams are NOT nullified (they don't individually constitute a physical observable)
- Instead, the **dressed propagator** (the solution of the Dyson equation) is where self-containment occurs
- The dressed propagator is defined as $G = G_0 + G_0 \Sigma G$ — which references $G$ on both sides

Under SCN: the self-consistent Dyson equation has no non-trivial solution → $G = G_0$ (the free propagator).

This gives the same prediction (no self-energy corrections) but arrives at it through a gauge-invariant principle that doesn't interfere with individual diagram contributions to other observables.

### 5.3 Impact on QCD β-Function

Under this refined principle, the gluon self-energy diagrams contribute to the β-function normally at fixed order, but the dressed gluon propagator is the bare propagator. The running coupling comes from vertex corrections and vacuum polarization only, potentially preserving asymptotic freedom through a different mechanism.

This requires careful calculation — it's the primary objective of the simulation code.

---

## 6. Experimental Targets for Simulation

Priority list for numerical comparison:

1. **$e^+e^- \to \mu^+\mu^-$ total cross-section** vs. $\sqrt{s}$ — pure QED, well-measured
2. **Electron $g-2$** — highest precision test, requires two-loop calculation
3. **$R$-ratio** ($\sigma(e^+e^- \to \text{hadrons})/\sigma(e^+e^- \to \mu^+\mu^-)$) — tests QCD corrections
4. **$\alpha_s(M_Z)$** — tests QCD running coupling
5. **Drell–Yan cross-section** — tests quark-parton model with QCD corrections

The simulation code in `src/` addresses items 1 and 3, with the framework extensible to the others.
