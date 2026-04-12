# 08 — Mathematical Foundations of Self-Containment Nullification

**Abstract.** We introduce a set-theoretic axiom — *Self-Containment Nullification* (SCN) — which occupies a position between the Axiom of Foundation (which forbids self-membership) and Aczel's Anti-Foundation Axiom (which permits it). SCN allows self-membership as a formal possibility but declares it dynamically unstable: any set satisfying $S \in S$ collapses to $\emptyset$. We develop the algebraic consequences systematically. The principal results are: (1) SCN induces an idempotent, nonlinear projection operator $\mathcal{N}$ on any algebraic structure equipped with a self-referentiality predicate; (2) the image of $\mathcal{N}$ decomposes any such structure into a *safe* component and a *nilpotent* component, recovering familiar constructions (dual numbers, Grassmann algebras) from a single axiom; (3) fixed-point equations under $\mathcal{N}$ terminate in one step, providing a canonical regularization of self-referential recursions. We identify the modeling assumptions — particularly the *propagation rule* governing how self-referentiality interacts with algebraic operations — that are required beyond the axiom itself, and catalog the alternative theories that arise from different choices (Appendix A). Applications to quantum field theory are discussed in a supplementary section.

---

## Part I: The SCN Framework

### 1. The Axiom

**Axiom 1 (Self-Containment Nullification).** *For any set $S$: if $S \in S$, then $S = \emptyset$.*

$$\forall S: S \in S \implies S = \emptyset$$

**Remark 1.1.** This occupies a third position between Foundation ($\lnot \exists S: S \in S$) and AFA ($\exists S: S \in S$ is consistent, and such sets are non-trivial). Under SCN, self-membership is *permitted* as a formal predicate but *dynamically unstable* — it triggers collapse.

**Remark 1.2.** The collapse $S \to \emptyset$ can be read as a structural assertion: self-referential objects have trivial content. Computationally, a self-referential expression that "calls itself" and is required to be well-defined must reduce to the empty structure.

### 2. The SCN Operator on Algebras

**Definition 2.1 (Tagged algebra).** A *tagged algebra* is a pair $(A, \sigma)$ where $A$ is an algebra over a field $\mathbb{F}$ and $\sigma: A \to \{0, 1\}$ is a *self-referentiality predicate*:
- $\sigma(x) = 1$: element $x$ is *self-referential* (participates in its own definition)
- $\sigma(x) = 0$: element $x$ is *safe* (no self-reference)

**Definition 2.2 (SCN operator).** The *SCN operator* $\mathcal{N}: A \to A$ is defined by:

$$\mathcal{N}(x) = \begin{cases} 0_A & \text{if } \sigma(x) = 1 \\ x & \text{if } \sigma(x) = 0 \end{cases}$$

This is the algebraic translation of Axiom 1: self-referential elements are sent to zero.

**Theorem 2.3 (Basic properties of $\mathcal{N}$).**

*(a) Idempotency:* $\mathcal{N}^2 = \mathcal{N}$.

*Proof.* If $\sigma(x) = 0$: $\mathcal{N}(\mathcal{N}(x)) = \mathcal{N}(x) = x$. If $\sigma(x) = 1$: $\mathcal{N}(\mathcal{N}(x)) = \mathcal{N}(0_A) = 0_A$ (since $\sigma(0_A) = 0$, as the zero element is not self-referential). $\square$

*(b) Conditional multiplicativity:* $\mathcal{N}(xy) = \mathcal{N}(x)\mathcal{N}(y)$ **if and only if** we adopt the *max-propagation rule* $\sigma(xy) = \max(\sigma(x), \sigma(y))$.

*Proof.* ($\Leftarrow$) Assume max-propagation. Case analysis:
- $\sigma(x) = \sigma(y) = 0$: $\sigma(xy) = 0$, so $\mathcal{N}(xy) = xy = \mathcal{N}(x)\mathcal{N}(y)$. ✓
- $\sigma(x) = 1, \sigma(y) = 0$: $\sigma(xy) = 1$, so $\mathcal{N}(xy) = 0 = 0 \cdot y = \mathcal{N}(x)\mathcal{N}(y)$. ✓
- $\sigma(x) = 0, \sigma(y) = 1$: symmetric. ✓
- $\sigma(x) = \sigma(y) = 1$: $\sigma(xy) = 1$, so $\mathcal{N}(xy) = 0 = 0 \cdot 0 = \mathcal{N}(x)\mathcal{N}(y)$. ✓

($\Rightarrow$) Now suppose multiplicativity holds but max-propagation fails. Then there exist $x, y$ with $\sigma(x) = 1, \sigma(y) = 0$ but $\sigma(xy) = 0$. Then $\mathcal{N}(xy) = xy \neq 0$ (generically), but $\mathcal{N}(x)\mathcal{N}(y) = 0 \cdot y = 0$. Contradiction. $\square$

*(c) Non-linearity:* $\mathcal{N}(\alpha x + \beta y) \neq \alpha \mathcal{N}(x) + \beta \mathcal{N}(y)$ in general.

*Proof.* Let $\sigma(x) = 1, \sigma(y) = 0$, and $\sigma(x + y) = 0$. Then $\mathcal{N}(x + y) = x + y$, but $\mathcal{N}(x) + \mathcal{N}(y) = 0 + y = y \neq x + y$. $\square$

**Remark 2.4.** Idempotency follows from the axiom alone. Multiplicativity requires an additional assumption about how $\sigma$ propagates through products. Non-linearity is a general feature: $\mathcal{N}$ acts differently on elements depending on a predicate, not on their algebraic value.

**Remark 2.5 (The propagation rule is a modeling choice).** The max-propagation rule $\sigma(xy) = \max(\sigma(x), \sigma(y))$ is not a consequence of Axiom 1 — it is a separate assumption about how self-referentiality interacts with the algebra's multiplication. Different propagation rules yield different theories (see Appendix A for a systematic comparison). Results in this paper that depend on max-propagation are explicitly marked.

### 3. Decomposition Theorem

**Proposition 3.1.** *Under max-propagation, the set $A_{\text{self-ref}} = \{x \in A : \sigma(x) = 1\}$ is a two-sided ideal of $A$.*

*Proof.* If $\sigma(\varepsilon) = 1$ and $a \in A$, then $\sigma(a\varepsilon) = \max(\sigma(a), 1) = 1$ and similarly $\sigma(\varepsilon a) = 1$. Additive closure: if $\sigma(\varepsilon_1) = \sigma(\varepsilon_2) = 1$ and we assume $\sigma(\varepsilon_1 + \varepsilon_2) = 1$ (Assumption A5 — see Appendix A), then $A_{\text{self-ref}}$ is closed under addition. $\square$

**Proposition 3.2.** *$A_{\text{safe}} = \{x \in A : \sigma(x) = 0\}$ is a subalgebra of $A$, and $A_{\text{self-ref}}$ is nilpotent: $\varepsilon_1 \varepsilon_2 = 0$ for any $\varepsilon_1, \varepsilon_2 \in A_{\text{self-ref}}$ after applying $\mathcal{N}$.*

*Proof.* Safe subalgebra: if $\sigma(a) = \sigma(b) = 0$, then $\sigma(ab) = \max(0,0) = 0$ under max-propagation. Nilpotency: $\mathcal{N}(\varepsilon_1 \varepsilon_2) = 0$ since $\sigma(\varepsilon_1 \varepsilon_2) = 1$. In the image of $\mathcal{N}$, all self-referential products vanish. $\square$

**Theorem 3.3 (SCN Decomposition).** *Let $(A, \sigma)$ be a tagged algebra under max-propagation. Then:*

$$A = A_{\text{safe}} \oplus A_{\text{self-ref}}$$

*where $A_{\text{safe}} = \operatorname{im} \mathcal{N}$ (a subalgebra) and $A_{\text{self-ref}} = \ker \mathcal{N}$ (a nilpotent ideal).*

**Corollary 3.4 (Dual number isomorphism).** *For a single self-referential generator $\varepsilon$ with $\sigma(\varepsilon) = 1$, the algebra $A$ modulo higher self-referential terms is isomorphic to the dual numbers: $A / I^2 \cong \mathbb{F}[\varepsilon]/(\varepsilon^2)$.*

This is the algebra of dual numbers — the same structure used for automatic differentiation, infinitesimal deformations, and jet spaces. SCN derives it from a single axiom rather than postulating $\varepsilon^2 = 0$.

### 4. Fixed Points and Termination

**Theorem 4.1 (One-step termination).** *Let $T: A \to A$ be an operator such that $T(x) = f(x) + g(x, T(x))$ where $g$ involves self-reference (the output $T(x)$ appears in the input). Under SCN, the resolution terminates in one step:*

$$\mathcal{N}(T(x)) = f(x) + g_{\text{safe}}(x)$$

*where $g_{\text{safe}}$ contains only non-self-referential contributions of $g$.*

*Proof.* Since $T(x)$ appears in its own definition, the feedback term $g(x, T(x))$ contains self-referential components. $\mathcal{N}$ projects these to zero in one application. Since $\mathcal{N}^2 = \mathcal{N}$ (Theorem 2.3a), no further applications change the result. $\square$

**Theorem 4.2 (Fixed-point uniqueness).** *Under SCN, every self-referential fixed-point equation has a unique resolution: the SCN-projected version. There is no iterative convergence — the resolution is algebraic, not analytic.*

*Proof.* The idempotency $\mathcal{N}^2 = \mathcal{N}$ means a single application of $\mathcal{N}$ reaches the fixed point. Unlike iterative schemes (Picard iteration, Newton's method), there is no sequence $x_0, x_1, x_2, \ldots$ converging to a limit. The fixed point is $\mathcal{N}(T(x))$, computed in one step. $\square$

**Example 4.3 (Recursive computation).** Consider a function defined by $f(x) = x + g(f(x))$ where $g$ feeds the output back into the input. This is a self-referential fixed point. Under SCN, the resolution is $\mathcal{N}(f(x)) = x + g(x)$ — the self-referential feedback term is eliminated in one step.

**Remark 4.4 (Application to QFT).** In quantum field theory, the Dyson equation $G = G_0 + G_0 \Sigma G$ has exactly this structure — see Supplementary §S1 for details. The mathematical theorem stands independently of the physical application.

**Example 4.5 (Recursive sequence).** Consider $a_n = f(a_{n-1})$ where $f$ involves self-reference at depth $\geq n_0$. Under SCN, all terms with depth $\geq n_0$ are nullified, truncating the recursion to a finite sum. This is a structural cutoff rather than an order-based one.

### 5. SCN Cohomology

**Theorem 5.1 (Exact sequence).** *The SCN operator induces a short exact sequence:*

$$0 \to \ker \mathcal{N} \xrightarrow{\iota} A \xrightarrow{\mathcal{N}} \operatorname{im} \mathcal{N} \to 0$$

*where $\iota$ is the inclusion map.*

*Proof.* Exactness at each position:
- At $\ker \mathcal{N}$: $\iota$ is injective (inclusion). ✓
- At $A$: $\ker(\mathcal{N}) = \operatorname{im}(\iota)$ by definition. ✓
- At $\operatorname{im} \mathcal{N}$: $\mathcal{N}$ is surjective onto its image. The sequence splits because $\mathcal{N}$ is idempotent — $\operatorname{im} \mathcal{N}$ is a direct summand. ✓ $\square$

**Theorem 5.2 (SCN cohomology).** *Define $H^0_{\text{SCN}}(A) = \ker \mathcal{N} = A_{\text{self-ref}}$ and $H^1_{\text{SCN}}(A) = A / \operatorname{im} \mathcal{N}$. Since the sequence splits, $H^1_{\text{SCN}}(A) \cong \ker \mathcal{N}$. The SCN cohomology is:*

$$H^*_{\text{SCN}}(A) = (A_{\text{self-ref}}, A_{\text{self-ref}})$$

*Both cohomology groups are isomorphic to the self-referential ideal.*

**Remark 5.3.** This short exact sequence parallels the BRST decomposition in gauge theory, where a nilpotent operator $Q$ with $Q^2 = 0$ separates physical and unphysical states (see Supplementary §S2 for the detailed analogy). The key structural difference: BRST uses a *linear* nilpotent operator and requires a cohomological quotient ($\ker Q / \operatorname{im} Q$); SCN uses a *nonlinear* idempotent projection and needs only a direct image (no quotient required, because $\mathcal{N}^2 = \mathcal{N}$).

### 6. SCN Calculus

**Theorem 6.1 (Differentiation rule).** *For a function $f: A \to A$ that is differentiable and respects the decomposition $x = a + \varepsilon$ with $a \in A_{\text{safe}}, \varepsilon \in A_{\text{self-ref}}$:*

$$\mathcal{N}(f(a + \varepsilon)) = f(a) + f'(a)\varepsilon$$

*This is exact (not an approximation) because $\varepsilon^2 = 0$ in the SCN-projected algebra.*

*Proof.* Taylor expand: $f(a + \varepsilon) = f(a) + f'(a)\varepsilon + \frac{1}{2}f''(a)\varepsilon^2 + \cdots$. Under SCN, $\varepsilon^2 = 0$, so all terms of order $\geq 2$ in $\varepsilon$ vanish exactly. $\square$

**Corollary 6.2.** *SCN calculus is equivalent to automatic differentiation via dual numbers.*

**Theorem 6.3 (Integration rule).** *Define the SCN integral of a function $f(a + \varepsilon) = f_0(a) + f_1(a)\varepsilon$ as:*

$$\int_{\text{SCN}} f(a + \varepsilon) \, d\varepsilon = f_1(a)$$

*This extracts the coefficient of $\varepsilon$ — the "self-referential component" of $f$. It is linear, satisfies $\int_{\text{SCN}} 1 \, d\varepsilon = 0$ and $\int_{\text{SCN}} \varepsilon \, d\varepsilon = 1$.*

**Remark 6.4.** The parallel $\int_{\text{SCN}} d\varepsilon = \int_{\text{Grassmann}} d\theta$ is exact for linear functions. For higher-order terms: Grassmann variables anticommute ($\theta_1 \theta_2 = -\theta_2 \theta_1$) while SCN nilpotents commute ($\varepsilon_1 \varepsilon_2 = \varepsilon_2 \varepsilon_1$). Both satisfy $\varepsilon^2 = 0$ and $\theta^2 = 0$, but with different symmetry. This is the essential distinction between SCN nilpotency and fermionic nilpotency.

### 7. Topological Invariants Under SCN

**Theorem 7.1 (Topological invariance).** *Let $X$ be a topological space and $\mathcal{N}$ act on $C^*(X)$ (the cochain complex). If $\sigma$ respects the coboundary operator ($\sigma \circ \delta = \delta \circ \sigma$ on cochains), then SCN preserves the Betti numbers: $b_n(\mathcal{N}(X)) = b_n(X)$ for all $n$.*

*Proof.* If $\sigma$ commutes with $\delta$, then $\mathcal{N}$ maps cocycles to cocycles and coboundaries to coboundaries. The induced map on cohomology $H^n(X; \mathbb{F})$ is the identity on safe classes and zero on self-referential classes. But the self-referential classes form a sub-complex, so the Euler characteristic $\chi = \sum_n (-1)^n b_n$ is preserved (alternating sum of a sub-complex is zero by acyclicity of the self-referential sector, which is contractible since $\mathcal{N}$ retracts it to zero). $\square$

**Remark 7.2.** This theorem implies that SCN cannot alter *counting invariants* of a structure — it can kill specific representatives but not the equivalence classes they belong to. Any application of SCN that claims to change the number of distinct classes (e.g., the number of independent sectors in a graded algebra) would require violating idempotency or the decomposition theorem, and is therefore inconsistent with the framework.

---

## Part II: Labeled SCN (Flavored Nullification)

### 8. Labeled SCN: Collapsing Objects with Conserved Labels

The basic SCN axiom treats all self-referential structures identically — they collapse to $\emptyset$ regardless of any other properties. In many algebraic settings, elements carry labels from a group (gradings, charges, representations), and any collapse should respect these labels. This motivates:

**Axiom 2 (Labeled SCN).** *Let $S$ be a set equipped with a label $\ell(S) \in L$ from a label group $(L, +)$. If $S \in S$, then $S \to \emptyset_\ell$, where $\emptyset_\ell$ carries label $\ell(S)$ (the label is conserved even in collapse).*

$$S \in S \implies S = \emptyset_{\ell(S)}$$

**Remark 8.1.** This changes the ontology: the zero element is no longer unique. There is a family of "labeled zeros" $\{0_\ell : \ell \in L\}$, one for each label. This is unusual from a set-theoretic perspective but standard in graded algebra — a graded ring $R = \bigoplus_g R_g$ has a zero element in each graded component. Labeled SCN makes the collapse operation grade-aware.

**Remark 8.2 (Physical motivation).** In physics, labels correspond to conserved quantum numbers (charge, color). See Supplementary §S3 for how labeled SCN interacts with gauge invariance and confinement.

### 9. Label-Conserving Collapse

**Setting.** Take $L = (\mathbb{Z}, +)$ (integer labels).

**Theorem 9.1 (Label-conserving collapse).** *Let $x$ be a self-referential element with label $\ell(x) = q \in \mathbb{Z}$. Under labeled SCN:*

$$\mathcal{N}_{\mathbb{Z}}(x) = 0_{q}$$

*The collapsed object has zero value but retains label $q$. In the graded algebra $A = \bigoplus_{q \in \mathbb{Z}} A_q$, this means the self-referential contribution vanishes within its graded component without leaking into other components.*

**Proposition 9.2 (Label conservation under $\mathcal{N}$).** *If $\sigma$ is label-blind (i.e., $\sigma$ depends only on structural properties, not on labels), then labeled SCN preserves the grading: $\mathcal{N}_L(A_q) \subseteq A_q$ for all $q \in L$.*

*Proof.* $\mathcal{N}_L(x) = 0_{\ell(x)}$ if $\sigma(x) = 1$, and $0_{\ell(x)} \in A_{\ell(x)} = A_q$. If $\sigma(x) = 0$, then $\mathcal{N}_L(x) = x \in A_q$. $\square$

**Remark 9.3.** In gauge theory, label conservation under SCN corresponds to Ward identity preservation. See Supplementary §S3.

### 10. Non-Abelian Labels Under SCN

**Setting.** Take $L = \mathrm{Rep}(G)$, the set of irreducible representations of a group $G$.

**Definition 10.1.** A *representation-labeled SCN algebra* is a tagged algebra $(A, \sigma, \rho)$ where $\rho: A \to \mathrm{Rep}(G)$ assigns a representation label to each element.

**Proposition 10.2 (Representation-graded collapse).** *Let $A$ carry a representation grading $A = \bigoplus_\rho A_\rho$. Then labeled SCN decomposes as:*

$$\mathcal{N}_L = \bigoplus_\rho \mathcal{N}_\rho$$

*where each $\mathcal{N}_\rho$ acts independently on the $\rho$-sector. Self-referential elements in each representation sector collapse independently, carrying their representation label.*

**Proposition 10.3 (Singlet constraint).** *If only elements in the trivial representation $\rho = \mathbf{1}$ can appear in certain algebraic constructions (e.g., traces, invariants), and SCN produces $0_\rho$ with $\rho \neq \mathbf{1}$, then the collapsed object is excluded from those constructions.*

**Remark 10.4.** The counting of independent collapsed objects equals the number of irreducible representations participating. For a group $G$ with adjoint representation of dimension $d$, self-referential elements in the adjoint sector produce $d$ independent labeled zeros — one per basis element of the representation.

**Remark 10.5 (Physical interpretation).** When $G = SU(3)$, the singlet constraint corresponds to color confinement. See Supplementary §S3.

### 11. Multi-Label SCN and Grading Constraints

**Definition 11.1.** A *multi-labeled SCN algebra* carries labels from a product group $L = L_1 \times L_2 \times \cdots \times L_n$.

**Theorem 11.2 (Grading preservation).** *Labeled SCN preserves the multi-grading: if $\sigma$ is label-blind, then $\mathcal{N}_L$ maps each multi-graded component $A_{(\ell_1, \ldots, \ell_n)}$ to itself.*

*Proof.* Immediate from Proposition 9.2 applied component-wise. $\square$

**Remark 11.3.** When the labels correspond to physical quantum numbers, grading preservation ensures that SCN does not create or destroy conserved quantities. See Supplementary §S3 for the connection to anomaly cancellation.

### 12. Extended Algebraic Structures

**Theorem 12.1 (Ring-theoretic properties).** *In a tagged ring $(R, \sigma)$ under max-propagation:*

*(a) $I = \{x \in R : \sigma(x) = 1\}$ is a two-sided ideal of $R$.*

*(b) The quotient $R/I \cong R_{\text{safe}}$ is the "SCN-safe" ring.*

*(c) $I^2 = 0$ in the image of $\mathcal{N}$ (nilpotent ideal of order 2).*

*Proof.*
- (a): If $\sigma(r) = 0$ and $\sigma(x) = 1$, then $\sigma(rx) = \max(0,1) = 1$ and $\sigma(xr) = 1$, so $I$ absorbs multiplication. Closure under addition by Assumption A5.
- (b): $R/I$ consists of cosets $\{a + I : a \in R_{\text{safe}}\}$, and the map $a \mapsto a + I$ is an isomorphism since $R = R_{\text{safe}} \oplus I$.
- (c): For $\varepsilon_1, \varepsilon_2 \in I$: $\mathcal{N}(\varepsilon_1 \varepsilon_2) = 0$ since $\sigma(\varepsilon_1 \varepsilon_2) = 1$. $\square$

**Remark 12.2.** The SCN quotient ring is isomorphic to $R[x]/(x^2)$ for a single generator — another path to the dual numbers, now from ring theory rather than algebra.

**Remark 12.3.** The SCN quotient ring $R / I$ represents the algebra of quantities that survive self-referential filtering. In any application where certain contributions are identified as self-referential and removed, $R_{\text{safe}}$ is the surviving algebra.

---

### 13. Summary and Open Directions

**What SCN provides (mathematically established):**

1. A novel third position between Foundation and AFA for handling set self-membership.
2. An idempotent, nonlinear projection operator $\mathcal{N}$ with well-defined algebraic properties (conditionally multiplicative under the max-propagation assumption — see Appendix A).
3. A canonical decomposition $A = A_{\text{safe}} \oplus A_{\text{self-ref}}$ with the self-referential ideal being nilpotent (connecting to dual numbers, Grassmann algebras).
4. A one-step termination for self-referential fixed-point equations.
5. An exact short sequence (SCN cohomology) with a structure analogous to BRST decomposition.
6. A labeled extension that respects grading under collapse.

**What SCN does NOT provide:**

1. A specification of $\sigma$ — the choice of what counts as "self-referential" is external to the axiom.
2. A unique propagation rule for $\sigma$ under products — the max-propagation rule (Assumption A1) is a modeling choice; alternatives exist (see Appendix A).
3. A derivation of constants — SCN constrains structure but does not predict numbers.

**Open mathematical questions:**

| Question | Status |
|----------|--------|
| Does SCN + ZF (minus Foundation) form a consistent theory? | Likely yes (SCN is weaker than Foundation; it forbids a strict subset of what Foundation forbids) |
| What is the model theory of SCN? | Open — what do models of ZF$^-$ + SCN look like? |
| Can $\sigma$ be derived from algebraic structure rather than imposed? | Partially — in graded algebras, $\sigma$ can be defined via grade (e.g., odd-grade elements) |
| Does SCN have a topos-theoretic formulation? | Open — SCN-algebras may form a category with interesting properties |
| Can SCN be composed with other selection axioms? | Open — e.g., "SCN + large cardinal axioms" or "SCN in homotopy type theory" |

**Most promising direction:** SCN is mathematically at its strongest as a **structural language** for situations where self-referential regularization is needed. The closest existing framework is **conditional expectations** in operator algebras (Tomiyama projections), but SCN's nonlinearity distinguishes it. Applications might include:
- Fixed-point regularization in dynamical systems
- Self-referential structures in computer science (type theory, recursive types)
- Category-theoretic models of self-reference with controlled collapse

---

## Appendix A: Assumptions and Alternatives

The SCN axiom (Axiom 1) and the tagged algebra definition (Definition 2.1) determine a minimal framework. Several results in this paper require **additional assumptions** that do not follow from the axiom. This appendix catalogs each assumption, identifies what depends on it, and describes the landscape of alternatives.

### A1. Max-Propagation Rule

**Assumption.** $\sigma(xy) = \max(\sigma(x), \sigma(y))$ — a product is self-referential if *either* factor is.

**Used in:** Theorem 2.3(b) (conditional multiplicativity), Corollary 3.4 (dual number isomorphism), Proposition 10.2 (representation-graded decomposition).

**Alternatives:**

| Rule | Definition | Consequence |
|------|-----------|-------------|
| **Max** (adopted here) | $\sigma(xy) = \max(\sigma(x), \sigma(y))$ | Multiplicativity: $\mathcal{N}(xy) = \mathcal{N}(x)\mathcal{N}(y)$ |
| **Min** | $\sigma(xy) = \min(\sigma(x), \sigma(y))$ | Only pure self-ref products collapse; mixed products survive. $\mathcal{N}$ is not multiplicative. |
| **Product** | $\sigma(xy) = \sigma(x)\cdot\sigma(y)$ | Equivalent to min for binary $\sigma$. |
| **Sum (capped)** | $\sigma(xy) = \min(1, \sigma(x)+\sigma(y))$ | Equivalent to max for binary $\sigma$; differs for graded $\sigma$ (see A2). |
| **Context-dependent** | $\sigma(xy) = f(\sigma(x), \sigma(y), x, y)$ | Most general; $\sigma$ propagation depends on element structure, not just $\sigma$-values. $\mathcal{N}$ loses most algebraic properties. |

**Discussion.** Max-propagation is the *unique* binary rule that makes $\mathcal{N}$ multiplicative (Theorem 2.3(b)). It is also the most conservative choice: it maximizes the set of elements classified as self-referential, and therefore the set of elements collapsed. Min-propagation would be the most permissive. Neither is "correct" in the abstract — the choice must be motivated by the application.

### A2. Binary Predicate

**Assumption.** $\sigma: A \to \{0, 1\}$ — self-referentiality is a binary property.

**Used in:** All results. The definition of $\mathcal{N}$ as a two-case operator (Definition 2.2) depends on this.

**Alternatives:**

- **Graded self-referentiality.** $\sigma: A \to \mathbb{N}$ tracking "depth" of self-reference. $\mathcal{N}$ could be defined as $\mathcal{N}(x) = 0$ if $\sigma(x) \geq k$ for some threshold $k$, or $\mathcal{N}$ could attenuate continuously: $\mathcal{N}(x) = \lambda^{-\sigma(x)} x$ for some $\lambda > 1$. This recovers something closer to a renormalization group.
- **Fuzzy self-referentiality.** $\sigma: A \to [0, 1]$ (continuous). $\mathcal{N}(x) = (1 - \sigma(x))x$. Interpolates between collapse ($\sigma = 1$) and identity ($\sigma = 0$). Idempotency fails unless $\sigma(\mathcal{N}(x)) = \sigma(x)$ or $\sigma((1-\sigma)x) = \sigma(x)$, which requires additional constraints.
- **Categorical.** $\sigma$ is a *property* in a topos, taking values in the subobject classifier $\Omega$ (which generalizes $\{0,1\}$).

### A3. Zero is Non-Self-Referential

**Assumption.** $\sigma(0_A) = 0$.

**Used in:** Theorem 2.3(a) (idempotency). If $\sigma(0_A) = 1$, then $\mathcal{N}(\mathcal{N}(\varepsilon)) = \mathcal{N}(0_A) = 0_A$ is still consistent, so idempotency holds vacuously. The real consequence: if $\sigma(0_A) = 1$, then the zero element is itself self-referential and $0_A \in \ker \mathcal{N}$ — the safe subspace would not contain zero, breaking the vector space structure of $A_{\text{safe}}$.

**Status:** Near-mandatory. Dropping this assumption collapses the algebraic framework.

### A4. Inverse Inherits Self-Referentiality

**Assumption.** $\sigma(g^{-1}) = \sigma(g)$ for invertible elements.

**Used in:** Theorem 12.1 (ring-theoretic properties).

**Alternatives:** $\sigma(g^{-1}) = 1 - \sigma(g)$ (self-referentiality flips under inversion). This would break the ideal structure of $A_{\text{self-ref}}$ and prevent ring-theoretic quotient constructions.

**Status:** Natural in any setting where $\sigma$ is defined by structural properties (graph topology, recursion depth) that are invariant under algebraic inversion.

### A5. Additive Closure of Self-Referential Elements

**Assumption.** If $\sigma(\varepsilon_1) = \sigma(\varepsilon_2) = 1$, then $\sigma(\varepsilon_1 + \varepsilon_2) = 1$.

**Used in:** Propositions 3.1–3.2 (ideal structure of $A_{\text{self-ref}}$), Theorem 5.2 (exact sequence), Theorem 12.1 (two-sided ideal).

**Alternatives:** Without additive closure, $A_{\text{self-ref}}$ is a subset but not a subspace. The decomposition $A = A_{\text{safe}} \oplus A_{\text{self-ref}}$ fails, the exact sequence does not exist, and $\ker \mathcal{N}$ is not an ideal. The operator $\mathcal{N}$ is still well-defined element-wise but loses most global algebraic properties.

**Status:** Essential for the algebraic theory. In applications, this assumption must be verified case-by-case.

### Summary of Assumption Dependencies

| Assumption | Key results that depend on it |
|------------|-------------------------------|
| A1 (max-propagation) | Multiplicativity (Thm 2.3b), dual numbers (Cor 3.4) |
| A2 (binary $\sigma$) | Two-case operator definition (Def 2.2), all subsequent results |
| A3 ($\sigma(0) = 0$) | $A_{\text{safe}}$ is a subspace, idempotency is non-trivial |
| A4 ($\sigma(g^{-1}) = \sigma(g)$) | Ring-theoretic quotient (Thm 12.1) |
| A5 (additive closure) | Ideal structure (Prop 3.1–3.2), exact sequence (Thm 5.2) |

---

## Supplementary: Applications to Quantum Field Theory

This supplementary section collects the connections between the mathematical SCN framework and quantum field theory. These applications motivated the development of the theory but are logically independent of the mathematical results in the main text.

> **Empirical status.** The most direct physical application — "Physical SCN" identifying self-referential elements with self-energy insertions — produces the skeleton expansion. This was empirically falsified at $\geq 415\sigma$ for the 2-loop electron $g-2$ anomalous magnetic moment. See `scn_c2_investigation.ipynb` for the detailed computation. The mathematical framework stands; its application to QED perturbation theory at this level fails. See the project documents `01`–`07` in this `Theory/` folder for the full investigation history.

### S1. Dyson Equation as SCN Fixed Point

The dressed propagator in QFT satisfies $G = G_0 + G_0 \Sigma G$, where $G$ appears on both sides — a self-referential fixed-point equation. Under Physical SCN, identifying self-energy insertions as self-referential, the resolution is:

$$\mathcal{N}(G) = G_0 + G_0 \Sigma_{\text{skel}} G_0$$

where $\Sigma_{\text{skel}}$ uses only skeleton (non-self-referential) self-energy diagrams. This is exactly the skeleton expansion — a well-known reorganization of perturbation theory that *does not change* physical predictions when summed to all orders (only the partial sums differ). This is the fixed-point result of Theorem 4.2 applied in a specific physical context.

### S2. BRST Analogy

The SCN exact sequence (Theorem 5.2)

$$0 \to \ker \mathcal{N} \xrightarrow{\iota} A \xrightarrow{\mathcal{N}} \operatorname{im} \mathcal{N} \to 0$$

is structurally analogous to the BRST decomposition $\mathcal{H} = \mathcal{H}_{\text{phys}} \oplus \mathcal{H}_{\text{gauge}}$ where the BRST operator $Q$ with $Q^2 = 0$ separates physical and unphysical states:

| BRST | SCN |
|------|-----|
| $Q^2 = 0$ (nilpotent) | $\varepsilon^2 \mapsto 0$ (nilpotent image) |
| $\mathcal{H}_{\text{phys}} = \ker Q / \operatorname{im} Q$ | $A_{\text{safe}} = \operatorname{im} \mathcal{N}$ |
| Unphysical states: $Q$-exact | Self-referential elements: $\ker \mathcal{N}$ |
| Gauge fixing: specifies representatives | Specifying $\sigma$: declares what is self-referential |

The key structural difference: BRST uses a *linear* nilpotent operator and requires a cohomological quotient ($\ker Q / \operatorname{im} Q$); SCN uses a *nonlinear* idempotent projection and needs only a direct image (no quotient required, because $\mathcal{N}^2 = \mathcal{N}$).

### S3. Labeled SCN and Gauge Invariance

In gauge theories, particles carry conserved quantum numbers (electric charge, color). Labeled SCN (§8) provides the mathematical framework for collapse that respects these gradings.

**Electric charge.** Taking $L = (\mathbb{Z}, +)$ with integer charges (in units of $e/3$), Theorem 9.1 ensures that a self-referential element with charge $q$ collapses to $0_q$ — the charge is conserved. Proposition 9.2 then says that if $\sigma$ is charge-blind (depends only on structural properties, not charge flow), the Ward identity $\partial_\mu J^\mu = 0$ is preserved at every order where $\mathcal{N}$ acts.

**Color.** Taking $L = \mathrm{Rep}(SU(3))$, Proposition 10.3 gives a structural articulation of confinement: if only color-singlet states can appear in certain constructions (physical observables), and SCN produces $0_\rho$ with $\rho \neq \mathbf{1}$, then the collapsed object is confined. Concretely: a gluon self-energy collapses to $0_{\mathbf{8}}$ (8 labeled zeros, one per adjoint basis element), and since $\mathbf{8} \neq \mathbf{1}$, this collapsed state cannot appear as a physical asymptotic state.

**Multi-label and anomalies.** With $L = U(1) \times SU(3)$ (or larger), Theorem 11.2 ensures multi-grading preservation. The triangle anomaly diagram ($\pi^0 \to \gamma\gamma$ and gauge anomaly cancellation) is *not* self-referential under any SCN formulation — it contains no self-energy subdiagram — so SCN does not threaten anomaly cancellation.

### S4. Generations and Topological Invariants

Remark 7.2 in the main text notes that topological invariants (Betti numbers, Euler characteristic) are SCN-invariant. In string theory, the number of fermion generations is a topological invariant of the compactification space. The $\mathbb{Z}_3$ structure of three lepton generations *could* be such an invariant — though we emphasize this is narrative, not derivation. The $\theta_0 = 2/9$ value (Brannen 2005) remains a numerical curiosity without a derivation from SCN.

---

## References

1. Aczel, P. (1988). *Non-Well-Founded Sets*. CSLI Lecture Notes.
2. Barwise, J. & Moss, L. (1996). *Vicious Circles*. CSLI Publications.
3. Brannen, C. (2006). "The Lepton Masses." (Preprint; $\theta_0 = 2/9$ first identified 2005.)
4. Grassmann, H. (1844). *Die lineale Ausdehnungslehre*.
5. Koide, Y. (1981). Lett. Nuovo Cim. **34**, 201.
6. Weinberg, S. (1995). *The Quantum Theory of Fields, Vol I.* Ch. 12.
7. Zinn-Justin, J. (2002). *Quantum Field Theory and Critical Phenomena.* Ch. 9.
8. Żenczykowski, P. (2013). Phys. Rev. D **86**, 117303. (Brannen–Rosen value.)
