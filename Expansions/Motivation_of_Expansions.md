# Expansions from the initial mathematical foundation

We've determined that SCN, predicated on the assumptions we've made thusly, doesn't have any real application
aside from being a novel approach to constructing a Set Theoretic framework. Of those things, hitherto not
strongly considered, we ask "What is most likely to have a broader impact"?

## Proposition

**A2 — graded self-referentiality ($\sigma: A \to \mathbb{N}$)** — and it's not close.

### The Case

**It generalizes rather than breaks.**  
Binary $\sigma$ is the special case $k = 1$ of the threshold version $\mathcal{N}(x) = 0$ if $\sigma(x) \geq k$.  
Every theorem in the paper survives as a $k = 1$ limit.  
The other alternatives (min-propagation, dropping A5, fuzzy $\sigma$) all *break* core results —
you lose multiplicativity, ideal structure, or idempotency respectively.  
Graded $\sigma$ preserves everything and adds a new parameter.

**It addresses exactly why Physical SCN failed.**  
Binary SCN kills all self-energy insertions uniformly — that's the skeleton expansion, and it's too aggressive (falsified at 415$\sigma$).  
A graded version could attenuate by depth: $\mathcal{N}(x) = \lambda^{-\sigma(x)} x$ suppresses deeper self-reference progressively rather
than killing it outright.  
That's structurally closer to what renormalization *actually does* —
it doesn't delete self-energy diagrams, it absorbs them into running couplings order by order.  
You could think of $\sigma(x) = n$ as "this element involves $n$ levels of self-reference," and the attenuation version as a controlled flow.

**Sum-capped propagation becomes non-trivial.**  
For binary $\sigma$, the sum-capped rule $\sigma(xy) = \min(1, \sigma(x) + \sigma(y))$ is equivalent to max.  
For graded $\sigma$, $\sigma(xy) = \sigma(x) + \sigma(y)$ is genuinely different — it tracks *accumulated* depth.  
Products of shallowly self-referential elements become deeply self-referential.  
This gives you a filtration on the algebra:
$A = F_0 \supseteq F_1 \supseteq F_2 \supseteq \cdots$ where $F_k = \{x : \sigma(x) \geq k\}$.  
That's a standard construction in algebra (I-adic filtration), and the associated graded ring
$\operatorname{gr}(A) = \bigoplus_k F_k / F_{k+1}$ is well-studied.

**It has immediate CS applications.**

Recursion depth tracking is already fundamental:

- Universe levels in dependent type theory (Agda, Coq) are exactly graded self-reference — `Type₀ : Type₁ : Type₂ : ...`
- Static analysis uses call-depth bounds for termination proofs
- Memoization can be framed as "cache results at self-reference depth $\leq k$"

### The Others

**The others are less fertile:**

- A1 min-propagation is a specific rule within the binary framework — it's a parameter choice, not a framework expansion.  
  Niche use: situations where mixing a self-referential element with a safe one "cures" the self-reference.
- A2 fuzzy ($\sigma \in [0,1]$) is interesting conceptually, but losing idempotency is devastating —  
  one-step termination is arguably SCN's most distinctive property.
- A3, A4, A5 alternatives all break the theory in ways that make it weaker without opening new directions.

### In Short

If I were picking one thing from this paper to develop further, it would be:  

- graded SCN with additive propagation $\sigma(xy) = \sigma(x) + \sigma(y)$
- threshold operator $\mathcal{N}_k$
- the resulting filtration/associated-graded structure

That's where the existing mathematics is deepest and the application surface is widest.

---

## What this framework can and cannot deliver

After developing [01_graded_scn_foundations.md](01_graded_scn_foundations.md) and auditing it for originality and correctness, we need to be honest about what applying this framework to existing mathematics would and would not achieve.

### What it provides

**A discovery heuristic across domains.** The framework asks a uniform set of questions of any algebraic structure: *Does it carry a depth function σ? Which propagation rule? Does G-A5 hold or only the ultrametric? What's the threshold operator? The attenuation?* Answering these for different domains surfaces structural parallels:

| Domain | σ | Propagation | G-A5? | $\mathcal{N}_k$ | $\mathcal{N}_\lambda$ |
|--------|---|-------------|-------|------------------|----------------------|
| Formal power series | degree | additive | yes | Taylor truncation | — |
| $p$-adic integers | $v_p$ | additive | **no** (ultrametric) | kills multiples of $p^k$ | $p$-free part |
| Type theory | universe level | max | yes | universe fragment | — |
| Perturbation theory | loop order | additive | yes | $k$-th order approx | soft regularization |
| Recursive programs | call depth | additive (modeled) | yes | bounded recursion | discounted recursion |

When two rows share the same column structure, theorems proved in one domain may have shadows in the other.

**The idempotent/multiplicative tradeoff as a design principle.** The paper surfaces a clean structural fact: $\mathcal{N}_k$ is idempotent but not multiplicative; $\mathcal{N}_\lambda$ is multiplicative but not idempotent. This tradeoff recurs under different names — rounding vs. scaling, hard clipping vs. soft compression, restriction to a fragment vs. probabilistic weighting, hard cutoff vs. analytic regularization. The framework gives it a precise algebraic characterization. Recognizing it as a single phenomenon suggests that any domain with one of these operators should have a natural partner.

**The G-A5/ultrametric classification.** This is a genuine fault line. The $p$-adic valuation satisfies the ultrametric but violates G-A5 ($v_3(3+6) = 2 \neq 1$). The classification determines whether the direct-sum decomposition exists (Theorem 6.1 of [01]), whether $\mathcal{N}_k$ coincides with the quotient map, and which theorems apply. Any filtered algebra can be classified by this, telling you immediately what transfers and what doesn't.

**$\mathcal{N}_\lambda$ as a potentially underexplored tool.** Hard truncation ($\mathcal{N}_k$) is ubiquitous — Taylor polynomials, perturbative expansions, bounded-depth analysis. The attenuation operator $\mathcal{N}_\lambda(x) = \lambda^{-\sigma(x)}x$ is less standard as a named construction: it keeps all terms but exponentially suppresses deep ones, and it's *exactly multiplicative*. This opens a two-dimensional approximation space $(k, \lambda)$ — hard threshold and soft attenuation — with algebraic guarantees.

### What it does NOT provide

- **New theorems about existing objects.** The filtration, associated graded ring, jet algebras, completions — all known. The framework proves nothing new about $\mathbb{F}[\varepsilon]/(\varepsilon^k)$ or $\mathbb{Z}_p$.
- **Computational advantage.** No faster algorithms. The operators are conceptual, not computational innovations.
- **Resolution of open problems.** It is an organizational framework, not a proof technique.

### Bottom line

The framework is a **lens**, not a microscope. Its value will come from suggesting new questions ("this system has a filtration — does it have a natural attenuation operator?"), porting intuitions across domains (same propagation rule + same G-A5 status = same theorems apply), and parametrizing approximation via the $(k, \lambda)$ pair.

---

## Primary target: perturbation theory

The most promising concrete application — and the one most likely to produce a result that can't be obtained without the framework — is applying $\mathcal{N}_\lambda$ to perturbative QFT.

### Why this target

1. **Binary SCN already engages with this domain.** The skeleton expansion (binary SCN applied to Feynman diagrams) was falsified at $\geq 415\sigma$ for electron $g-2$ at 2-loop. We know exactly where and why it fails: it kills all self-energy insertions uniformly. Graded SCN with depth-weighted diagrams is the natural next step.

2. **The domain has additive propagation with G-A5.** Loop order in Feynman diagrams satisfies $\sigma(\text{diagram}_1 \cdot \text{diagram}_2) = \sigma(\text{diagram}_1) + \sigma(\text{diagram}_2)$ and sums of same-loop-order diagrams stay at that loop order. This is the best-behaved case for the framework — all theorems apply.

3. **There is a clear experimental benchmark.** The anomalous magnetic moment $g-2$ of the electron is known to extraordinary precision. Any proposed weighting scheme either matches experiment or doesn't. No ambiguity about success criteria.

4. **$\mathcal{N}_\lambda$ offers something genuinely different from existing methods.** Standard approaches either truncate at fixed loop order (= $\mathcal{N}_k$), or use resummation (Borel, Padé) to handle the divergent tail. The attenuation operator $\mathcal{N}_\lambda$ is neither: it keeps all diagrams but weights them by $\lambda^{-\text{loops}}$, and it preserves multiplicative structure exactly. This is not the same as Borel summation, and could be complementary.

### What success would look like

- Compute $g-2$ with diagrams weighted by $\lambda^{-\sigma}$ (where $\sigma$ = loop order).
- Fit $\lambda$ to the known experimental value.
- Test whether a *single* $\lambda$ can simultaneously fit multi-loop data — i.e., whether the weighting scheme is consistent across orders, not just a one-parameter curve fit to one number.
- If it works: this would demonstrate that depth-weighted perturbation theory is a viable approximation method with a principled algebraic foundation.
- If it doesn't: we learn something about why hard truncation is the only viable option and can close the book cleanly.

### What this requires

1. Published QED loop coefficients for $g-2$ (these exist in the literature through 5-loop, computed by Aoyama, Kinoshita, Nio et al.).
2. Implementation of $\lambda$-weighted summation — straightforward numerics.
3. Comparison to experiment and to standard truncation.

This is a *computational* question, not a *proof* question. We either fit the data or we don't.
