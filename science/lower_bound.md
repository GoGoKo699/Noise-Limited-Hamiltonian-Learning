# Indistinguishable interactions and the calibration limit

The estimator's noise term reflects an ambiguity in the experimental model. Two physical generators can have different Hamiltonian coefficients and still produce the same distribution for every experiment allowed by the [model](model.md). Additional repetitions then cannot choose between them.

This page constructs such a pair with the same diagonal dissipative rates. Its separation has the same weak-signal and strong-signal dependence as the [learning guarantee](model.md). The general commuting-gauge indistinguishability principle is inherited from Flammia, Sinha and Tong, Theorem 18. The dissipative product sector below also appears in Malekakhlagh et al., Result 1. The contribution developed here is the quantitative physical family, its positivity margin, and the resulting sharp boundary modulus; see [Related work](../references/RELATED_WORK.md).

## 1. A two-qubit physical family

Use the canonical Hermitian Pauli basis, write $`IX=I\otimes X`$ and similarly for other labels, and take

```math
H=h\,ZZ.
```

The generator convention is

```math
\mathcal L_{h,c}(\rho)
=-i[H,\rho]
+\sum_{A,B\ne I}\alpha_{AB}
\left(A\rho B-\frac12\{BA,\rho\}\right).
```

Put diagonal rate $`\Gamma`$ on $`IX,IY,XI,YI`$ and diagonal rate $`\eta`$ on $`ZY,ZX,YZ,XZ`$. All other diagonal entries vanish. The only nonzero offdiagonal entries, together with their symmetric partners, are

```math
\alpha_{IX,ZY}=\alpha_{XI,YZ}=-\frac c2,
\qquad
\alpha_{IY,ZX}=\alpha_{YI,XZ}=\frac c2.
\tag{L1}
```

Here $`c`$ is real. After permuting its indices, the nonzero part of the Kossakowski matrix is a direct sum of four matrices of the form

```math
\begin{pmatrix}
\Gamma&\pm c/2\\
\pm c/2&\eta
\end{pmatrix}.
```

Consequently, for $`\Gamma,\eta\ge0`$,

```math
\alpha\succeq0
\quad\Longleftrightarrow\quad
|c|\le r,
\qquad r:=2\sqrt{\Gamma\eta}.
\tag{L2}
```

This is an exact physicality condition. In the ordered convention of the model, the target $`C=ZZ`$ has

```math
\Delta_{ZZ}=8\sqrt{\Gamma\eta}=4r.
\tag{L3}
```

There are four nonzero unordered diagonal-rate pairs whose projective product is $`ZZ`$, and the sum defining $`\Delta_{ZZ}`$ counts both orders. The value depends on the diagonal rates, even when some allowed offdiagonal entries vanish.

## 2. Exact Pauli blocks and the gauge transformation

For each row in the following table choose the indicated signed operator $`Q=-i(ZZ)P`$.

| $`P`$ | $`Q`$ |
|---|---|
| $`IX`$ | $`ZY`$ |
| $`IY`$ | $`-ZX`$ |
| $`XI`$ | $`YZ`$ |
| $`YI`$ | $`-XZ`$ |

With Pauli transfer convention $`T_{A,B}=\operatorname{Tr}[A\mathcal L(B)]/4`$, each ordered basis $`(P,Q)`$ has the block

```math
T^{(P,Q)}=
\begin{pmatrix}
-2\Gamma-6\eta&-2(h+c)\\
2(h-c)&-6\Gamma-2\eta
\end{pmatrix}.
\tag{L4}
```

The remaining Pauli labels have no offdiagonal transfer entries. The identity has diagonal entry zero; $`IZ,ZI,XX,XY,YX,YY`$ have diagonal entry $`-4(\Gamma+\eta)`$; and $`ZZ`$ has diagonal entry $`-8(\Gamma+\eta)`$.

These formulas follow directly from Pauli multiplication. A diagonal dissipator $`\gamma(A\rho A-\rho)`$ contributes $`-2\gamma`$ to a Pauli that anticommutes with $`A`$ and zero to a commuting Pauli. The four real cross terms in (L1) add symmetric offdiagonal entries in the four blocks, while the Hamiltonian adds their antisymmetric entries. Thus (L4) specifies the entire generator, including the entries outside the target's blocks.

Let $`\mathcal D_\lambda`$ denote the single-qubit depolarizing map,

```math
\mathcal D_\lambda(X)
=\lambda X+(1-\lambda)\operatorname{Tr}(X)\frac I2,
```

and define the invertible support gauge

```math
\mathcal G_\theta
=\mathcal D_{e^{-\theta}}\otimes\mathcal D_{e^{-\theta}}.
```

It multiplies a weight-$`w`$ Pauli by $`e^{-w\theta}`$ and commutes with every product of single-qubit unitary channels. In each block (L4), $`P`$ has weight one and $`Q`$ has weight two. The two offdiagonal entries therefore transform as

```math
h'-c'=e^{-\theta}(h-c),
\qquad
h'+c'=e^{\theta}(h+c).
```

The diagonal entries remain unchanged. Solving these equations gives the exact identity

```math
\mathcal G_\theta\mathcal L_{h,c}\mathcal G_\theta^{-1}
=\mathcal L_{h',c'},
\qquad
\begin{aligned}
h'&=h\cosh\theta+c\sinh\theta,\\
c'&=c\cosh\theta+h\sinh\theta.
\end{aligned}
\tag{L5}
```

In particular, $`\Gamma`$ and $`\eta`$ do not change, and

```math
(h')^2-(c')^2=h^2-c^2.
\tag{L6}
```

For this family, each reciprocal block estimate is $`\operatorname{sgn}(h)\sqrt{(h^2-c^2)_+}`$. Equation (L6) explains why that estimate is invariant along the family. Equality of this one statistic alone would not establish an operational lower bound. The next section proves equality of the complete accessible distributions.

## 3. Physical preparation and measurement

Choose $`\lambda=e^{-2}`$ and let the prepared state and readout channel of the first model be

```math
\rho_0=
\left(\frac{I+\lambda Z}{2}\right)^{\otimes2},
\qquad
\mathcal E=\mathcal D_\lambda^{\otimes2}.
```

For $`0\le\theta\le1/4`$, the transformed preparation and readout are

```math
\rho'_0=\mathcal G_\theta(\rho_0)
=\left(\frac{I+\lambda e^{-\theta}Z}{2}\right)^{\otimes2},
\qquad
\mathcal E'=\mathcal E\mathcal G_\theta^{-1}
=\mathcal D_{\lambda e^\theta}^{\otimes2}.
\tag{L7}
```

Both are physical because $`0\lt\lambda e^{-\theta}\le1`$ and $`0\lt\lambda e^\theta\lt1`$. The inverse gauge need not itself be a channel: the composed readout channel in (L7) is a channel, which is the required operational condition.

For every one- or two-qubit support, the preparation parity and diagonal readout visibility of both models are positive. A common lower bound is $`e^{-6}`$. Thus both models satisfy a fixed local-visibility promise independent of the noise rates and of $`h`$.

The constant $`e^{-6}`$ is only a convenient explicit choice. For any prescribed $`0\lt r_p,r_m\lt1`$ on two-qubit supports, choose

```math
\max(\sqrt{r_p},\sqrt{r_m})\lt\lambda\lt1
```

and a fixed $`\theta_0\gt0`$ satisfying

```math
\theta_0\le\frac14,
\qquad
\lambda e^{-\theta_0}\ge\sqrt{r_p},
\qquad
\lambda e^{\theta_0}\le1.
```

Using $`\theta\le\theta_0`$ gives the same construction with constants depending on the prescribed visibilities. The argument does not assert the same ambiguity when preparation or readout is perfectly calibrated. The two-qubit obstruction can also be embedded among additional uncoupled qubits; fixed-locality visibility bounds then remain independent of the total number of qubits.

## 4. Equality for every allowed controlled experiment

Let $`\Phi`$ be any sequence of native evolutions and trusted product-unitary pulses. From (L5),

```math
e^{t\mathcal L_{h',c'}}
=\mathcal G_\theta e^{t\mathcal L_{h,c}}\mathcal G_\theta^{-1}.
```

Commutation with every allowed pulse makes adjacent gauge factors cancel, so the entire transformed experiment obeys

```math
\Phi'=\mathcal G_\theta\Phi\mathcal G_\theta^{-1}.
\tag{L8}
```

For any computational-basis outcome $`z`$,

```math
\begin{aligned}
p'(z)
&=\operatorname{Tr}\!\left[
|z\rangle\langle z|\,
\mathcal E'\Phi'(\rho'_0)
\right]\\
&=\operatorname{Tr}\!\left[
|z\rangle\langle z|\,
\mathcal E\Phi(\rho_0)
\right]
=p(z).
\end{aligned}
\tag{L9}
```

The equality holds for arbitrary allowed pulse choices, arbitrary nonnegative evolution times, and the full outcome distribution. It therefore survives randomized experiment selection. It also survives classical adaptation between repetitions: conditioned on any common history, both models assign the same probability to the next outcome, so induction gives the same joint law of every finite transcript. An estimator's additional classical randomization cannot distinguish the models either.

The statement uses the experimental contract of the project: a fresh noisy preparation, native evolution interspersed with trusted single-qubit unitary control, and final noisy readout. It does not grant calibrated intermediate measurements, entangling controls, or access to the environment. Those operations could change which gauges commute with the experiment.

## 5. A quantitative pair with a uniform positivity margin

Fix

```math
0\lt\eta\le\Gamma\le\frac14,
\qquad
r=2\sqrt{\Gamma\eta}\le\frac14,
\qquad
0\le h\le\frac14.
```

Choose

```math
c_0=\frac r2,
\qquad
\theta=\frac{r}{4(h+r)}.
\tag{L10}
```

Then $`0\lt\theta\le1/4`$. The original generator is physical by (L2). For the transformed cross coefficient, use $`\sinh\theta\le\theta\cosh\theta`$ and $`h\theta\le r/4`$ to obtain

```math
c_1
=\frac r2\cosh\theta+h\sinh\theta
\le\frac{3r}{4}\cosh(1/4)
\lt r.
\tag{L11}
```

Thus the transformed generator is also physical, with a strict positivity margin in each active block. All coefficients remain bounded by one: for example, $`h_1\le\tfrac14\cosh(1/4)+\tfrac18\sinh(1/4)\lt0.3`$.

The Hamiltonian separation satisfies

```math
\begin{aligned}
g:=h_1-h
&=h(\cosh\theta-1)+\frac r2\sinh\theta\\
&\ge\frac r2\theta
=\frac{r^2}{8(h+r)}.
\end{aligned}
\tag{L12}
```

The two models retain exactly the same diagonal rates and the same $`\Delta_{ZZ}=4r`$. The transformed SPAM in (L7) makes their entire accessible data law identical.

For the more general visibility choice in Section 3, take $`\theta=\theta_0r/(h+r)`$. Then (L11) still holds because $`\theta_0\le1/4`$, and (L12) becomes $`g\ge\theta_0r^2/[2(h+r)]`$. This changes only a constant controlled by the visibility promise.

## 6. Estimation lower bound and matching regimes

Consider any estimator $`\widehat h`$ obtained from any allowed finite experiment protocol, with any number of repetitions and any classical adaptation. Let $`\mathbb E_0,\mathbb E_1`$ refer to the two models in Section 5. Their transcript and estimator distributions are identical. The pointwise triangle inequality therefore yields

```math
\max_{i\in\{0,1\}}
\mathbb E_i|\widehat h-h_i|
\ge\frac{g}{2}
\ge\frac{r^2}{16(h+r)}
\ge\frac{\Delta_{ZZ}^2}{256(h+\Delta_{ZZ})}.
\tag{L13}
```

For a probability statement, the two open intervals of radius $`g/2`$ around $`h_0`$ and $`h_1`$ are disjoint. Hence

```math
\max_{i\in\{0,1\}}
\Pr_i\!\left(|\widehat h-h_i|\ge\frac g2\right)
\ge\frac12.
\tag{L14}
```

These bounds remain valid if an estimator is supplied the exact diagonal rates $`\Gamma,\eta`$. The ambiguity lies in how the allowed offdiagonal dissipator, coherent coupling, and unknown SPAM fit together.

Equations (L12)–(L14) give

```math
g=\Omega\!\left(
\frac{\Gamma\eta}{h+\sqrt{\Gamma\eta}}
\right).
```

When $`h=O(\sqrt{\Gamma\eta})`$, this is order $`\sqrt{\Gamma\eta}`$. When $`h\gg\sqrt{\Gamma\eta}`$, it is order $`\Gamma\eta/h`$. The two members' values of $`h+\Delta_{ZZ}`$ differ only by a constant factor, so both are in the same regime. This matches the noise dependence of the upper guarantee up to constants over the stated model class. It does not establish an optimal repetition count for every Hamiltonian subfamily.

The rate parameter $`\eta`$ is a weak **diagonal dissipative rate**. The allowed cross coefficient already has size $`\sqrt{\Gamma\eta}`$. Accordingly, the weak-signal square root is not an amplification relative to the norm of the full dissipator perturbation. The stronger-signal conclusion is the quadratic suppression of its calibration ambiguity relative to that cross-sector scale.

## 7. Reproducible checks and their extent

The [verification suite](../verification/README.md) assembles the generator directly from its Hamiltonian and Kossakowski matrix. It compares the result with every block in (L4), checks the full similarity (L5), checks positive semidefiniteness, and compares all four readout probabilities after sampled product-unitary sequences. The proof above supplies the statement for every allowed sequence and every repetition count; a finite set of numerical circuits cannot establish that quantifier.

The same suite also checks the upper construction's canonical projection and overlapping-patch cancellation, and simulates actual signed-parity counts with unknown preparation/readout gains. Those checks distinguish an algebraic convention error, a statistical effect, and the physical ambiguity proved here.
