# Reciprocal experiments and a stable estimator

Unknown preparation and readout gains can rescale a Pauli response without changing its physical generator. Reciprocal experiments eliminate those gains: one experiment prepares a component along $`P`$ and reads $`Q`$; the other interchanges their roles. Their derivative product, normalized by two zero-time signals, is independent of SPAM. Averaging the resulting reciprocal estimates and applying the [local reconstruction](local_reconstruction.md) gives the Hamiltonian-learning theorem in the [model](model.md).

The character-randomization identity used below is inherited from Flammia, Sinha and Tong, [FST2026, Eq. (94)](../references/RELATED_WORK.md). Their Theorem 31 also contains the reciprocal pure-Hamiltonian structure at the exact boundary. The present argument quantifies the error away from that boundary and treats the singular square root uniformly.

## 1. A measured signal with one preparation and one readout factor

Let $`D=2^N`$, and write $`\overline{\operatorname{Tr}}(X)=\operatorname{Tr}(X)/D`$. For a signed Hermitian Pauli $`P`$, let $`S_P=\operatorname{supp}(P)`$. Choose a trusted product Clifford $`U_P`$ satisfying

```math
U_P Z_{S_P}U_P^\dagger=P.
```

The sign of $`P`$ is included in this choice. A negative signed Pauli is not supplied as a density operator. Its coefficient is extracted from ordinary noisy preparations using signed classical outcomes.

Define the positive, support-dependent visibilities

```math
s_P:=s_{S_P}=\operatorname{Tr}(Z_{S_P}\rho_0),
\qquad
m_P:=m_{S_P}
=\overline{\operatorname{Tr}}
\left[Z_{S_P}\mathcal E^\dagger(Z_{S_P})\right].
```

For every Pauli used here, $`|S_P|\le k`$, so the [SPAM assumption](model.md) gives

```math
r_p\le s_P\le1,
\qquad
r_m\le m_P\le1.
```

The upper bound on $`m_P`$ follows because $`\mathcal E^\dagger`$ is unital and positive, and therefore contracts the operator norm of a Hermitian observable. These factors can vary with the support. They need not be calibrated individually.

For a projective Pauli $`R`$, define its character by $`RPR=\chi_P(R)P`$, with $`\chi_P(R)\in\{-1,1\}`$. Uniform averaging over all projective $`N`$-qubit Paulis gives, for any operator $`X`$,

```math
\mathbb E_R\bigl[\chi_P(R)RXR\bigr]
=\overline{\operatorname{Tr}}(PX)P.
\tag{1}
```

This is Pauli character orthogonality. It also holds for signed representatives because both occurrences of $`P`$ change sign together.

To estimate a transfer signal from $`P`$ to $`Q`$, perform the following experiment:

1. Prepare the fixed noisy state $`\rho_0`$ and apply $`U_P`$.
2. Apply a uniformly random product Pauli $`R_0`$, then evolve under the native generator for time $`t`$.
3. Apply an independent uniformly random product Pauli $`R_1`$, then $`U_Q^\dagger`$, and measure in the computational basis through the fixed readout channel $`\mathcal E`$.
4. Let $`Y\in\{-1,1\}`$ be the measured parity on $`S_Q`$. Record $`\chi_P(R_0)\chi_Q(R_1)Y`$.

The effective measured observable before the final basis change is

```math
M_Q=U_Q\mathcal E^\dagger(Z_{S_Q})U_Q^\dagger.
```

Equation (1) gives

```math
\mathbb E_{R_0}
\left[\chi_P(R_0)R_0U_P\rho_0U_P^\dagger R_0\right]
=\frac{s_P}{D}P,
```

```math
\mathbb E_{R_1}
\left[\chi_Q(R_1)R_1M_QR_1\right]
=m_QQ.
```

Consequently, the bounded recorded random variable has expectation

```math
F_{QP}(t)
=m_Qs_P\,
\overline{\operatorname{Tr}}
\left[Qe^{t\mathcal L}(P)\right].
\tag{2}
```

This calculation makes no product-noise or independence assumption about qubits within $`\rho_0`$ or $`\mathcal E`$. The random Paulis are implemented as single-qubit gates. The signal uses the native global evolution; no effective reduced semigroup is assumed.

Write

```math
T_{QP}=\overline{\operatorname{Tr}}\left[Q\mathcal L(P)\right],
\qquad
d_{QP}=F'_{QP}(0)=m_Qs_PT_{QP},
\qquad
z_P=F_{PP}(0)=m_Ps_P.
\tag{3}
```

Use the same basis conventions in the cross and zero-time experiments. Then

```math
-\frac{d_{QP}d_{PQ}}{z_Pz_Q}
=-T_{QP}T_{PQ}.
\tag{4}
```

The [resource analysis](resources.md) establishes simultaneous additive estimates of these derivatives and baselines from bounded outcomes.

## 2. Oriented Pauli pairs isolate the target sector

Fix a nonidentity canonical Pauli $`C`$. Choose $`P`$ anticommuting with $`C`$ and orient its partner as

```math
Q=-iCP.
```

Both operators are Hermitian, and

```math
-i[C,P]=2Q,
\qquad
-i[C,Q]=-2P.
\tag{5}
```

For this oriented pair define

```math
a=\frac{T_{QP}+T_{PQ}}4,
\qquad
b=\frac{T_{QP}-T_{PQ}}4.
\tag{6}
```

Thus $`T_{QP}=2(b+a)`$ and $`T_{PQ}=-2(b-a)`$. The coefficient $`h_C`$ contributes $`a=0`$ and $`b=h_C`$.

Only the dissipative product sector $`A\star B=C`$ can affect either entry in (6). Indeed, all three terms of $`\mathcal D_{AB}(P)`$ are proportional, projectively, to $`A\star B\star P`$. A Hamiltonian term with label $`R`$ contributes projectively to $`R\star P`$, and therefore contributes to $`Q`$ only when $`R=C`$.

For any Hermitian Pauli input and output, a transfer entry of $`\mathcal D_{AB}`$ has absolute value at most $`2`$. This follows by the triangle inequality: the sandwich term has norm one and the two anticommutator terms have norm at most one half each. Complete positivity gives

```math
|\alpha_{AB}|\le\sqrt{\alpha_{AA}\alpha_{BB}}.
```

Using the ordered leakage sum over allowed pairs,

```math
\Delta_C=
\sum_{\substack{(A,B)\in\mathcal I_d\\A\star B=C}}
\sqrt{\alpha_{AA}\alpha_{BB}},
```

the two dissipative transfer corrections are each bounded by $`2\Delta_C`$. Hence every oriented pair used by the estimator satisfies

```math
|a|\le\Delta_C,
\qquad
|b-h_C|\le\Delta_C.
\tag{7}
```

These bounds refer to the global canonical coefficient $`h_C`$, including when the two Paulis are measured inside a smaller region whose instantaneous Hamiltonian has an exterior contribution.

## 3. The reciprocal functional

Let $`[u]_+=\max\{u,0\}`$ and $`\operatorname{sgn}(0)=0`$. The ideal reciprocal estimate associated with one pair is

```math
g=
\frac12\operatorname{sgn}(d_{QP})
\sqrt{\left[-\frac{d_{QP}d_{PQ}}{z_Pz_Q}\right]_+}
=\phi(b,a),
```

```math
\phi(b,a):=
\operatorname{sgn}(b+a)\sqrt{[b^2-a^2]_+}.
\tag{8}
```

When the radicand is positive, $`|b|\gt|a|`$ and $`\operatorname{sgn}(b+a)=\operatorname{sgn}(b)`$. When it is nonpositive, the output is zero. Thus $`\phi`$ is unambiguous even at a zero slope or a vanishing coupling.

Define the noise modulus

```math
\psi_h(D)=\frac{D^2}{|h|+D},
\qquad
\psi_0(0)=0.
\tag{9}
```

**Lemma 1 — uniform reciprocal bias.** If $`|a|\le D`$ and $`|b-h|\le D`$, then

```math
|\phi(b,a)-b|\le3\psi_h(D).
\tag{10}
```

**Proof.** First, $`|\phi(b,a)-b|\le|a|`$ for all real $`a,b`$. If $`|b|\le|a|`$, the left side is $`|b|`$. Otherwise,

```math
|\phi(b,a)-b|
=|b|-\sqrt{b^2-a^2}
=\frac{a^2}{|b|+\sqrt{b^2-a^2}}
\le|a|.
\tag{11}
```

If $`D=0`$, then $`a=0`$ and $`\phi(b,0)=b`$. For $`D\gt0`$ and $`|h|\le2D`$, the first bound gives

```math
|\phi(b,a)-b|\le D\le\frac{3D^2}{|h|+D}.
```

For $`|h|\gt2D`$, we have $`|b|\ge|h|-D\gt D\ge|a|`$. Equation (11) then gives

```math
|\phi(b,a)-b|
\le\frac{D^2}{|h|-D}
\le\frac{3D^2}{|h|+D}.
```

This proves (10). $`\square`$

The relevant comparison is with $`b`$, not immediately with $`h_C`$. A single block can contain a linear dissipative contribution to $`b-h_C`$. The [canonical average](local_reconstruction.md#1-canonical-hamiltonian-projection) cancels that contribution before the final Hamiltonian is reconstructed.

## 4. Finite-data stability at every coupling strength

The square root is not uniformly Lipschitz as a function of two arbitrary slopes. Its possible singularity does not worsen the precision exponent of this learning task, because the physical constraints (7) relate the slopes to the same noise modulus.

Suppose every raw derivative and zero-time estimate in one reciprocal pair obeys

```math
|\widehat d_{QP}-d_{QP}|,
|\widehat d_{PQ}-d_{PQ}|,
|\widehat z_P-z_P|,
|\widehat z_Q-z_Q|
\le\tau.
\tag{12}
```

Let $`z_*=r_pr_m`$, and clip each empirical baseline to the interval $`[z_*/2,1]`$. Denote the clipped values by $`\widetilde z_P,\widetilde z_Q`$. Since each true baseline lies in $`[z_*,1]`$, clipping preserves the additive error bound in (12).

The implemented normalized coordinates and pair estimator are

```math
\widehat x=
\frac{\widehat d_{QP}}{2\sqrt{\widetilde z_P\widetilde z_Q}},
\qquad
\widehat y=
-\frac{\widehat d_{PQ}}{2\sqrt{\widetilde z_P\widetilde z_Q}},
\qquad
\widehat g=
\operatorname{sgn}(\widehat x)
\sqrt{[\widehat x\widehat y]_+}.
\tag{13}
```

The estimator uses neither $`\Delta_C`$ nor an estimate of its diagonal rates.

Let $`D_0`$ be a uniform bound on the absolute raw derivatives. Under the local-strength convention in the [model](model.md), one may take $`D_0=Jk`$; see [resources](resources.md). On $`[z_*/2,1]^2`$, each partial derivative of $`(uv)^{-1/2}`$ has absolute value at most $`2/z_*^2`$. Therefore the exact coordinates

```math
x=\frac{d_{QP}}{2\sqrt{z_Pz_Q}},
\qquad
y=-\frac{d_{PQ}}{2\sqrt{z_Pz_Q}}
```

satisfy

```math
|\widehat x-x|,|\widehat y-y|
\le K_0\tau,
\qquad
K_0=\frac1{z_*}+\frac{2D_0}{z_*^2}.
\tag{14}
```

Using (3) and (6), these exact coordinates can be written as

```math
x=\kappa(b+a),
\qquad
y=\kappa^{-1}(b-a),
\qquad
\kappa=
\sqrt{\frac{m_Qs_P}{m_Ps_Q}}
\in[\sqrt{z_*},z_*^{-1/2}].
\tag{15}
```

The factor $`\kappa`$ is unknown and is used only in the proof. Define fictitious perturbed block variables

```math
\widetilde b=
\frac{\kappa^{-1}\widehat x+\kappa\widehat y}{2},
\qquad
\widetilde a=
\frac{\kappa^{-1}\widehat x-\kappa\widehat y}{2}.
```

Then $`\widehat g=\phi(\widetilde b,\widetilde a)`$, and

```math
|\widetilde b-b|,|\widetilde a-a|
\le\Lambda\tau,
\qquad
\Lambda=K_0z_*^{-1/2}.
\tag{16}
```

Applying Lemma 1 with $`D=\Delta_C+\Lambda\tau`$ is legitimate because both inequalities in (7) remain valid with that enlarged $`D`$. Moreover,

```math
\frac{d}{dD}\psi_h(D)
=\frac{D(2|h|+D)}{(|h|+D)^2}
\le1
```

whenever the displayed derivative is defined, and $`\psi_0(D)=D`$. Thus $`\psi_h`$ is 1-Lipschitz on the nonnegative axis. Combining this fact with (16) gives the finite-data bound

```math
|\widehat g-b|
\le3\psi_{h_C}(\Delta_C)+4\Lambda\tau.
\tag{17}
```

Equation (17) includes $`h_C=0`$, $`\Delta_C=0`$, sign changes, and $`b^2=a^2`$. It requires no minimum nonzero coupling or externally supplied sign.

## 5. From pair estimates to the Hamiltonian

For a region $`W`$ containing $`\operatorname{supp}(C)`$, partition the anticommuting Pauli labels on $`W`$ into unordered pairs and orient each pair as in (5). There are $`4^{|W|}/4`$ such pairs. Let $`f_W`$ be the coefficient of $`C`$ in the instantaneous reduced generator. The exact projection identity proved in [local reconstruction](local_reconstruction.md) is

```math
f_W=
\frac1{4^{|W|}/4}\sum_e b_e.
```

Define $`\widehat f_W`$ by replacing every $`b_e`$ in this average with (13). On the simultaneous primitive-accuracy event (12), equation (17) implies

```math
|\widehat f_W-f_W|
\le3\psi_{h_C}(\Delta_C)+4\Lambda\tau.
\tag{18}
```

The final support correction is a known linear combination of these region estimates whose total absolute weight is at most $`L_C`$, with $`L_C`$ bounded by a constant depending on locality and degree. It follows that

```math
|\widehat h_C-h_C|
\le L_C
\left[
3\frac{\Delta_C^2}{|h_C|+\Delta_C}
+4\Lambda\tau
\right].
\tag{19}
```

Choosing the primitive accuracy proportional to the desired statistical precision yields the theorem in [model](model.md). The resource analysis supplies the probability and repetition count for the simultaneous event. The deterministic argument here does not require independence between different estimated coefficients within a shot.

At $`\Delta_C=0`$, one oriented pair already gives the correct coefficient in the infinite-data limit: take $`P`$ on one anticommuting site of $`C`$, so both $`P`$ and $`Q=-iCP`$ have weight at most $`k`$. The full averaged construction is needed for the stronger robustness guarantee away from that boundary.

The modulus is expressed in the true dissipative rates. Turning estimates of very small rates into optimally narrow, honest data-dependent confidence regions is a different statistical question and is not part of the theorem.
