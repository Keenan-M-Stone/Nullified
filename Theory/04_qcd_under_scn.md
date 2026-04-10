# QCD Under SCN: Detailed Analysis

## 1. QCD Review

Quantum Chromodynamics describes the strong interaction between quarks and gluons:

$$\mathcal{L}_{\text{QCD}} = \sum_f \bar{q}_f(i\gamma^\mu D_\mu - m_f)q_f - \frac{1}{4}G^a_{\mu\nu}G^{a\mu\nu}$$

with $D_\mu = \partial_\mu - ig_s T^a A^a_\mu$ and $G^a_{\mu\nu} = \partial_\mu A^a_\nu - \partial_\nu A^a_\mu + g_s f^{abc}A^b_\mu A^c_\nu$.

Crucially, the non-Abelian field strength contains the $f^{abc}A^b_\mu A^c_\nu$ term, generating **gluon self-interactions** absent in QED. This is the structural feature that makes QCD under SCN fundamentally different from QED under SCN.

### 1.1 QCD Feynman Rules

Building blocks:
- **Quark propagator:** $\frac{i(\not{p}+m)\delta_{ij}}{p^2 - m^2}$ (color indices $i,j$)
- **Gluon propagator:** $\frac{-ig_{\mu\nu}\delta^{ab}}{k^2}$ (color indices $a,b$)
- **Quark-gluon vertex:** $-ig_s \gamma^\mu T^a_{ij}$
- **Triple-gluon vertex:** $g_s f^{abc}[g^{\mu\nu}(k_1-k_2)^\rho + \text{cyclic}]$
- **Four-gluon vertex:** $-ig_s^2 [f^{abe}f^{cde}(g^{\mu\rho}g^{\nu\sigma}-g^{\mu\sigma}g^{\nu\rho}) + \text{perms}]$
- **Ghost propagator:** $\frac{i\delta^{ab}}{k^2}$
- **Ghost-gluon vertex:** $g_s f^{abc} k^\mu$

---

## 2. Self-Containment Classification in QCD

### 2.1 Gluon Self-Interaction: The Central Challenge

Unlike QED where the gauge boson (photon) doesn't self-interact, gluons carry color charge and interact with each other. This creates self-containment scenarios absent in QED.

### 2.2 One-Loop Gluon Self-Energy Diagrams

There are three contributions to the one-loop gluon self-energy:

#### (a) Quark Loop

```
    g ~~~~●——→——●~~~~ g
              ↑  |
              |  ↓
              ←——
           (q q̄ loop)
```

The gluon propagator is corrected by a quark-antiquark loop. Internal lines are quarks, not gluons.

**Self-containing?** NO — the internal structure (quark propagators) differs from the external structure (gluon propagator).

**SCN status:** SURVIVES ✓

#### (b) Gluon Loop

```
    g ~~~~●~~~~●~~~~ g
              |  |
              g  g
              |  |
              ●~~~~
         (gluon loop)
```

The gluon propagator is corrected by a loop of virtual gluons (via triple-gluon vertices). Internal lines include gluon propagators — the same type as the external line being corrected.

**Self-containing?** YES — the gluon propagator correction uses internal gluon propagators.

**SCN status:** NULLIFIED ✗

#### (c) Ghost Loop

```
    g ~~~~●- - -●~~~~ g
              ↑  |
              |  ↓
              - --
          (ghost loop)
```

The ghost loop corrects the gluon propagator. Internal lines are Faddeev–Popov ghosts, not gluons.

**Self-containing?** NO — internal structure (ghost propagators) differs from external (gluon).

**SCN status:** SURVIVES ✓

### 2.3 One-Loop Quark Self-Energy

```
    q ——→——●~~~~●——→—— q
              |  ↑
              g  |
              ↓  |
         q ——→——●
```

The quark propagator correction contains an internal quark propagator (same type as external).

**Self-containing?** YES

**SCN status:** NULLIFIED ✗

### 2.4 Vertex Corrections

**Quark-gluon vertex correction (gluon exchange):** Contains internal quark and gluon propagators. No nested vertex correction. **NOT self-containing. SURVIVES.** ✓

**Triple-gluon vertex correction (gluon loop):** A correction to the triple-gluon vertex that internally contains triple-gluon vertices. The correction to a gluon self-coupling uses the same gluon self-coupling — this is self-referential.

**Self-containing?** This requires careful analysis. The internal triple-gluon vertices are tree-level vertices, not corrected vertices. Under our definition (the correction must contain a nested correction of the same type), a one-loop correction to the triple-gluon vertex that only uses tree-level triple-gluon vertices internally is **NOT** self-containing.

**SCN status of triple-gluon vertex correction:** SURVIVES ✓ (at one loop)

However, a **two-loop** correction that contains a one-loop vertex correction sub-diagram WOULD be self-containing → NULLIFIED.

---

## 3. Impact on the QCD β-Function

### 3.1 Standard QCD β-Function

The one-loop β-function coefficient:

$$\beta_0 = \frac{11C_A}{3} - \frac{4T_F n_f}{3}$$

For $SU(3)$: $C_A = 3$, $T_F = 1/2$, giving:

$$\beta_0 = 11 - \frac{2n_f}{3}$$

The contributions come from:
- Gluon self-energy (gluon loop): contributes to the $11C_A/3 = 11$ (partial)
- Gluon self-energy (ghost loop): contributes to the $11C_A/3 = 11$ (partial)
- Gluon self-energy (quark loop): contributes the $-2n_f/3$
- Vertex corrections: contribute to both terms

### 3.2 SCN-Filtered β-Function

Under SCN, the gluon-loop contribution to the gluon self-energy is nullified. This removes a significant part of the $11C_A/3$ term.

**Detailed decomposition:**

The gluon contribution to $\beta_0$ can be traced through the gluon vacuum polarization tensor $\Pi^{ab}_{\mu\nu}(q)$. The gauge-invariant combination involves:

- Gluon loop: $\Pi^{\text{gl}}$: Contributes $\frac{10C_A}{3}$ to $\beta_0$ → **NULLIFIED**
- Ghost loop: $\Pi^{\text{gh}}$: Contributes $\frac{C_A}{3}$ to $\beta_0$ → **SURVIVES**
- Quark loop: $\Pi^{\text{q}}$: Contributes $-\frac{4T_Fn_f}{3}$ to $\beta_0$ → **SURVIVES**

**SCN β-function (tentative):**

$$\beta_0^{\text{SCN}} = \frac{C_A}{3} - \frac{4T_F n_f}{3} = 1 - \frac{2n_f}{3}$$

For $n_f \geq 2$: $\beta_0^{\text{SCN}} < 0$ → the coupling **increases** at high energies → **NO asymptotic freedom**.

### 3.3 The Asymptotic Freedom Problem

This is a **critical issue**. Asymptotic freedom is experimentally confirmed:
- Deep inelastic scattering scaling violations
- Jet production rates at varying $\sqrt{s}$
- Lattice QCD calculations

If SCN destroys asymptotic freedom, the framework is empirically falsified for QCD — at least in its naive form.

### 3.4 Possible Resolutions

#### Resolution A: Modified Self-Containment Criterion

Perhaps the gluon-loop contribution to the gluon self-energy should NOT be classified as self-containing. Argument: the gluon loop connects to the external gluon line through triple-gluon *vertices*, not through gluon *propagators* of the same topology. The self-interaction is a vertex effect, not a propagator effect.

Under this revised criterion: gluon self-energy (gluon loop) SURVIVES, and $\beta_0$ is unchanged.

**Trade-off:** This weakens the SCN principle by introducing ambiguity in the definition of self-containment for non-Abelian theories.

#### Resolution B: SCN-Modified Running

Perhaps the correct interpretation is not that $\beta_0$ changes, but that the running coupling under SCN follows a different RG equation:

$$\mu\frac{d\alpha_s}{d\mu} = -\beta_0^{\text{SCN}} \alpha_s^2 - \beta_1^{\text{SCN}} \alpha_s^3 - \cdots$$

With $\beta_0^{\text{SCN}} = 1 - \frac{2n_f}{3}$ and suitable higher-order coefficients, the theory might still exhibit effective asymptotic freedom in a limited energy range or through higher-order effects.

#### Resolution C: SCN Applies Only to Physical Propagators

Perhaps SCN should be applied to physical (gauge-invariant) quantities only, not to individual Feynman diagrams in a fixed gauge. The gluon self-energy is gauge-dependent; the physical observable (e.g., a cross-section) is not. When combined with vertex corrections (which survive), the gauge-invariant result may preserve asymptotic freedom.

This is the most physically motivated resolution and requires explicit calculation.

#### Resolution D: Accept Modified QCD

Perhaps the SCN framework predicts a different strong-force behavior that approaches known QCD only in certain limits. This would be an empirically falsifiable prediction:

- At currently probed energies, standard QCD works. If SCN-QCD gives different predictions, we can identify the energy scale of divergence and test it.

---

## 4. Confinement Under SCN

### 4.1 The Confinement Argument

One of the attractive features of SCN for QCD is a natural confinement mechanism:

1. An isolated gluon state involves gluon self-interactions (the gluon field equation involves the $f^{abc}$ term)
2. These self-interactions create a self-referential state structure
3. Under SCN, this self-referential structure nullifies → isolated gluon states collapse to the vacuum
4. Only color-neutral combinations (where the self-interactions are "screened") survive as physical states

### 4.2 Formal Statement

Define a **color state** $|c\rangle$ as a set containing the particle's color charge and its interaction history. For an isolated gluon:

$$|g^a\rangle = \{c_a,\; p,\; \varepsilon,\; V_{\text{self}}(g^a)\}$$

where $V_{\text{self}}(g^a)$ represents the gluon's self-coupling, which involves $g^a$ itself. This is self-containment: the state-set references the state-set.

Under SCN: $|g^a\rangle \to |\emptyset\rangle = |0\rangle$ (vacuum).

For a color-singlet state like a meson $|q\bar{q}\rangle$:

$$|q\bar{q}\rangle = \{q_i,\; \bar{q}^i,\; V_{q\bar{q}}\}$$

The interaction $V_{q\bar{q}}$ involves gluon exchange but the state itself is a quark-antiquark pair — no particle in the state is the same type as the state itself. Not self-containing → survives.

### 4.3 Limitations

This argument is **qualitative, not quantitative**. Real confinement involves:
- Linear potential at large distances
- String breaking
- Flux tubes
- A mass gap

SCN provides a selection-rule argument for WHY confinement occurs but does not derive these specific features. Whether the quantitative details emerge from a careful SCN-based calculation is an open question.

---

## 5. Color Factor Analysis

### 5.1 SCN-Filtered Color Factors

In standard QCD, amplitudes involve color factors built from $T^a_{ij}$ (fundamental) and $f^{abc}$ (structure constants). Under SCN filtering:

**Surviving contributions use:**
- $T^a_{ij}T^a_{kl}$ (quark-gluon interactions) → CF factor $C_F = (N^2-1)/(2N)$
- $f^{abc}$ in vertex corrections (tree-level vertices, not self-containing loops) → $C_A$ from vertices

**Nullified contributions lose:**
- $f^{acd}f^{bcd}$ from gluon-loop self-energy → removes some $C_A$ contributions
- The Casimir scaling between fundamental and adjoint representations is modified

### 5.2 Impact on Color Flow

The surviving diagrams favor "quark-type" color flow over "gluon-type" color flow. This has observable consequences:
- Jet color-charge patterns
- Particle multiplicity ratios between quark and gluon jets
- Color coherence effects

---

## 6. Summary Table: QCD Diagrams at One Loop

| Diagram | Internal content | Self-containing? | SCN status |
|---------|-----------------|-------------------|------------|
| Quark self-energy | quark + gluon | Yes (quark line) | Nullified |
| Gluon SE (quark loop) | quark pair | No | Survives |
| Gluon SE (gluon loop) | gluons | Yes (gluon line) | Nullified |
| Gluon SE (ghost loop) | ghosts | No | Survives |
| Quark-gluon vertex | quark + gluon | No (tree vertices) | Survives |
| Triple-gluon vertex (1L) | gluons | No (tree vertices) | Survives |
| Four-gluon vertex (1L) | Case-by-case | Depends | Case-by-case |

---

## 7. Key Open Questions for QCD

1. **Can asymptotic freedom be recovered** through a physically motivated refinement of SCN?
2. **Does the confinement argument** produce quantitatively correct predictions (mass gap, string tension)?
3. **What are the SCN predictions** for $e^+e^-$ → hadrons ($R$-ratio) at different energies?
4. **How does SCN affect** the parton distribution functions (PDFs) and DGLAP evolution?
5. **Is the ghost sector** treatment consistent with BRST symmetry under SCN?

These questions require both analytical work and numerical simulation — the code in `src/` addresses item 3.
