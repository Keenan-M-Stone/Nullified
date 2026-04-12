# 01 — Mathematical Foundations of Graded Self-Containment Nullification

**Abstract.** We extend the Self-Containment Nullification (SCN) framework [08] from a binary self-referentiality predicate $\sigma: A \to \{0, 1\}$ to a *graded* predicate $\sigma: A \to \mathbb{N}$, measuring the *depth* of self-reference. The binary theory is recovered as the special case of threshold $k = 1$. The principal new results are: (1) the additive propagation rule $\sigma(xy) = \sigma(x) + \sigma(y)$ induces a multiplicative filtration $A = F_0 \supseteq F_1 \supseteq F_2 \supseteq \cdots$ whose associated graded ring recovers standard constructions in commutative algebra; (2) the threshold operator $\mathcal{N}_k$ is idempotent for every $k$, giving a family of projections parametrized by cutoff depth; (3) the *attenuation operator* $\mathcal{N}_\lambda(x) = \lambda^{-\sigma(x)} x$ provides a continuous alternative to hard cutoff, with a flow equation connecting different attenuation scales; (4) the algebraic structure of graded SCN connects directly to I-adic completions, p-adic valuations, and universe-level hierarchies in type theory.

**Relation to prior work.** This paper builds on the binary SCN framework developed in [08, Theory/08_mathematical_foundations.md]. All theorems in [08] are recovered at $k = 1$. The motivation for this extension — and the reasons it was selected over other alternatives (min-propagation, fuzzy $\sigma$, etc.) — is documented in [Expansions/Motivation_of_Expansions.md].

**Note on originality.** The algebraic structures developed here — filtered algebras, associated graded rings, truncated polynomial rings, valuations — are well-established in commutative algebra (Bourbaki, Atiyah-Macdonald, Eisenbud) and differential geometry (Ehresmann, Weil, Kock). The jet algebra $\mathbb{F}[\varepsilon]/(\varepsilon^k)$, the $I$-adic filtration, the $p$-adic valuation, and the associated graded construction are all standard. What this paper contributes is not new algebra but a new *interpretive framework*: viewing these constructions through the lens of *graded self-referentiality depth* originating from a set-theoretic axiom about self-membership. The synthesis — connecting self-reference, valuations, jets, and type-theoretic universe levels under a single conceptual umbrella — and the proposed applications (depth-weighted diagram filtering, predicativity bounds) are the novel contribution.

---

## Part I: Graded SCN Framework

### 1. The Graded Axiom

**Axiom 1G (Graded Self-Containment Nullification).** *For any set $S$ equipped with a self-reference depth $d(S) \in \mathbb{N}$: if $d(S) \geq k$ for a chosen threshold $k \geq 1$, then $S = \emptyset$.*

$$\forall S: d(S) \geq k \implies S = \emptyset$$

**Remark 1.1.** When $k = 1$, this reduces to standard SCN: any self-reference at all triggers collapse. When $k > 1$, shallow self-reference is tolerated — only reference chains of depth $\geq k$ are unstable. This parametrizes a family of theories interpolating between "all self-reference is fatal" ($k = 1$) and "all self-reference is permitted" ($k = \infty$, recovering AFA-like behavior).

**Remark 1.2.** The depth $d(S)$ counts levels of self-referential nesting. Informally: $d(S) = 0$ means $S$ is not self-referential; $d(S) = 1$ means $S$ references itself directly; $d(S) = 2$ means $S$ references a structure that itself is self-referential; and so on. This is an externally assigned label on structures, not a derived property of bare sets.

### 2. Graded Tagged Algebras

**Definition 2.1 (Graded tagged algebra).** A *graded tagged algebra* is a pair $(A, \sigma)$ where $A$ is an algebra over a field $\mathbb{F}$ and $\sigma: A \to \mathbb{N}$ is a *graded self-referentiality function* satisfying:

- (G0) $\sigma(0_A) = 0$ (the zero element has no self-reference)
- (G1) $\sigma(a) = 0$ for all $a \in A_{\text{safe}}$ (safe elements have depth zero)

**Remark 2.2.** In [08], $\sigma: A \to \{0,1\}$ and (G0)–(G1) reduce to Assumptions A2–A3 of that paper. The graded version adds no new constraints at depth 0 — it extends only by allowing finer classification of the self-referential sector.

**Definition 2.3 (Threshold SCN operator).** For threshold $k \geq 1$, the *threshold SCN operator* $\mathcal{N}_k: A \to A$ is:

$$\mathcal{N}_k(x) = \begin{cases} 0_A & \text{if } \sigma(x) \geq k \\ x & \text{if } \sigma(x) < k \end{cases}$$

**Remark 2.4.** $\mathcal{N}_1$ is exactly the binary SCN operator $\mathcal{N}$ of [08, Definition 2.2]. The family $\{\mathcal{N}_k\}_{k \geq 1}$ forms a nested sequence of projections with $\operatorname{im} \mathcal{N}_1 \subseteq \operatorname{im} \mathcal{N}_2 \subseteq \cdots \subseteq A$: higher thresholds retain more structure.

### 3. Properties of the Threshold Operator

**Theorem 3.1 (Idempotency at every threshold).** *For all $k \geq 1$: $\mathcal{N}_k^2 = \mathcal{N}_k$.*

*Proof.* If $\sigma(x) < k$: $\mathcal{N}_k(x) = x$, so $\mathcal{N}_k(\mathcal{N}_k(x)) = \mathcal{N}_k(x) = x$. If $\sigma(x) \geq k$: $\mathcal{N}_k(x) = 0_A$, and $\sigma(0_A) = 0 < k$ by (G0), so $\mathcal{N}_k(0_A) = 0_A$. $\square$

**Corollary 3.2 (Monotonicity).** *If $j \leq k$, then $\mathcal{N}_j \circ \mathcal{N}_k = \mathcal{N}_j$ and $\operatorname{im} \mathcal{N}_j \subseteq \operatorname{im} \mathcal{N}_k$.*

*Proof.* If $\sigma(x) \geq k \geq j$, then $\mathcal{N}_k(x) = 0_A$ and $\mathcal{N}_j(0_A) = 0_A = \mathcal{N}_j(x)$. If $j \leq \sigma(x) < k$, then $\mathcal{N}_k(x) = x$ and $\mathcal{N}_j(x) = 0_A = \mathcal{N}_j(\mathcal{N}_k(x))$. If $\sigma(x) < j \leq k$, then both operators fix $x$. $\square$

**Remark 3.3.** This means the family $\{\mathcal{N}_k\}$ forms a *projective system*. The map $k \mapsto \mathcal{N}_k$ is monotone increasing in the lattice of projections on $A$ (ordered by image inclusion). The inverse limit $\varprojlim \mathcal{N}_k$ recovers the full algebra $A$ — increasingly permissive thresholds converge to the identity.

### 4. Additive Propagation and Filtrations

**Assumption G-A1 (Additive propagation).** *For a product of elements:*

$$\sigma(xy) = \sigma(x) + \sigma(y)$$

**Remark 4.1.** This is the key departure from [08]. Under binary $\sigma$, additive propagation reduces to max-propagation (since $\min(1, 0+1) = 1 = \max(0,1)$). Under graded $\sigma$, it is genuinely different: the depth of a product equals the *sum* of the depths of its factors. Products of shallowly self-referential elements become deeply self-referential. This corresponds to the intuition that composing two self-referential processes compounds the self-reference.

**Remark 4.2 (Alternatives).** Other propagation rules for graded $\sigma$:

| Rule | Definition | Character |
|------|-----------|-----------|
| **Additive** (adopted here) | $\sigma(xy) = \sigma(x) + \sigma(y)$ | Depth accumulates through composition |
| **Max** (from [08]) | $\sigma(xy) = \max(\sigma(x), \sigma(y))$ | Depth saturates; no accumulation |
| **Min** | $\sigma(xy) = \min(\sigma(x), \sigma(y))$ | Only shallow-shallow products are shallow |
| **Submultiplicative** | $\sigma(xy) \leq \sigma(x) + \sigma(y)$ | Weaker; allows partial cancellation |

Additive propagation is the natural choice for *counting*-type depths (loop counts, recursion depths, nesting levels). Max-propagation is natural for *tainting*-type depths (any contact with self-reference propagates it fully).

**Definition 4.3 (Depth filtration).** Under additive propagation, define the *depth-$k$ subspace*:

$$F_k = \{x \in A : \sigma(x) \geq k\} \cup \{0_A\}$$

(We include $0_A$ in every $F_k$ since $\sigma(0_A) = 0$ and $F_k$ must be closed under the zero element for algebraic structure.)

**Theorem 4.4 (Filtration structure).** *Under additive propagation, $\{F_k\}_{k \geq 0}$ is a descending multiplicative filtration of $A$:*

*(a)* $A = F_0 \supseteq F_1 \supseteq F_2 \supseteq \cdots$

*(b)* $F_j \cdot F_k \subseteq F_{j+k}$  (multiplicative compatibility)

*(c)* $\bigcap_{k=0}^\infty F_k = \{0_A\}$ (separation, if $\sigma$ is bounded on nonzero elements) or the set of elements with $\sigma = \infty$ (which is empty for $\sigma: A \to \mathbb{N}$).

*Proof.*
- (a): $\sigma(x) \geq k+1 \implies \sigma(x) \geq k$, so $F_{k+1} \subseteq F_k$. $F_0 = A$ since $\sigma(x) \geq 0$ for all $x$.
- (b): If $x \in F_j$ and $y \in F_k$, then $\sigma(x) \geq j$ and $\sigma(y) \geq k$, so $\sigma(xy) = \sigma(x) + \sigma(y) \geq j + k$, hence $xy \in F_{j+k}$.
- (c): If $x \in \bigcap_k F_k$, then $\sigma(x) \geq k$ for all $k \in \mathbb{N}$, which is impossible for $\sigma: A \to \mathbb{N}$ unless $x = 0_A$. $\square$

**Assumption G-A5 (Additive closure within levels).** *If $\sigma(x) = \sigma(y) = n$, then $\sigma(x + y) = n$.*

**Remark 4.5.** This is the graded analogue of [08, Assumption A5]. It ensures each $F_k$ is closed under addition (hence a subspace), which is required for the quotient and associated graded constructions below. Together with (G0), it implies $\sigma(\alpha x) = \sigma(x)$ for $\alpha \in \mathbb{F} \setminus \{0\}$ (scalar multiplication does not change depth).

**Remark 4.6 (Ultrametric alternative).** A weaker alternative to G-A5 is the *ultrametric inequality*: $\sigma(x + y) \geq \min(\sigma(x), \sigma(y))$. This preserves the filtration structure — each $F_k$ remains closed under addition — but allows sums of equal-depth elements to be *deeper* than their summands (e.g., $v_3(3 + 6) = v_3(9) = 2 > 1 = v_3(3) = v_3(6)$ in the $p$-adic case). G-A5 is strictly stronger: it forces $\sigma(x+y) = n$ when $\sigma(x) = \sigma(y) = n$, forbidding depth increase; the ultrametric permits it. Note: G-A5 does not constrain sums of *different-depth* elements. For full filtration closure one also needs $\sigma(x + y) \geq \min(\sigma(x), \sigma(y))$ when $\sigma(x) \neq \sigma(y)$, which is provided by the ultrametric but not by G-A5 alone. In properly graded algebras (where every element decomposes uniquely into homogeneous components) this issue does not arise.

### 5. Associated Graded Ring

**Definition 5.1.** The *associated graded ring* of the depth filtration is:

$$\operatorname{gr}(A) = \bigoplus_{k=0}^{\infty} F_k / F_{k+1}$$

The $k$-th component $\operatorname{gr}_k(A) = F_k / F_{k+1}$ consists of elements of *exact* depth $k$ (modulo those of depth $\geq k+1$).

**Theorem 5.2 (Graded ring structure).** *Under additive propagation and Assumption G-A5, $\operatorname{gr}(A)$ is a graded ring with multiplication:*

$$\operatorname{gr}_j(A) \times \operatorname{gr}_k(A) \to \operatorname{gr}_{j+k}(A)$$

*induced by $[x]_j \cdot [y]_k = [xy]_{j+k}$ where $[x]_j$ denotes the class of $x$ in $F_j / F_{j+1}$.*

*Proof.* Well-definedness: if $x' = x + f$ with $f \in F_{j+1}$ and $y' = y + g$ with $g \in F_{k+1}$, then $x'y' = xy + xg + fy + fg$. Since $\sigma(xg) \geq \sigma(x) + \sigma(g) \geq j + (k+1) = j + k + 1$, we have $xg \in F_{j+k+1}$. Similarly $fy \in F_{j+k+1}$ and $fg \in F_{j+k+2} \subseteq F_{j+k+1}$. So $x'y' \equiv xy \pmod{F_{j+k+1}}$. $\square$

**Remark 5.3.** This is a standard construction in commutative algebra. If $I$ is an ideal of a ring $R$ and $F_k = I^k$, the associated graded ring $\operatorname{gr}_I(R) = \bigoplus_k I^k / I^{k+1}$ controls the local geometry of $\operatorname{Spec}(R)$ near $V(I)$. The SCN version applies it to the *self-referentiality ideal* rather than an algebraic ideal — the filtration is defined by a predicate ($\sigma$) rather than by powers of a fixed ideal.

**Corollary 5.4 (Connection to I-adic filtration).** *If we define $I = F_1 = \{x : \sigma(x) \geq 1\}$, then under additive propagation $F_k \supseteq I^k$ (since products of $k$ elements from $F_1$ have $\sigma \geq k$). If equality holds — i.e., every element of depth $\geq k$ is a sum of products of $k$ elements of depth $\geq 1$ — then $F_k = I^k$ exactly and $\operatorname{gr}(A) = \operatorname{gr}_I(A)$ is the standard $I$-adic associated graded ring.*

### 6. The Threshold Operator on the Filtration

**Theorem 6.1 (Threshold-filtration correspondence).** *Suppose $A$ admits a direct-sum decomposition into homogeneous components: $A \cong \bigoplus_{n=0}^{\infty} A_n$ where $A_n = \{x \in A : \sigma(x) = n\}$ and every element has a unique expression $x = \sum_n a_n$ with $a_n \in A_n$. Then the threshold operator $\mathcal{N}_k$ acts as truncation:*

$$\mathcal{N}_k\left(\sum_{n=0}^{\infty} a_n\right) = \sum_{n=0}^{k-1} a_n$$

*and $\operatorname{im} \mathcal{N}_k \cong A / F_k$.*

*Proof.* Each $a_n$ has $\sigma(a_n) = n$, and $\mathcal{N}_k$ retains $a_n$ iff $n < k$. The isomorphism $\operatorname{im} \mathcal{N}_k \cong A/F_k$ follows because the sequence $0 \to F_k \to A \to A/F_k \to 0$ splits via the projection $x \mapsto \sum_{n < k} a_n$. $\square$

**Remark 6.1a.** The direct-sum hypothesis is essential. It holds for graded algebras (polynomial rings, formal power series) but fails for many filtered algebras — e.g., $\mathbb{Z}$ under $v_p$ does NOT decompose as $\bigoplus_n \{x : v_p(x) = n\}$ because these sets are not subgroups (they are not closed under addition). In such cases, $\mathcal{N}_k$ is still a well-defined element-wise operator, but it is NOT the same as the quotient map $A \to A/F_k$.

**Remark 6.2.** This makes the family $\{\mathcal{N}_k\}$ into a *truncation system* on the graded ring. The analogy to power series is exact: if $A = \mathbb{F}[[x]]$ (formal power series) with $\sigma(x^n) = n$, then $\mathcal{N}_k$ truncates to polynomials of degree $< k$. This is the Taylor polynomial projection — idempotent, non-linear on the full ring, and parametrized by a cutoff order.

**Corollary 6.3 (Graded decomposition at threshold $k$).** *Under the hypotheses of Theorem 6.1 (direct-sum decomposition), for each $k$:*

$$A = \underbrace{\bigoplus_{n=0}^{k-1} A_n}_{\operatorname{im} \mathcal{N}_k} \oplus \underbrace{\bigoplus_{n=k}^{\infty} A_n}_{\ker \mathcal{N}_k = F_k}$$

*This generalizes the binary decomposition $A = A_{\text{safe}} \oplus A_{\text{self-ref}}$ from [08, Theorem 3.3], which is the $k = 1$ case.*

### 7. Conditional Multiplicativity at Threshold $k$

**Theorem 7.1 (Multiplicativity conditions for $\mathcal{N}_k$).** *The threshold operator $\mathcal{N}_k$ satisfies $\mathcal{N}_k(xy) = \mathcal{N}_k(x) \mathcal{N}_k(y)$ if and only if:*

$$\sigma(x) < k \text{ and } \sigma(y) < k \implies \sigma(xy) < k$$

*Under additive propagation, this holds when $\sigma(x) + \sigma(y) < k$, but fails when $\sigma(x) + \sigma(y) \geq k$ with both $\sigma(x), \sigma(y) < k$.*

*Proof.* Suppose $\sigma(x) = j < k$ and $\sigma(y) = \ell < k$. Then $\mathcal{N}_k(x) = x$ and $\mathcal{N}_k(y) = y$, so $\mathcal{N}_k(x)\mathcal{N}_k(y) = xy$. But $\sigma(xy) = j + \ell$, which may be $\geq k$ even though $j, \ell < k$. In that case $\mathcal{N}_k(xy) = 0 \neq xy$. $\square$

**Remark 7.2.** This is a fundamental difference from binary SCN, where $\mathcal{N}$ is multiplicative under max-propagation ([08, Theorem 2.3b]). In graded SCN with additive propagation, $\mathcal{N}_k$ is multiplicative *only on elements whose combined depth stays below threshold*. Multiplicativity fails precisely at the "boundary" where shallow elements compose to cross the threshold. This is structurally analogous to how Taylor polynomial truncation is not multiplicative: $(1 + x)(1 + x) = 1 + 2x + x^2$, but truncating each factor at degree 1 and multiplying gives $1 + 2x$, while truncating the product at degree 1 gives $1 + 2x$ — but truncating at degree 1 means $x^2$ is lost, and $\mathcal{N}_2((1+x)(1+x)) = 1 + 2x$ while $\mathcal{N}_2(1+x) \cdot \mathcal{N}_2(1+x) = 1 + 2x + x^2$ since both factors survive $\mathcal{N}_2$.

**Correction:** More carefully — $\mathcal{N}_k$ acts on depth, not polynomial degree, so the right analogy requires specifying $\sigma$. The point stands: multiplicativity of $\mathcal{N}_k$ is restricted to the sub-semigroup $\{x : \sigma(x) < k/2\}$ under additive propagation (so that any pairwise product stays below $k$). On this domain, $\mathcal{N}_k$ is a multiplicative projection.

**Proposition 7.3 (Multiplicative domain).** *Let $S_{k} = \{x \in A : \sigma(x) < \lceil k/2 \rceil\}$. Then $\mathcal{N}_k$ restricted to products within $S_k$ is multiplicative: for $x, y \in S_k$, $\mathcal{N}_k(xy) = \mathcal{N}_k(x)\mathcal{N}_k(y) = xy$.*

*Proof.* If $\sigma(x), \sigma(y) < \lceil k/2 \rceil$, then $\sigma(xy) = \sigma(x) + \sigma(y) < 2\lceil k/2 \rceil \leq k + 1$, so $\sigma(xy) \leq k$. For strict inequality: $\sigma(x) + \sigma(y) \leq 2(\lceil k/2 \rceil - 1) \leq k - 1 < k$ when $k \geq 2$. (For $k = 1$: $S_1 = \{x : \sigma(x) = 0\} = A_{\text{safe}}$, recovering [08].) $\square$

### 8. The Attenuation Operator

**Definition 8.1 (Attenuation operator).** For $\lambda > 1$, the *attenuation operator* $\mathcal{N}_\lambda: A \to A$ is:

$$\mathcal{N}_\lambda(x) = \lambda^{-\sigma(x)} x$$

This suppresses elements continuously by their self-reference depth: safe elements ($\sigma = 0$) pass through unchanged, while deeply self-referential elements are exponentially attenuated.

**Theorem 8.2 (Properties of $\mathcal{N}_\lambda$).**

*(a) $\mathcal{N}_\lambda$ is NOT idempotent (in general):* $\mathcal{N}_\lambda^2(x) = \lambda^{-\sigma(\lambda^{-\sigma(x)} x)} \lambda^{-\sigma(x)} x$.

If $\sigma$ is insensitive to scalar multiplication — i.e., $\sigma(\alpha x) = \sigma(x)$ for $\alpha \in \mathbb{F} \setminus \{0\}$ (which follows from G-A5) — then:

$$\mathcal{N}_\lambda^2(x) = \lambda^{-2\sigma(x)} x \neq \lambda^{-\sigma(x)} x$$

So $\mathcal{N}_\lambda$ is not idempotent. Instead, $\mathcal{N}_\lambda^n(x) = \lambda^{-n\sigma(x)} x$.

*(b) Multiplicativity under additive propagation:*

$$\mathcal{N}_\lambda(xy) = \lambda^{-\sigma(xy)} xy = \lambda^{-(\sigma(x) + \sigma(y))} xy = (\lambda^{-\sigma(x)} x)(\lambda^{-\sigma(y)} y) = \mathcal{N}_\lambda(x) \mathcal{N}_\lambda(y)$$

*$\mathcal{N}_\lambda$ is a multiplicative (hence ring) homomorphism.* $\square$

*(c) Limit behavior:*

$$\lim_{\lambda \to \infty} \mathcal{N}_\lambda(x) = \begin{cases} x & \text{if } \sigma(x) = 0 \\ 0 & \text{if } \sigma(x) \geq 1 \end{cases} = \mathcal{N}_1(x)$$

*The hard threshold operator $\mathcal{N}_1$ is the $\lambda \to \infty$ limit of the attenuation operator.*

**Remark 8.3.** The loss of idempotency is the price of continuity. However, the attenuation operator gains full multiplicativity — something the threshold operator has only conditionally. This is a trade-off: $\mathcal{N}_k$ is idempotent but not multiplicative; $\mathcal{N}_\lambda$ is multiplicative but not idempotent.

**Remark 8.4.** The iterated application $\mathcal{N}_\lambda^n(x) = \lambda^{-n\sigma(x)} x$ gives a *discrete flow* on $A$: each application further suppresses self-referential elements by a factor of $\lambda^{-\sigma(x)}$. For $\sigma(x) = 0$, the element is a fixed point. For $\sigma(x) \geq 1$, the element flows to zero exponentially. This is a contraction mapping on $A_{\text{self-ref}}$.

### 9. Flow Equation and Renormalization Structure

**Definition 9.1 (Scale parameter).** Write $t = \ln \lambda$, so $\mathcal{N}_\lambda(x) = e^{-t\sigma(x)} x$. Define the *flow* $x(t) = \mathcal{N}_{e^t}(x) = e^{-t\sigma(x)} x$.

**Theorem 9.2 (SCN flow equation).** *The flow satisfies:*

$$\frac{dx(t)}{dt} = -\sigma(x) \cdot x(t)$$

*This is a first-order linear ODE with solution $x(t) = x(0) e^{-\sigma(x) t}$.*

*Proof.* Direct differentiation: $\frac{d}{dt} e^{-t\sigma(x)} x = -\sigma(x) e^{-t\sigma(x)} x = -\sigma(x) \cdot x(t)$. $\square$

**Remark 9.3 (Connection to RG equations).** The flow equation $\frac{dx}{dt} = -\sigma(x) x$ has the structure of a *renormalization group equation* with an anomalous dimension equal to $\sigma(x)$. In the RG framework, the anomalous dimension $\gamma$ controls how an operator scales under RG flow: $\mathcal{O}(\mu) \sim \mu^{-\gamma} \mathcal{O}(\mu_0)$. Here, self-reference depth $\sigma$ plays the role of $\gamma$, and the SCN flow parameter $t$ plays the role of $\ln(\mu/\mu_0)$. Safe elements ($\sigma = 0$) are marginal (scale-invariant); self-referential elements are irrelevant (flow to zero). See §16 for further discussion of this analogy.

**Theorem 9.4 (Semi-group property).** *The attenuation operators form a one-parameter semi-group:*

$$\mathcal{N}_{\lambda_1} \circ \mathcal{N}_{\lambda_2} = \mathcal{N}_{\lambda_1 \lambda_2}$$

*equivalently, in the flow parameter: $x(t_1 + t_2) = \mathcal{N}_{e^{t_1}}(x(t_2))$.*

*Proof.* $\mathcal{N}_{\lambda_1}(\mathcal{N}_{\lambda_2}(x)) = \lambda_1^{-\sigma(\lambda_2^{-\sigma(x)} x)} \lambda_2^{-\sigma(x)} x = \lambda_1^{-\sigma(x)} \lambda_2^{-\sigma(x)} x = (\lambda_1 \lambda_2)^{-\sigma(x)} x$, using $\sigma(\alpha x) = \sigma(x)$ for scalar $\alpha$. $\square$

### 10. Graded SCN Cohomology

**Theorem 10.1 (Graded exact sequence).** *For each threshold $k$, there is a split short exact sequence:*

$$0 \to F_k \xrightarrow{\iota} A \xrightarrow{\mathcal{N}_k} A / F_k \to 0$$

*where $\iota$ is inclusion. This is the $k$-th level of a tower of exact sequences connected by the filtration maps $F_{k+1} \hookrightarrow F_k$.*

*Proof.* Same argument as [08, Theorem 5.1] — $\mathcal{N}_k$ is an idempotent projection, so the sequence splits. $\square$

**Theorem 10.2 (Long exact sequence of the filtration).** *The successive quotients $F_k / F_{k+1} = \operatorname{gr}_k(A)$ fit into short exact sequences:*

$$0 \to F_{k+1} \to F_k \to \operatorname{gr}_k(A) \to 0$$

*These assemble into an exact couple, and the associated spectral sequence has $E_1^{p,q}$-page determined by the graded components $\operatorname{gr}_p(A)$.*

**Remark 10.3.** The spectral sequence machinery is available but may be more structure than needed for initial applications. The key practical content is that each threshold level $k$ adds exactly one graded component $\operatorname{gr}_{k-1}(A)$ to the surviving algebra: $\operatorname{im} \mathcal{N}_k = \operatorname{im} \mathcal{N}_{k-1} \oplus \operatorname{gr}_{k-1}(A)$.

### 11. Nilpotency and Polynomial Truncation

**Theorem 11.1 (Stratified nilpotency).** *Under additive propagation, a product of $m$ elements from $F_1$ (the self-referential ideal) lies in $F_m$:*

$$\underbrace{F_1 \cdot F_1 \cdots F_1}_{m \text{ factors}} \subseteq F_m$$

*Consequently, $\mathcal{N}_k$ annihilates all products of $\geq k$ self-referential elements.*

*Proof.* If $x_1, \ldots, x_m \in F_1$, then $\sigma(x_i) \geq 1$ for each $i$, so $\sigma(x_1 \cdots x_m) = \sum_i \sigma(x_i) \geq m$. Hence $x_1 \cdots x_m \in F_m$, and $\mathcal{N}_k(x_1 \cdots x_m) = 0$ when $m \geq k$. $\square$

**Corollary 11.2 (Generalized dual numbers).** *For a single generator $\varepsilon$ with $\sigma(\varepsilon) = 1$, the image of $\mathcal{N}_k$ restricted to the subalgebra generated by $A_{\text{safe}}$ and $\varepsilon$ is:*

$$\operatorname{im} \mathcal{N}_k \cong \mathbb{F}[\varepsilon] / (\varepsilon^k)$$

*When $k = 1$: $\mathbb{F}[\varepsilon] / (\varepsilon) \cong \mathbb{F}$ (binary SCN — self-referential generator is killed). When $k = 2$: $\mathbb{F}[\varepsilon] / (\varepsilon^2)$ (dual numbers — recovers [08, Corollary 3.4]). When $k = 3$: $\mathbb{F}[\varepsilon] / (\varepsilon^3)$ (2-jets). General $k$: the algebra of $(k-1)$-jets.*

**Remark 11.3.** This is the central structural result of graded SCN. The threshold $k$ determines how many levels of "infinitesimal" self-reference survive:

| $k$ | Surviving algebra | Classical name | Application |
|-----|------------------|----------------|-------------|
| 1 | $\mathbb{F}$ | Scalars | Binary SCN (total collapse) |
| 2 | $\mathbb{F}[\varepsilon]/(\varepsilon^2)$ | Dual numbers | Automatic differentiation (1st derivative) |
| 3 | $\mathbb{F}[\varepsilon]/(\varepsilon^3)$ | 2-jets | 2nd-order Taylor (curvature) |
| $k$ | $\mathbb{F}[\varepsilon]/(\varepsilon^k)$ | $(k-1)$-jets | $(k-1)$-th order Taylor expansion |
| $\infty$ | $\mathbb{F}[[\varepsilon]]$ | Formal power series | No truncation (AFA-like) |

**Remark 11.4.** The jet space connection gives graded SCN immediate application to differential geometry: the $k$-jet bundle $J^k(M)$ parametrizes Taylor approximations of functions on a manifold $M$ up to order $k$. The SCN threshold $k$ becomes the jet order. The SCN operator $\mathcal{N}_k$ becomes the jet projection $j^{k-1}: C^\infty(M) \to J^{k-1}(M)$.

### 12. Graded SCN Calculus

**Theorem 12.1 (Taylor expansion to order $k-1$).** *For $f: A \to A$ smooth and $x = a + \varepsilon$ with $a \in A_{\text{safe}}$, $\sigma(\varepsilon) = 1$:*

$$\mathcal{N}_k(f(a + \varepsilon)) = \sum_{n=0}^{k-1} \frac{f^{(n)}(a)}{n!} \varepsilon^n$$

*This is exact in the image of $\mathcal{N}_k$ (not an approximation — $\varepsilon^k = 0$ in $\operatorname{im} \mathcal{N}_k$).*

*Proof.* Taylor expand: $f(a + \varepsilon) = \sum_{n=0}^{\infty} \frac{f^{(n)}(a)}{n!} \varepsilon^n$. Since $\sigma(\varepsilon^n) = n\sigma(\varepsilon) = n$ under additive propagation, $\mathcal{N}_k$ retains terms with $n < k$ and annihilates terms with $n \geq k$. $\square$

**Corollary 12.2.** *Graded SCN calculus provides exact derivatives up to order $k - 1$. At $k = 2$, this is automatic differentiation (first derivative only, recovering [08, Theorem 6.1]). At $k = 3$, it provides both first and second derivatives. At general $k$, it provides derivatives $f'(a), f''(a), \ldots, f^{(k-1)}(a)$ simultaneously.*

**Theorem 12.3 (Graded integration).** *Define the graded SCN integral extracting the depth-$n$ coefficient:*

$$\int_{\text{SCN}}^{(n)} f \, d\varepsilon^n = \text{coefficient of } \varepsilon^n \text{ in } \mathcal{N}_k(f), \qquad 0 \leq n < k$$

*This satisfies $\int_{\text{SCN}}^{(n)} \varepsilon^m \, d\varepsilon^n = \delta_{mn}$.*

**Remark 12.4.** The system of graded integrals $\{\int^{(0)}, \int^{(1)}, \ldots, \int^{(k-1)}\}$ extracts all surviving Taylor coefficients simultaneously. This is the algebraic content of the jet projection.

---

## Part II: Connections and Applications

### 13. Connection to $p$-adic Valuation

**Proposition 13.1.** *Let $R = \mathbb{Z}$ and define $\sigma(n) = v_p(n)$ (the $p$-adic valuation — the exponent of $p$ in the prime factorization of $n$, with $v_p(0) = \infty$ conventionally; we set $\sigma(0) = 0$ to satisfy (G0)). Then:*

*(a) Additive propagation holds for multiplication: $v_p(nm) = v_p(n) + v_p(m)$.*

*(b) The filtration $F_k = \{n : v_p(n) \geq k\} = p^k \mathbb{Z}$ is the standard $p$-adic filtration.*

*(c) The associated graded ring is $\operatorname{gr}_{p}(\mathbb{Z}) \cong \mathbb{F}_p[t]$ (polynomial ring over the field with $p$ elements).*

*(d) The threshold operator $\mathcal{N}_k$ acts as an element-wise filter: $\mathcal{N}_k(n) = n$ if $v_p(n) < k$, and $\mathcal{N}_k(n) = 0$ if $v_p(n) \geq k$. This kills all multiples of $p^k$ and preserves the rest. Note that this is NOT the same as reduction mod $p^k$ — e.g., $\mathcal{N}_2(15) = 15$ at $p = 3$ (since $v_3(15) = 1 < 2$), but $15 \bmod 9 = 6$. The quotient map $\mathbb{Z} \to \mathbb{Z}/p^k\mathbb{Z}$ is the genuine $p$-adic truncation; $\mathcal{N}_k$ is a cruder operation that does not decompose elements by their $p$-adic digits.*

*(e) The $p$-adic completion $\mathbb{Z}_p = \varprojlim \mathbb{Z}/p^k\mathbb{Z}$ is the inverse limit of the quotient system — NOT of $\mathcal{N}_k$, since $\operatorname{im} \mathcal{N}_k \not\cong \mathbb{Z}/p^k\mathbb{Z}$ (see (d) and Remark 6.1a).*

**Remark 13.2.** The $p$-adic valuation is an instance of the additive propagation and filtration structure (parts (a)–(c)), but NOT a full instance of the graded tagged algebra framework. Critically, Assumption G-A5 *fails*: $v_3(3) = 1$ and $v_3(6) = 1$, but $v_3(3 + 6) = v_3(9) = 2 \neq 1$. The $p$-adic valuation satisfies the *ultrametric inequality* $v_p(x + y) \geq \min(v_p(x), v_p(y))$ (Remark 4.6) — sums can have *higher* depth, not equal depth. This means the direct-sum decomposition required by Theorem 6.1 fails for $\mathbb{Z}$ under $v_p$: the sets $\{n : v_p(n) = k\}$ are not closed under addition. The $p$-adic example is instructive for the multiplicative structure but requires the ultrametric variant (Remark 4.6) rather than G-A5 for additive structure.

**Corollary 13.3 (SCN attenuation as $p$-free part).** *The attenuation operator with $\lambda = p$ gives $\mathcal{N}_p(n) = p^{-v_p(n)} n = n / p^{v_p(n)}$, which strips all factors of $p$ from $n$ (the "$p$-free part"). E.g., $\mathcal{N}_3(18) = 3^{-2} \cdot 18 = 2$, $\mathcal{N}_3(7) = 7$, $\mathcal{N}_3(27) = 1$.*

### 14. Connection to Universe Levels in Type Theory

**Proposition 14.1 (Universe hierarchy as graded SCN).** *In a dependent type theory with a universe hierarchy $\mathcal{U}_0 : \mathcal{U}_1 : \mathcal{U}_2 : \cdots$, define $\sigma(T) = $ the universe level of type $T$. Then:*

*(a) $\sigma(\mathcal{U}_n) = n + 1$ (each universe lives one level above its contents).*

*(b) Product types satisfy $\sigma(\Pi_{x:A} B(x)) = \max(\sigma(A), \sup_x \sigma(B(x)))$ — this is max-propagation, not additive.*

*(c) The threshold operator $\mathcal{N}_k$ restricts to types in universes $< k$, producing a *cumulative universe fragment*.*

**Remark 14.2.** Universe levels use max-propagation, not additive. This is because a function type's self-referentiality is determined by its most complex component, not the sum. However, some type-theoretic constructions *do* use additive propagation: the *universe polymorphism level* in Coq-style systems adds levels when quantifying over universes.

**Remark 14.3.** The graded SCN threshold $k$ corresponds to a *predicativity bound*: types at level $< k$ are "predicatively safe," and types at level $\geq k$ are "impredicatively dangerous" (in the Russellian sense of self-referential definitions). Graded SCN formalizes the informal notion of "controlled impredicativity" used in proof assistants.

### 15. Connection to Recursion Depth Bounding

**Proposition 15.1.** *Let $f$ be a recursive function. Define $\sigma(f^{(n)}) = n$ where $f^{(n)}$ denotes $f$ with call stack depth $n$. Then:*

*(a) Under a model where composition increments depth, $\sigma(g \circ f) = \sigma(g) + \sigma(f)$. (This is a modeling choice, not a provable fact about execution — real stack depth depends on the execution model.)*

*(b) The threshold operator $\mathcal{N}_k$ truncates recursion at depth $k$: $\mathcal{N}_k(f^{(n)}) = 0$ for $n \geq k$. This is bounded recursion / stack depth limiting.*

*(c) The attenuation operator $\mathcal{N}_\lambda(f^{(n)}) = \lambda^{-n} f^{(n)}$ gives exponentially decaying weight to deeper recursive calls. This is a form of *discounted recursion*.*

**Remark 15.2.** Discounted recursion (part (c)) connects to:
- **Memoization with decay:** Cache entries from deep recursive calls are given lower priority.
- **Iterative deepening:** Run computation to depth $k$, then $k+1$, etc. — this is the sequence $\mathcal{N}_1, \mathcal{N}_2, \mathcal{N}_3, \ldots$
- **Value iteration in reinforcement learning:** Future rewards are discounted by $\gamma^n$ where $\gamma < 1$ and $n$ is the time horizon. This is $\mathcal{N}_\lambda$ with $\lambda = 1/\gamma$.

### 16. Connection to Renormalization (Supplementary)

**Remark 16.1 (Structural analogy).** In perturbative QFT, the renormalization group (RG) flow describes how coupling constants change with energy scale $\mu$:

$$\mu \frac{dg}{d\mu} = \beta(g)$$

The SCN flow equation (Theorem 9.2) $\frac{dx}{dt} = -\sigma(x) x$ has the same structure with $\beta(x) = -\sigma(x) x$ — a *linear* beta function. Real QFT beta functions are nonlinear (they depend on $g$ itself), which is what makes RG flow rich. The SCN version is a linearized, exactly solvable analogue.

**Remark 16.2 (Why binary SCN failed and graded SCN may not).** Binary SCN ($k = 1$) kills *all* self-energy insertions — this is the skeleton expansion, falsified at $\geq 415\sigma$ for the 2-loop electron $g-2$ [see Theory/scn_c2_investigation.ipynb]. The problem is that binary SCN is too aggressive: it treats $\sigma = 1$ (one self-energy insertion) the same as $\sigma = 100$ (deeply nested self-reference). Graded SCN at threshold $k > 1$ would retain self-energy insertions up to depth $k - 1$. The question of whether any finite $k > 1$ can match experimental data is open — it requires computation, not proof. The attenuation operator $\mathcal{N}_\lambda$ with finite $\lambda$ offers a third possibility: all self-energy diagrams contribute, but with exponentially suppressed weight at higher depth.

> **Status:** These are structural observations, not claims. Whether graded SCN produces viable physics at any $k$ or $\lambda$ is an empirical question that would require computing $g-2$ with depth-weighted diagrams and comparing to experiment.

---

## Part III: Formal Structure

### 17. Category of Graded Tagged Algebras

**Definition 17.1.** The category **GradSCN** has:
- **Objects:** Graded tagged algebras $(A, \sigma)$ satisfying (G0)–(G1).
- **Morphisms:** Algebra homomorphisms $\phi: A \to B$ that preserve depth: $\sigma_B(\phi(x)) = \sigma_A(x)$.

**Proposition 17.2.** *The threshold operators $\mathcal{N}_k$ are natural transformations: for any depth-preserving morphism $\phi$, $\phi \circ \mathcal{N}_k^A = \mathcal{N}_k^B \circ \phi$.*

*Proof.* $\phi(\mathcal{N}_k^A(x)) = \phi(x)$ if $\sigma_A(x) < k$ (since $\phi$ preserves depth, $\sigma_B(\phi(x)) = \sigma_A(x) < k$, so $\mathcal{N}_k^B(\phi(x)) = \phi(x)$). If $\sigma_A(x) \geq k$: $\phi(0_A) = 0_B = \mathcal{N}_k^B(\phi(x))$ since $\sigma_B(\phi(x)) \geq k$. $\square$

**Proposition 17.3 (Completion functor).** *The assignment $(A, \sigma) \mapsto \hat{A} = \varprojlim_{k} A / F_k$ defines a functor from **GradSCN** to complete filtered algebras. If $A$ is already complete with respect to the depth filtration, this is the identity.*

### 18. Summary and Open Directions

**What graded SCN provides beyond [08]:**

1. A parametrized family of idempotent projections $\{\mathcal{N}_k\}_{k \geq 1}$, recovering binary SCN at $k = 1$.
2. A natural filtration $F_0 \supseteq F_1 \supseteq \cdots$ with an associated graded ring, connecting self-reference to standard commutative algebra.
3. Stratified nilpotency: $\varepsilon^k = 0$ at threshold $k$, recovering the full hierarchy of jet algebras $\mathbb{F}[\varepsilon]/(\varepsilon^k)$.
4. The attenuation operator $\mathcal{N}_\lambda$: a multiplicative (but non-idempotent) alternative with continuous suppression and a semi-group flow structure.
5. An explicit flow equation $\dot{x} = -\sigma(x) x$ connecting SCN to renormalization group structure.
6. Concrete instances: $p$-adic valuation (§13), universe levels (§14), recursion depth (§15).

**What remains open:**

| Question | Notes |
|----------|-------|
| Does graded SCN at some $k > 1$ or $\lambda$ match experimental QFT data? | Requires computation — see §16.2 |
| What is the "right" propagation rule for additive $\sigma$ under sums? | G-A5 (strict) vs. ultrametric (§4.6) — application-dependent |
| Spectral sequence applications | §10 — the machinery is available but unexplored |
| Non-commutative graded SCN | All results assume $A$ is commutative or $\sigma$ respects non-commutativity |
| Connection to operadic structure | Self-referential compositions have a natural operad structure |
| Categorical semantics of bounded self-reference | §14 — relating graded SCN to predicativity in type theory |

**Most promising computational directions:**

1. **Jet algebra applications:** Implement graded SCN at $k = 3, 4, 5$ for automatic higher-order differentiation. Compare to existing AD frameworks.
2. **Depth-weighted QFT:** Compute $g-2$ with diagrams weighted by $\lambda^{-\sigma}$ and fit $\lambda$ to experiment. Determine if a single $\lambda$ can fit multi-loop data.
3. **Recursion analysis:** Apply graded SCN to program analysis — bound recursion depth, compute resource consumption via the attenuation operator.

---

## References

1. Aczel, P. (1988). *Non-Well-Founded Sets*. CSLI Lecture Notes.
2. Atiyah, M. & Macdonald, I. (1969). *Introduction to Commutative Algebra*. Ch. 10 (Completions).
3. Eisenbud, D. (1995). *Commutative Algebra with a View Toward Algebraic Geometry*. GTM 150, Springer. Ch. 5 (Filtrations and the Artin-Rees Lemma).
4. Kock, A. (2006). *Synthetic Differential Geometry*. 2nd ed. (Jet bundles via nilpotent infinitesimals.)
5. Kolář, I., Michor, P. & Slovák, J. (1993). *Natural Operations in Differential Geometry*. (Jet bundles.)
6. Robert, A. (2000). *A Course in p-adic Analysis*. Springer. (p-adic filtrations.)
7. Univalent Foundations Program. (2013). *Homotopy Type Theory*. (Universe levels.)
8. [08] Theory/08_mathematical_foundations.md — Binary SCN mathematical foundations.
9. [Motivation] Expansions/Motivation_of_Expansions.md — Motivation for graded extension.
