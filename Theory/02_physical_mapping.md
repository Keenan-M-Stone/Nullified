# Physical Mapping: Sets → Particles → Diagrams

## 1. Overview

This document establishes the precise correspondence between the set-theoretic framework (with SCN) and the physical structures of quantum field theory. The mapping has three layers:

$$\text{Sets} \;\xrightarrow{\Phi_1}\; \text{Particle States} \;\xrightarrow{\Phi_2}\; \text{Feynman Diagrams} \;\xrightarrow{\text{SCN filter}}\; \text{Allowed Amplitudes}$$

---

## 2. Layer 1: Sets → Particle States ($\Phi_1$)

### 2.1 Particle States as Sets

Each particle type is represented as a set encoding its quantum numbers:

$$e^- = \{q_e,\; m_e,\; s_{1/2},\; L_e\}$$
$$\gamma = \{q_0,\; m_0,\; s_1,\; \varepsilon\}$$
$$g^a = \{q_0,\; m_0,\; s_1,\; c_a\}$$
$$q_f = \{q_f,\; m_f,\; s_{1/2},\; c_i,\; f\}$$

where:
- $q$ = electric charge
- $m$ = mass  
- $s$ = spin
- $L$ = lepton number
- $\varepsilon$ = polarization
- $c_a$ = color charge (adjoint representation for gluons, fundamental for quarks)
- $f$ = flavor

### 2.2 Multi-Particle States

A multi-particle state is a set of particle states:

$$|e^- \gamma\rangle \;\longleftrightarrow\; \{e^-, \gamma\} = \bigl\{\{q_e, m_e, s_{1/2}, L_e\},\; \{q_0, m_0, s_1, \varepsilon\}\bigr\}$$

No self-containment occurs here: particle sets don't contain other particle sets as elements (they contain quantum number labels).

### 2.3 When Does Self-Containment Arise?

Self-containment arises when we model **interactions** — specifically, when a particle's state-set is redefined to include its own radiative corrections.

**The dressed propagator:** In standard QFT, the full (dressed) electron propagator is:

$$S(p) = \frac{1}{\not{p} - m - \Sigma(p)}$$

where $\Sigma(p)$ is the self-energy, which itself depends on $S(p)$ (the Dyson equation). The dressed propagator is defined in terms of itself — it is a **fixed point** of the Dyson equation.

In set language: $S_{\text{dressed}} = f(S_{\text{dressed}})$, i.e., $S_{\text{dressed}} \in \text{Image}(f)$ where $f$ takes $S_{\text{dressed}}$ as input. This is the structural self-containment that SCN targets.

---

## 3. Layer 2: Particle States → Feynman Diagrams ($\Phi_2$)

### 3.1 Diagrams as Graphs with Set Labels

A Feynman diagram $D = (V, E, \lambda)$ where:
- $V$ = vertices (interaction points)
- $E$ = edges (propagators), each connecting two vertices
- $\lambda: E \to \mathcal{P}$ = labeling function assigning a particle-set to each edge

### 3.2 Subdiagram Structure

A **subdiagram** $D' \subseteq D$ is obtained by selecting a subset of vertices and all edges connecting them.

**1PI (One-Particle Irreducible) subdiagrams** are subdiagrams that remain connected when any single internal edge is cut. These are the building blocks of radiative corrections.

### 3.3 Self-Containment in Diagrams — Formal Definition

**Definition:** Let $D$ be a Feynman diagram. Let $e \in E$ be an internal edge (propagator) with particle label $\lambda(e) = P$. A subdiagram $D' \subseteq D$ is a **self-containment** of edge $e$ if:

1. $D'$ is 1PI  
2. $D'$ is a radiative correction to $e$: removing $D'$ from $D$ and replacing it with a single edge yields a valid diagram
3. $D'$ has external legs whose quantum numbers match $P$
4. $D'$ contains an internal edge $e'$ with $\lambda(e') = P$ (same particle type as the edge being corrected)

Condition 4 is the key — the correction to a propagator of type $P$ *internally uses* a propagator of type $P$. This is the set-theoretic self-containment: the definition of $P$'s propagator references $P$'s propagator.

**Analogous definition for vertices:** A 1PI subdiagram correcting a vertex $v$ is self-containing if it internally contains a vertex of the same type as $v$ in a radiatively nested fashion.

### 3.4 Classification: Which Standard Diagrams Are Self-Containing?

#### QED One-Loop Diagrams

| Diagram | Description | Self-Containing? | Reason |
|---------|-------------|-------------------|--------|
| Electron self-energy | $e \to e\gamma \to e$ | **YES** | Corrects electron propagator; contains internal electron propagator |
| Vacuum polarization | $\gamma \to e\bar{e} \to \gamma$ | **NO** | Corrects photon propagator; contains fermion loop, not photon |
| Vertex correction | Triangle diagram | **NO** | Corrects QED vertex; contains no internal vertex correction |

#### QCD One-Loop Diagrams  

| Diagram | Description | Self-Containing? | Reason |
|---------|-------------|-------------------|--------|
| Quark self-energy | $q \to qg \to q$ | **YES** | Corrects quark propagator; contains internal quark propagator |
| Gluon self-energy (quark loop) | $g \to q\bar{q} \to g$ | **NO** | Corrects gluon propagator; internal loop is quarks |
| Gluon self-energy (gluon loop) | $g \to gg \to g$ | **YES** | Corrects gluon propagator; contains internal gluon propagator |
| Gluon self-energy (ghost loop) | $g \to c\bar{c} \to g$ | **NO** | Corrects gluon propagator; internal loop is ghosts |
| Triple-gluon vertex correction | Various topologies | **Case-by-case** | Depends on whether internal gluon lines form a nested correction |

---

## 4. Layer 3: SCN Filter → Allowed Amplitudes

### 4.1 The Filtering Algorithm

Given a set of Feynman diagrams contributing to a process at a given order:

```
FUNCTION SCN_FILTER(diagrams):
    allowed = []
    FOR EACH diagram D in diagrams:
        IF NOT has_self_containment(D):
            allowed.append(D)
    RETURN allowed
```

```
FUNCTION has_self_containment(D):
    FOR EACH internal edge e in D:
        FOR EACH 1PI subdiagram D' correcting e:
            IF D' contains an internal edge of the same particle type as e:
                RETURN TRUE
    FOR EACH vertex v in D:
        FOR EACH 1PI subdiagram D' correcting v:
            IF D' contains an internal instance of the same vertex type:
                RETURN TRUE
    RETURN FALSE
```

### 4.2 Amplitude Computation

For an allowed diagram $D$, the amplitude is computed using standard Feynman rules — SCN only acts as a **filter**, not as a modification of the rules themselves.

$$\mathcal{M}_{\text{SCN}} = \sum_{D \in \text{allowed}} \mathcal{M}(D)$$

---

## 5. The Set-Theoretic Cycle

The full logical flow:

1. **Particle types** ↔ sets of quantum numbers (no self-containment)  
2. **Interactions** ↔ set operations at vertices (no self-containment at tree level)  
3. **Loop corrections** ↔ nested set constructions (self-containment possible)  
4. **SCN filter** ↔ nullify self-containing constructions  
5. **Observables** ↔ computed from surviving amplitudes  

The physical content of SCN is concentrated at step 4: it provides a **selection rule** for radiative corrections, eliminating those with a self-referential structure.

---

## 6. Well-Definedness

**Theorem (SCN is well-defined on Feynman diagrams):**  
The self-containment predicate is decidable for any finite Feynman diagram.

*Proof sketch:* A Feynman diagram is a finite labeled graph. Enumerating all 1PI subdiagrams is finite. Checking edge/vertex label matching is a finite string comparison. Therefore, `has_self_containment` terminates in finite time for any input. $\square$

**Theorem (SCN-filtered perturbation theory is finite at each order):**  
If the number of contributing diagrams at order $n$ is finite in standard perturbation theory, then the SCN-filtered count is also finite (and ≤ the standard count).

*Proof:* SCN only removes diagrams; it doesn't add any. $\square$

**Open question (MOOT):** Does the SCN-filtered perturbation series converge better than the standard (asymptotic) series? By removing self-referential diagrams — which contribute the fastest-growing factorial terms — the growth rate may be reduced.

> **Post-falsification note:** Physical SCN has been falsified at ≥415σ by the 2-loop electron $g-2$ (`scn_c2_investigation.ipynb`). This convergence question is therefore moot — the SCN-filtered series is the wrong series.
