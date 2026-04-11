# Open Questions and Discussion Points

> **Status key:** ✅ RESOLVED | ⚠️ PARTIALLY RESOLVED | ❌ OPEN | 🔬 NEEDS COMPUTATION
>
> **Last updated after:** Formulation comparison framework ([scn_formulations.ipynb](scn_formulations.ipynb)) and risk audit (April 2026).

## 1. Foundational Questions

### Q1: Is "dynamic" SCN well-defined without a process algebra? — ✅ RESOLVED

The static version of SCN (in classical set theory) is either vacuously true (with Foundation) or inconsistent (with AFA). The physical version requires a dynamic interpretation — self-containment triggers nullification during a *process*. But we haven't specified the formal process algebra. What are the states, transitions, and composition rules?

**Suggested direction:** Use Milner's CCS (Calculus of Communicating Systems) or the π-calculus as the process algebra, with particles as processes and interactions as communication events. Self-containment becomes a recursive process definition, and SCN becomes a termination condition.

> **Resolution (Physical SCN):** The formulation comparison in [scn_formulations.ipynb](scn_formulations.ipynb) established that Physical SCN provides well-defined semantics without a full process algebra. Self-containment is defined via the Dyson equation: $G = G_0 + G_0 \Sigma G$ is self-referential because $G$ appears on both sides. This is equivalent to the **skeleton expansion** — a standard QFT concept (Weinberg Ch.12, Zinn-Justin Ch.9). The prescription is: compute $\Sigma$ using only skeleton diagrams with bare propagators $G_0$; do not iterate the Dyson equation. A formal process algebra may still be interesting but is no longer a prerequisite for applying SCN.

### Q2: Does SCN have a categorical formulation? — ❌ OPEN

Category theory provides tools for self-referential structures (fixed points, initial algebras, comonads). Is there a categorical version of SCN?

**Possible answer:** In the category **Set**, the axiom $S \in S \Rightarrow S = \emptyset$ relates to the initial algebra of the powerset functor. The empty set is the initial object. SCN says that any fixed point of the membership relation is the initial object. In categorical language: the only coalgebra for the "element-of" endofunctor whose carrier is its own element is the trivial coalgebra.

> **Notebook result:** The coalgebraic/algebraic perspective is developed computationally in [scn_foundations.ipynb](scn_foundations.ipynb), §4 (BRST–SCN analogy) and §6 (exterior derivative / de Rham cohomology under SCN). The Dyson equation iteration under SCN is shown to converge to a fixed point in §6.1.

### Q3: What about indirect self-containment? — ✅ RESOLVED

We've focused on direct self-containment ($S \in S$). What about $S \in T \in S$ (mutual containment) or longer chains? Should these also be nullified?

**Physical relevance:** In Feynman diagrams, this corresponds to overlapping divergences — e.g., a photon propagator correction that internally contains a vertex correction that internally contains a photon propagator correction. The chain $\gamma \to e\bar{e}(\text{with VP}) \to \gamma$ involves mutual containment.

**Working answer:** For now, we apply SCN only to direct self-containment (a propagator correction that uses the same type of propagator). Indirect cases are left for future investigation.

> **Resolution (Physical SCN):** Under Physical SCN, indirect self-containment is handled naturally. $A \to B \to A$ chains — where corrected-$A$ appears inside correction-to-$A$ via an intermediate $B$ — are exactly **nested self-energy insertions** at 2-loop. These are nullified at 2-loop under Physical SCN because they involve propagators that have been partially dressed (i.e., they use $G_1 = G_0 + G_0\Sigma_1 G_0$ instead of $G_0$). In the skeleton expansion language: they are non-skeleton diagrams.

---

## 2. Physical Questions

### Q4: How does SCN interact with gauge invariance at higher orders? — ⚠️ PARTIALLY RESOLVED

At one loop, we showed the Ward identity is preserved. But at two loops and beyond, the interplay between nullified and surviving diagrams becomes more complex. Gauge cancellations in standard QFT often involve self-energy, vertex, and box diagrams together.

**Test case:** Compute the two-loop QED contribution to $e^+e^- \to \mu^+\mu^-$ under SCN and verify gauge independence.

> **Progress (Physical SCN):** At 1-loop, Physical SCN is identical to standard QFT, so gauge invariance is trivially preserved. At 2-loop, the **skeleton expansion interpretation** provides a strong theoretical argument: the 1PI effective action $\Gamma[\phi]$ satisfies Slavnov–Taylor identities by construction (Zinn-Justin, Ch.9). Physical SCN ≡ "use $\Gamma$, don't iterate the Dyson equation" preserves gauge invariance because $\Gamma$ does. In the background field formalism, this argument is clean. In the standard formalism, gauge-fixing introduces additional subtleties at 2-loop. A complete proof requires explicit computation. **Status: theoretically likely resolved, awaits numerical confirmation.**

### Q5: Does SCN respect unitarity? — ⚠️ PARTIALLY RESOLVED

The optical theorem relates the imaginary part of forward scattering amplitudes to total cross-sections:

$$2 \,\text{Im}\, \mathcal{M}(a \to a) = \sum_f \int d\Pi_f \,|\mathcal{M}(a \to f)|^2$$

Removing self-energy diagrams from the left side (forward scattering amplitude) without removing corresponding terms from the right side (cross-sections) could violate this. Must verify.

> **Progress (Physical SCN):** At 1-loop, unitarity is trivially satisfied (identical to standard QFT). At 2-loop, Physical SCN removes only a **subset** of diagrams (nested SE insertions), so any unitarity violation would be a perturbative correction, not a catastrophic failure. Additionally, in the skeleton expansion, SE insertions and their cuts appear in matched pairs on both sides of the optical theorem — removing both sides simultaneously should preserve the identity. **Status: theoretically plausible, needs explicit 2-loop verification.**

### Q6: What is the SCN prediction for the Lamb shift? — ✅ RESOLVED

The Lamb shift ($2S_{1/2}$ – $2P_{1/2}$ splitting in hydrogen) receives contributions from:
- Vacuum polarization (Uehling term): **survives SCN**
- Electron self-energy: **survives under Physical SCN** (uses bare propagators at 1-loop)
- Vertex correction: **survives SCN**

Standard theory: Lamb shift $\approx 1057$ MHz

> **Resolution (Physical SCN):** Under Physical SCN, 1-loop self-energy survives because it uses bare propagators $G_0$ — there is no self-reference at the Dyson level. The Lamb shift prediction is **1057 MHz**, matching experiment. This was the **decisive test** that ruled out Structural and Diagrammatic SCN (both predict ~40 MHz). See [scn_formulations.ipynb](scn_formulations.ipynb), §4 for the full computation.
>
> **Formulations ruled out:** Structural SCN and Diagrammatic SCN are **empirically falsified** by the Lamb shift (predicted 40 MHz vs. measured 1057 MHz). Soft variants cannot rescue them without making $\Lambda_{\text{SCN}} \ll m_e$, at which point SCN has no observable effect.

### Q7: Is there a connection to the hierarchy problem? — ❌ OPEN (unchanged by Physical SCN)

The hierarchy problem in the Standard Model involves the Higgs mass receiving quadratically divergent self-energy corrections. Under Physical SCN, the 1-loop Higgs self-energy **survives** (it uses bare propagators), so the leading quadratic divergence is **not removed**. Higher-order nested corrections are suppressed, but the dominant contribution remains.

**If SCN could be made to work for QED/QCD**, its extension to the electroweak sector might address the hierarchy problem — one of the biggest open problems in particle physics.

> **Assessment (Physical SCN):** Physical SCN does NOT solve the hierarchy problem at 1-loop. The Higgs self-energy uses bare propagators → survives. Only nested 2+ loop corrections are removed, which are subleading. This was noted in [scn_formulations.ipynb](scn_formulations.ipynb), §10.

### Q8: What about anomalies? — ✅ RESOLVED

Quantum anomalies (chiral anomaly, trace anomaly) arise from loop diagrams. The chiral anomaly comes from the triangle diagram $\gamma \to \gamma\gamma$ (with a fermion loop). This diagram is NOT self-containing under any SCN formulation (no photon propagator inside the fermion-loop correction). So the chiral anomaly survives.

**Important:** The anomaly MUST survive for the theory to be consistent (anomaly cancellation is required for gauge theories).

> **Resolution:** The triangle diagram is not self-containing under any of the four SCN formulations (Literal, Structural, Diagrammatic, Physical). The chiral anomaly and anomaly cancellation are preserved. ✓

---

## 3. Computational Questions

### Q9: Can self-containment detection be automated? — ✅ RESOLVED

Checking all subdiagrams of a Feynman diagram is in principle a graph isomorphism problem (NP, possibly not NP-complete). For the diagrams relevant to low-order perturbation theory (<5 loops), this is computationally tractable.

**Implementation:** The `src/diagrams.py` code implements this for 1-loop diagrams. The `src/scn_models.py` module provides four formulation classes, each with a `classify(diagram)` method.

> **Resolution:** Implemented and tested. The `src/scn_models.py` module provides `classify()` for all four formulations. At 1-loop, classification is exact. At 2-loop, classification currently uses proxy flags (`has_nested_self_energy`); the simulation engine will extend this to full topological analysis. See [scn_formulations.ipynb](scn_formulations.ipynb), §1 for the classification table.
>
> **Known limitation (Risk 4):** The `g2_components()` method uses hand-coded tables rather than deriving results from `classify()`. The simulation engine will unify these by generating actual 2-loop diagram topologies.

### Q10: Can we use existing QFT tools? — ✅ RESOLVED

Tools like FORM, FeynCalc, FeynArts, MadGraph generate and evaluate Feynman diagrams. Can we add an SCN filter pass?

**Yes:** The filter is a post-generation step. Generate all diagrams for a process at a given order, then apply the self-containment predicate, then evaluate only the surviving diagrams. This is implementable as a plugin for existing tools.

> **Resolution:** Confirmed. The `src/scn_filter.py` and `src/scn_models.py` modules implement exactly this pattern: generate → classify → filter → evaluate. Under Physical SCN, this is equivalent to selecting only skeleton diagrams, which is a well-defined concept in standard QFT tools.

---

## 4. Questions for Discussion — Resolutions

### D1: Which definition of self-containment feels most natural? — ✅ ANSWERED

- **(a) Literal:** $S \in S$ (only direct membership) — **TRIVIAL** in perturbation theory (no diagram literally contains itself)
- **(b) Structural:** A set contains a sub-structure isomorphic to itself — **RULED OUT** by Lamb shift (predicts 40 MHz vs. 1057 MHz measured)
- **(c) Diagrammatic:** A Feynman diagram correcting a propagator uses that propagator type internally — **RULED OUT** by Lamb shift (same as Structural at 1-loop)
- **(d) Physical-observable:** Self-containment is defined at the level of dressed propagators (Dyson equation) — **★ VIABLE** (agrees with standard QFT at 1-loop; testable at 2-loop)

> **Resolution:** Physical SCN (option d) is the only non-trivial viable formulation. See [scn_formulations.ipynb](scn_formulations.ipynb) for the complete comparative analysis. It has a precise restatement as the **skeleton expansion** — compute using only skeleton (2PI) self-energy diagrams with bare propagators; do not iterate the Dyson equation.

### D2: Should SCN apply to vertices as well as propagators? — ✅ ANSWERED

> **Resolution:** Under Physical SCN, this question dissolves. Self-containment is defined at the Dyson equation level, not at the diagram level. Vertex corrections are not self-referential in the Dyson sense (they don't define themselves in terms of themselves). At 1-loop, all vertex corrections survive. At 2-loop, a vertex diagram that *contains* a nested self-energy insertion has that insertion nullified — but this is because the SE is self-referential, not because the vertex is. Structural SCN (which does nullify nested vertex corrections) is ruled out.

### D3: How should we handle the QCD asymptotic freedom issue? — ✅ RESOLVED

- ~~**(a)** Accept that SCN modifies QCD and explore the consequences~~
- ~~**(b)** Refine the self-containment criterion to preserve asymptotic freedom~~
- **(c)** Apply SCN only to physical observables (Resolution C) ← **THIS IS PHYSICAL SCN**
- ~~**(d)** Treat it as evidence that SCN is not applicable to QCD~~

> **Resolution:** Physical SCN preserves the standard QCD $\beta_0 = (11C_A - 4T_F n_f)/3$ at 1-loop because all 1-loop diagrams use bare propagators and survive. Asymptotic freedom is maintained for $n_f \leq 16$. The Structural/Diagrammatic formulations (which lose AF) are ruled out. See [scn_formulations.ipynb](scn_formulations.ipynb), §2–3.

### D4: What energy regime should the simulations focus on? — ✅ ANSWERED

> **Resolution:** Focus on **(b) intermediate QED** (MeV–GeV) for the most immediate testable predictions. The make-or-break test is the **2-loop electron $g-2$ coefficient $C_2$**, which is a pure QED calculation at the ~MeV scale. If Physical SCN passes this test, extend to (a) atomic physics and (c) QCD. The simulation engine should handle arbitrary QED processes at 1-loop and compute skeleton diagram contributions at 2-loop.

---

## 5. Prioritized Next Steps (Updated)

| Priority | Task | Status |
|----------|------|--------|
| 1 | ~~Calculate the Lamb shift under SCN~~ | ✅ Done — 1057 MHz under Physical SCN |
| 2 | **Compute $C_2^{\text{PHY}}$ for $g-2$** | 🔬 NEXT — classify 7 two-loop vertex diagrams, sum skeleton contributions |
| 3 | ~~Run the simulation code~~ | ✅ Done — [scn_formulations.ipynb](scn_formulations.ipynb) |
| 4 | ~~Explore Resolution C for QCD~~ | ✅ Done — Physical SCN IS Resolution C |
| 5 | Verify unitarity at 2-loop | ⚠️ Theoretically likely OK (skeleton argument), needs computation |
| 6 | **Build simulation engine** | 🔬 NEXT — generate → filter → integrate → renormalize pipeline |
| 7 | Verify gauge invariance at 2-loop | ⚠️ Strong theoretical support, needs explicit calculation |

> **Progress:** Items 1, 3, 4 are complete. The Koide formula, $\theta_0 = 2/9$ discovery, and Soft SCN QCD model are explored in [scn_investigations.ipynb](scn_investigations.ipynb). Mathematical foundations in [scn_foundations.ipynb](scn_foundations.ipynb). Formulation comparison in [scn_formulations.ipynb](scn_formulations.ipynb). The simulation engine is the primary vehicle for items 2, 5, 6, 7.

---

## 6. Known Risks and Honest Assessment

This section documents intellectual risks identified during our self-audit. Transparency is essential.

### Risk 1: Physical SCN vacuousness — RESOLVED

**Concern:** In perturbation theory, every diagram uses bare propagators. No diagram literally uses the dressed propagator. So Physical SCN might be Literal SCN (= standard QFT) at all orders.

**Resolution:** Physical SCN is NOT vacuous. 2-loop diagrams with nested SE insertions use **partially corrected propagators** ($G_1 = G_0 + G_0\Sigma_1 G_0$), which ARE self-referential at the Dyson level. Physical SCN ≡ skeleton expansion, which is a well-defined, non-trivial prescription that removes specific diagrams starting at 2-loop.

**Caveat:** The connection to the set-theoretic axiom $\forall S: S \in S \Rightarrow S = \emptyset$ is **motivational**, not deductive. The axiom suggests the prescription; it does not logically force it.

### Risk 2: Koide/θ₀ independence — CONFIRMED (must separate in documentation)

**Concern:** The Koide formula ($Q = 2/3$) and $\theta_0 = 2/9$ are phenomenological observations about lepton masses that work identically with or without SCN.

**Status:** Confirmed. These are NOT SCN predictions. The Z₃ nesting-depth narrative is suggestive but not a derivation. All documentation must clearly separate "interesting phenomenology" from "SCN-specific results." The README and theory docs have been updated accordingly.

### Risk 3: Circular reasoning in formulation selection — PARTIALLY RESOLVED

**Concern:** We defined Physical SCN so that 1-loop results survive, then cited 1-loop agreement as evidence.

**Resolution:** The definition is physically motivated (bare vs. dressed propagators) and maps to a standard concept (skeleton expansion), so it is not purely ad-hoc. However, **1-loop agreement must NOT be cited as evidence** for Physical SCN. The real test is at 2-loop ($C_2^{\text{PHY}}$), which we have not yet computed.

### Risk 4: Code inconsistency — CONFIRMED (to be fixed in simulation engine)

**Concern:** `g2_components(loop_order=2)` is hand-coded rather than derived from `classify()`. At 2-loop, vertex diagrams **containing** SE insertions should be partially nullified, but `classify()` only checks the top-level diagram type.

**Resolution:** The simulation engine will unify these by generating actual 2-loop diagram topologies and classifying subdiagrams. The hand-coded tables are acknowledged as placeholders.

### Risk 5: Gauge invariance at 2-loop — LIKELY RESOLVED (theoretical argument)

**Concern:** Removing nested SE insertions could break Ward-Takahashi identities at 2-loop.

**Resolution:** The skeleton expansion interpretation provides strong theoretical support. The 1PI effective action $\Gamma[\phi]$ satisfies Slavnov-Taylor identities by construction. Physical SCN = "use $\Gamma$ without Dyson resummation" inherits this gauge symmetry. In the background field formalism, this is clean. Explicit 2-loop computation would provide definitive confirmation.
