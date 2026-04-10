# Open Questions and Discussion Points

## 1. Foundational Questions

### Q1: Is "dynamic" SCN well-defined without a process algebra?

The static version of SCN (in classical set theory) is either vacuously true (with Foundation) or inconsistent (with AFA). The physical version requires a dynamic interpretation — self-containment triggers nullification during a *process*. But we haven't specified the formal process algebra. What are the states, transitions, and composition rules?

**Suggested direction:** Use Milner's CCS (Calculus of Communicating Systems) or the π-calculus as the process algebra, with particles as processes and interactions as communication events. Self-containment becomes a recursive process definition, and SCN becomes a termination condition.

### Q2: Does SCN have a categorical formulation?

Category theory provides tools for self-referential structures (fixed points, initial algebras, comonads). Is there a categorical version of SCN?

**Possible answer:** In the category **Set**, the axiom $S \in S \Rightarrow S = \emptyset$ relates to the initial algebra of the powerset functor. The empty set is the initial object. SCN says that any fixed point of the membership relation is the initial object. In categorical language: the only coalgebra for the "element-of" endofunctor whose carrier is its own element is the trivial coalgebra.

### Q3: What about indirect self-containment?

We've focused on direct self-containment ($S \in S$). What about $S \in T \in S$ (mutual containment) or longer chains? Should these also be nullified?

**Physical relevance:** In Feynman diagrams, this corresponds to overlapping divergences — e.g., a photon propagator correction that internally contains a vertex correction that internally contains a photon propagator correction. The chain $\gamma \to e\bar{e}(\text{with VP}) \to \gamma$ involves mutual containment.

**Working answer:** For now, we apply SCN only to direct self-containment (a propagator correction that uses the same type of propagator). Indirect cases are left for future investigation.

---

## 2. Physical Questions

### Q4: How does SCN interact with gauge invariance at higher orders?

At one loop, we showed the Ward identity is preserved. But at two loops and beyond, the interplay between nullified and surviving diagrams becomes more complex. Gauge cancellations in standard QFT often involve self-energy, vertex, and box diagrams together.

**Test case:** Compute the two-loop QED contribution to $e^+e^- \to \mu^+\mu^-$ under SCN and verify gauge independence.

### Q5: Does SCN respect unitarity?

The optical theorem relates the imaginary part of forward scattering amplitudes to total cross-sections:

$$2 \,\text{Im}\, \mathcal{M}(a \to a) = \sum_f \int d\Pi_f \,|\mathcal{M}(a \to f)|^2$$

Removing self-energy diagrams from the left side (forward scattering amplitude) without removing corresponding terms from the right side (cross-sections) could violate this. Must verify.

### Q6: What is the SCN prediction for the Lamb shift?

The Lamb shift ($2S_{1/2}$ – $2P_{1/2}$ splitting in hydrogen) receives contributions from:
- Vacuum polarization (Uehling term): **survives SCN**
- Electron self-energy: **nullified under SCN**
- Vertex correction: **survives SCN**

Standard theory: Lamb shift $\approx 1057$ MHz

Under SCN, the self-energy contribution (which is the dominant part) is removed. This would give a dramatically different prediction — likely a severe test.

**Priority:** Calculate this explicitly. If SCN removes the dominant self-energy contribution to the Lamb shift, the theory is in serious trouble.

### Q7: Is there a connection to the hierarchy problem?

The hierarchy problem in the Standard Model involves the Higgs mass receiving quadratically divergent self-energy corrections. Under SCN, Higgs self-energy is nullified (it's self-containing: the Higgs propagator correction uses internal Higgs propagators). This would naturally protect the Higgs mass from radiative corrections.

**If SCN could be made to work for QED/QCD**, its extension to the electroweak sector might address the hierarchy problem — one of the biggest open problems in particle physics.

### Q8: What about anomalies?

Quantum anomalies (chiral anomaly, trace anomaly) arise from loop diagrams. The chiral anomaly comes from the triangle diagram $\gamma \to \gamma\gamma$ (with a fermion loop). This diagram is NOT self-containing under SCN (no photon propagator inside the fermion-loop correction). So the chiral anomaly survives.

**Important:** The anomaly MUST survive for the theory to be consistent (anomaly cancellation is required for gauge theories).

---

## 3. Computational Questions

### Q9: Can self-containment detection be automated?

Checking all subdiagrams of a Feynman diagram is in principle a graph isomorphism problem (NP, possibly not NP-complete). For the diagrams relevant to low-order perturbation theory (<5 loops), this is computationally tractable.

**Implementation:** The `src/diagrams.py` code implements this for up to two loops.

### Q10: Can we use existing QFT tools?

Tools like FORM, FeynCalc, FeynArts, MadGraph generate and evaluate Feynman diagrams. Can we add an SCN filter pass?

**Yes:** The filter is a post-generation step. Generate all diagrams for a process at a given order, then apply the self-containment predicate, then evaluate only the surviving diagrams. This is implementable as a plugin for existing tools.

---

## 4. Questions for Discussion (User + AI)

These are the points where your input is most valuable:

### D1: Which definition of self-containment feels most natural to you?

- **(a) Literal:** $S \in S$ (only direct membership)
- **(b) Structural:** A set contains a sub-structure isomorphic to itself
- **(c) Diagrammatic:** A Feynman diagram correcting a propagator uses that propagator type internally
- **(d) Physical-observable:** Self-containment is defined at the level of dressed propagators (Dyson equation)

Each gives slightly different results. The theory's predictions depend on this choice.

### D2: Should SCN apply to vertices as well as propagators?

If yes: vertex corrections that contain the same vertex type are also nullified. This would remove more diagrams but might over-restrict the theory.

If no: only propagator self-energy corrections are subject to SCN. This is more conservative and preserves vertex corrections like the Schwinger term.

### D3: How should we handle the QCD asymptotic freedom issue?

- **(a)** Accept that SCN modifies QCD and explore the consequences
- **(b)** Refine the self-containment criterion to preserve asymptotic freedom
- **(c)** Apply SCN only to physical observables (Resolution C)
- **(d)** Treat it as evidence that SCN is not applicable to QCD

### D4: What energy regime should the simulations focus on?

- **(a)** Low-energy QED (atomic physics scale): Lamb shift, hyperfine structure
- **(b)** Intermediate QED (MeV–GeV): $e^+e^-$ collider processes
- **(c)** High-energy QCD (GeV–TeV): jet physics, deep inelastic scattering
- **(d)** All of the above

---

## 5. Prioritized Next Steps

1. ⚡ **Calculate the Lamb shift under SCN** — Most decisive test
2. 📊 **Compute $C_2^{\text{SCN}}$** for $g-2$ — Highest precision comparison
3. 💻 **Run the simulation code** — Generate plots comparing SCN vs. standard vs. data
4. 🔧 **Explore Resolution C** for QCD — Gauge-invariant SCN
5. 📐 **Check unitarity** at one loop — Optical theorem verification
