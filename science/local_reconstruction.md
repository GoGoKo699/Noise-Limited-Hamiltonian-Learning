# Canonical averaging and local support reconstruction

A Pauli transfer block need not equal a Hamiltonian coefficient: dissipative terms can contribute to its antisymmetric part. In addition, restricting observations to a small region can move an exterior dissipative term into the region's effective Hamiltonian. This page resolves both effects while using preparation and measurement visibility only on the original allowed patches.

The [reciprocal estimator](estimator.md) supplies accurate estimates of each block's antisymmetric part up to the second-order noise modulus. First average all blocks to obtain a canonical local coefficient. Then remove the exterior contributions with a finite support identity. The required regions never exceed the promised locality $`k`$.

## 1. Canonical Hamiltonian projection

Consider a region $`W`$ of $`w`$ qubits, with Hilbert-space dimension $`q=2^w`$. Its canonical Pauli basis consists of Hermitian tensor products of $`I,X,Y,Z`$. Define

```math
\mathcal K_C(X)=-i[C,X],
\qquad
\langle\mathcal A,\mathcal B\rangle_{\mathrm{sop}}
=\mathrm{Tr}_{\mathrm{sop}}(\mathcal A^\dagger\mathcal B).
```

The superoperator inner product uses an orthonormal operator basis, such as $`P/\sqrt q`$. Consequently the Pauli transfer entries

```math
T_{QP}=q^{-1}\mathrm{Tr}\left[Q\mathcal L_W(P)\right]
```

are matrix entries in an orthonormal basis, and their ordinary matrix inner product equals $`\langle\cdot,\cdot\rangle_{\mathrm{sop}}`$.

**Lemma 1 — orthogonal Hamiltonian component.** For nonidentity canonical Pauli labels $`C,R,A,B`$ on $`W`$,

**(1)**

```math
\langle\mathcal K_C,\mathcal K_R\rangle_{\mathrm{sop}}
=2q^2\,\mathbf1\{C=R\},
\qquad
\langle\mathcal K_C,\mathcal D_{AB}\rangle_{\mathrm{sop}}=0.
```

**Proof.** Write $`L_A(X)=AX`$ and $`R_B(X)=XB`$. The superoperator trace identity

```math
\mathrm{Tr}_{\mathrm{sop}}(L_AR_B)
=\mathrm{Tr}(A)\mathrm{Tr}(B)
```

follows by vectorization or direct calculation in matrix units. The left-right maps obey

```math
\langle L_AR_B,L_UR_V\rangle_{\mathrm{sop}}
=\mathrm{Tr}(A^\dagger U)
\mathrm{Tr}(B^\dagger V).
```

For the sandwich term $`L_AR_B`$, both $`A`$ and $`B`$ are traceless, so its inner product with $`L_C-R_C`$ vanishes. For any matrix $`D`$,

```math
\langle\mathcal K_C,L_D+R_D\rangle_{\mathrm{sop}}=0,
```

because the two terms proportional to $`q\mathrm{Tr}(CD)`$ cancel, as do the two terms proportional to $`\mathrm{Tr}(C)\mathrm{Tr}(D)`$. Set $`D=BA`$ to handle the anticommutator in $`\mathcal D_{AB}`$. Expanding two commutators and using $`\mathrm{Tr}(CR)=q\mathbf1\{C=R\}`$ gives the first identity. $`\square`$

If $`f_W`$ is the canonical Hamiltonian coefficient of $`C`$ in $`\mathcal L_W`$, Lemma 1 therefore gives

**(2)**

```math
f_W=
\frac{\langle\mathcal K_C,\mathcal L_W\rangle_{\mathrm{sop}}}{2q^2}.
```

This uses the canonical traceless-Pauli representation. A decomposition that permits identity terms in jump operators must first combine their Hamiltonian contributions.

Exactly half of the $`4^w`$ Pauli labels anticommute with nonidentity $`C`$. Multiplication projectively by $`C`$ partitions those labels into $`q^2/4`$ unordered pairs. For each pair choose signed representatives $`P,Q`$ with $`Q=-iCP`$. The commutator has only two nonzero entries on that pair: $`2`$ from $`P`$ to $`Q`$ and $`-2`$ from $`Q`$ to $`P`$. Thus the pair contributes

```math
2T_{QP}-2T_{PQ}=8b_{PQ},
\qquad
b_{PQ}:=\frac{T_{QP}-T_{PQ}}4,
```

to the numerator of (2). We obtain the exact average

**(3)**

```math
\boxed{
f_W=\frac1{q^2/4}\sum_{\{P,Q\}}b_{PQ}.
}
```

The result is independent of which projective member is chosen first. Reversing the choice while preserving $`Q=-iCP`$ changes $`a_{PQ}`$ to $`-a_{PQ}`$ and leaves $`b_{PQ}`$ unchanged. Equation (3) cancels every canonical dissipative contribution to the Hamiltonian projection, including dissipative terms whose individual transfer blocks are antisymmetric.

## 2. What a local region actually reveals

Let $`\mathcal L`$ be the global generator and let $`W`$ contain $`S:=\mathrm{supp}(C)`$. Define the instantaneous reduced map

**(4)**

```math
\mathcal L_W(X)
=2^{-|W^c|}\mathrm{Tr}_{W^c}
\left[\mathcal L(X\otimes I_{W^c})\right].
```

For Pauli labels $`P,Q`$ supported on $`W`$,

**(5)**

```math
2^{-|W|}\mathrm{Tr}_W\left[Q\mathcal L_W(P)\right]
=2^{-N}\mathrm{Tr}\left[Q\mathcal L(P)\right].
```

Therefore the native global derivative experiments recover exactly the transfer entries used in (3). Equation (4) is a mathematical restriction of the derivative. It does not assert that the reduced finite-time evolution equals $`e^{t\mathcal L_W}`$.

To compute its Hamiltonian coefficient, factor each canonical global Pauli as $`A=A_W\otimes A_{W^c}`$. The normalized exterior trace of a dissipator vanishes unless $`A_{W^c}=B_{W^c}`$, because distinct exterior Pauli matrices are orthogonal. When the exterior labels agree, it is exactly the local expression $`\mathcal D_{A_WB_W}`$.

If both local labels are nonidentity, Lemma 1 shows that this term has no canonical Hamiltonian projection. If both are identity, it vanishes. A Hamiltonian shift can therefore arise only when one local label is identity. For a nonidentity local Pauli $`C`$,

```math
\mathcal D_{I,C}(X)=-\frac12[C,X],
\qquad
\mathcal D_{C,I}(X)=\frac12[C,X].
```

The global contributing labels must have the form $`A=V`$, $`B=CV`$, with nonidentity $`V`$ supported entirely outside $`W`$. Since $`C`$ and $`V`$ have disjoint support, $`CV`$ is their canonical positive-phase tensor product. Summing the two conjugate ordered coefficients yields

**(6)**

```math
\alpha_{V,CV}\mathcal D_{I,C}
+\alpha_{CV,V}\mathcal D_{C,I}
=-i\mathrm{Im}(\alpha_{V,CV})[C,\cdot].
```

The sign and absence of a factor two in (6) follow from the stated ordering $`(V,CV)`$ and $`\alpha_{CV,V}=\overline{\alpha_{V,CV}}`$.

A global Hamiltonian term survives the exterior trace only when it is supported inside $`W`$. Its contribution to the coefficient of $`C`$ is then exactly $`h_C`$. Combining these observations gives

**(7)**

```math
f_W=h_C+
\sum_{\substack{V\ne I\\\mathrm{supp}(V)\cap W=\varnothing}}
\mathrm{Im}(\alpha_{V,CV}),
```

where structurally forbidden coefficients are zero.

## 3. A support formula using only allowed patches

Let $`\mathsf P`$ be the known family of allowed patches, each of size at most $`k`$, with each qubit belonging to at most $`\nu`$ patches. Define the possible nonempty spectator supports

**(8)**

```math
\mathcal F_C=
\left\{
F\ne\varnothing:
F\cap S=\varnothing,
\quad
S\cup F\subseteq B\text{ for some }B\in\mathsf P
\right\}.
```

This finite family is downward closed among nonempty sets. It is determined by the allowed pattern, not by unknown coefficients. If an even sparser list of dissipative pairs is specified, one may keep the same family and set its forbidden coefficients to zero.

For $`F\in\mathcal F_C`$, let

```math
x_F=
\sum_{\mathrm{supp}(V)=F}
\mathrm{Im}(\alpha_{V,CV}).
```

For each $`E\in\mathcal F_C\cup\{\varnothing\}`$, measure the region $`W=S\cup E`$ and denote its canonical coefficient by $`f(E)`$. Equation (7) becomes

**(9)**

```math
\boxed{
f(E)=h_C+
\sum_{F\in\mathcal F_C}
x_F\,\mathbf1\{E\cap F=\varnothing\}.
}
```

Every required $`W`$ lies inside a single allowed patch and has size at most $`k`$. It is unnecessary to measure the union of different patches meeting $`S`$.

For nonempty $`F\in\mathcal F_C`$, form the finite difference

```math
d_F=\sum_{E\subseteq F}(-1)^{|E|}f(E).
```

The constant $`h_C`$ cancels. For the contribution of $`x_G`$, only subsets $`E\subseteq F\setminus G`$ remain, and their signed sum is zero unless $`F\subseteq G`$. Hence

**(10)**

```math
d_F=\sum_{\substack{G\in\mathcal F_C\\G\supseteq F}}x_G.
```

Descending support inversion recovers the individual $`x_F`$. For Hamiltonian learning, the following direct combination is sufficient:

**(11)**

```math
\boxed{
h_C=f(\varnothing)
+\sum_{F\in\mathcal F_C}(-1)^{|F|}
\sum_{E\subseteq F}(-1)^{|E|}f(E).
}
```

To verify (11), substitute (10). The coefficient of each $`x_G`$ from the double sum is

```math
\sum_{\varnothing\ne F\subseteq G}(-1)^{|F|}=-1,
```

which cancels its coefficient in $`f(\varnothing)`$. Downward closure ensures that every nonempty subset of $`G`$ occurs. This identity also covers $`\mathcal F_C=\varnothing`$, when $`h_C=f(\varnothing)`$.

## 4. The reconstruction has bounded amplification

Replace every $`f(E)`$ in (11) by the reciprocal average $`\widehat f(E)`$. The sum of the absolute coefficients in this explicit, possibly uncollected expression is

**(12)**

```math
L_C:=1+\sum_{F\in\mathcal F_C}2^{|F|}.
```

Every patch containing $`S`$ contains any one fixed site of $`S`$, so there are at most $`\nu`$ of them. A patch $`B`$ contributes at most

```math
\sum_{\varnothing\ne F\subseteq B\setminus S}2^{|F|}
=3^{|B\setminus S|}-1
\le3^{k-|S|}-1
```

to (12). Counting a support more than once only enlarges the bound, so

**(13)**

```math
L_C\le1+\nu\left(3^{k-|S|}-1\right).
```

In particular, $`L_C`$ is independent of $`N`$, $`h_C`$, and the noise rates. The number of required regions is also bounded:

```math
|\mathcal F_C|+1
\le1+\nu\left(2^{k-|S|}-1\right).
```

The [pair-estimator bound](estimator.md#4-finite-data-stability-at-every-coupling-strength) applies to every region directly relative to the same global $`h_C`$ and $`\Delta_C`$. It is not necessary to replace the denominator by the region-dependent $`f(E)`$. If all primitive estimates have additive error at most $`\tau`$, equations (11)–(13) therefore yield

```math
|\widehat h_C-h_C|
\le L_C\left[
3\frac{\Delta_C^2}{|h_C|+\Delta_C}
+4\Lambda\tau
\right],
```

with the same visibility-dependent $`\Lambda`$ defined in the estimator proof. This is the deterministic reconstruction step in the main theorem.

## 5. An overlapping-patch example

Take four qubits, target $`C=Z_1Z_2`$, and allowed patches $`\{1,2,3\}`$ and $`\{1,2,4\}`$. The possible spectator supports are $`\{3\}`$ and $`\{4\}`$, with no allowed support $`\{3,4\}`$. Then

```math
f(\varnothing)=h_C+x_{\{3\}}+x_{\{4\}},
\qquad
f(\{3\})=h_C+x_{\{4\}},
\qquad
f(\{4\})=h_C+x_{\{3\}},
```

and

```math
h_C=f(\{3\})+f(\{4\})-f(\varnothing).
```

The correction uses regions of at most three qubits. No four-qubit visibility is assumed. Imaginary dissipative pairs such as $`(X_3,Z_1Z_2X_3)`$ and $`(Y_4,Z_1Z_2Y_4)`$ realize the two shifts in (6). The [verification account](../verification/README.md) includes this nontrivial cancellation: the individual shifts can be first order in $`\Delta_C`$, while the final reciprocal reconstruction retains the second-order error for a resolved coupling.
