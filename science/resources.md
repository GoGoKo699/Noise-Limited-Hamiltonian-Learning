# Experiments, derivatives and physical resources

The [estimator proof](estimator.md) reduces learning to simultaneous additive estimates of native-evolution derivatives and zero-time baselines. This page completes that reduction with a finite sampling protocol. The analytic interpolation and weighted-node method follow [FST2026, Lemma 28, and Trefethen2019](../references/RELATED_WORK.md); the locality argument is also present in FST Appendix A. We give their application and constants for the present experimental signals.

## 1. Local observables have a uniform analytic neighborhood

Use the local-strength contract (2) in the [model](model.md). If an observable is supported on $`S`$, a summand with $`B\cap S=\varnothing`$ annihilates it: its adjoint acts on the exterior identity and $`\mathcal L_B^\dagger(I)=0`$.

Starting with a Pauli $`Q`$ of weight at most $`k`$, expand $`(\mathcal L^\dagger)^nQ`$ into ordered local words. At step $`j`$, a nonzero term meets a support of size at most $`k+(j-1)(k-1)\le kj`$. The sum of the norms of all next local terms meeting that support is at most $`Jkj`$. Induction therefore gives

```math
\|(\mathcal L^\dagger)^nQ\|_\infty
\le (Jk)^n n!,
\qquad n\ge0.
\tag{1}
```

Only trace annihilation, locality and the incident norm bound are used here. Individual local summands need not be completely positive.

For the experimental signal $`F_{QP}(t)=m_Qs_P\,2^{-N}\operatorname{Tr}[Qe^{t\mathcal L}(P)]`$, normalized trace against a Pauli is bounded by the operator norm. Hence

```math
|F_{QP}(z)|\le\frac1{1-Jk|z|}
\quad\text{when }Jk|z|\lt1,
\qquad
|F'_{QP}(0)|\le D_0:=Jk.
\tag{2}
```

These are size-independent bounds. They do not assume that local reduced dynamics is an autonomous semigroup.

Set $`G=\max\{1,Jk\}`$ and choose the fixed native-time window

```math
T=\frac1{4G}.
\tag{3}
```

Under $`t=T(x+1)/2`$, the Bernstein ellipse with parameter $`\rho=2`$ maps into $`|t|\le9T/8`$. Equation (2) bounds the analytic signal there by $`B=2`$. On real nonnegative times the signal is the mean of a signed parity in $`\{-1,1\}`$ and therefore lies in $`[-1,1]`$.

## 2. A derivative estimate with charged repetitions

For an integer $`m\ge1`$, let

```math
x_j=\cos(j\pi/m),
\qquad t_j=\frac T2(x_j+1),
\qquad j=0,\ldots,m.
```

Let $`p_m`$ interpolate the rescaled signal at these Chebyshev–Lobatto nodes. Its endpoint derivative is a weighted sum

```math
\frac2T p'_m(-1)=\sum_{j=0}^m w_jF(t_j),
\qquad
W_m:=\sum_{j=0}^m|w_j|=\frac{2m^2}{T}.
\tag{4}
```

For explicit weights, put $`c_0=c_m=2`$ and $`c_j=1`$ otherwise. The endpoint row of the interpolation differentiation matrix gives

```math
w_j=\frac2T\frac2{c_j}
\frac{(-1)^{m+j}}{-1-x_j}\quad(j\lt m),
\qquad
w_m=-\frac{2m^2+1}{3T}.
```

The products $`w_jT_m(x_j)`$ all have the sign $`(-1)^{m-1}`$, where $`T_m`$ is the degree-$`m`$ Chebyshev polynomial. Since $`|T_m(x_j)|=1`$, exact interpolation of $`T_m`$ gives $`\sum_j|w_j|=|(2/T)T'_m(-1)|=2m^2/T`$, including $`m=1`$.

For completeness, analyticity with bound $`B`$ on the parameter-2 ellipse gives Chebyshev coefficients of magnitude at most $`2B2^{-\ell}`$. At the Lobatto nodes, each higher Chebyshev polynomial aliases to one of degree at most $`m`$. Its endpoint derivative and the original derivative differ in magnitude by at most $`2\ell^2`$. Consequently,

```math
\left|\frac2T p'_m(-1)-F'(0)\right|
\le\frac{8B}{T}\sum_{\ell>m}\ell^2 2^{-\ell}
=\frac{8B}{T}2^{-m}(m^2+4m+6).
\tag{5}
```

Choose $`m`$ so that the last expression is at most $`\tau/2`$. For fixed model parameters this requires $`m=O(\log(2/\tau))`$.

In each repetition, draw $`j`$ with probability $`|w_j|/W_m`$, perform the [signed-parity experiment](estimator.md#1-a-measured-signal-with-one-preparation-and-one-readout-factor) at time $`t_j`$, and record $`W_m\operatorname{sgn}(w_j)Y_j`$. The mean of $`M`$ such records is an unbiased estimate of the interpolating derivative and has range $`[-W_m,W_m]`$. Hoeffding's inequality yields

```math
\Pr\!\left(
|\widehat D-\mathbb E\widehat D|\gt\tau/2
\right)
\le2\exp\!\left(-\frac{M\tau^2}{8W_m^2}\right).
\tag{6}
```

If $`K`$ is the total number of primitive derivative and baseline coordinates, it suffices to use

```math
M=\left\lceil
\frac{8W_m^2}{\tau^2}\log\frac{2K}{\delta}
\right\rceil
\tag{7}
```

per global derivative setting. Each baseline is an ordinary zero-time signed-parity mean; $`\lceil2\tau^{-2}\log(2K/\delta)\rceil`$ repetitions per baseline setting suffice. Combining (5), (6), and a union bound gives raw error at most $`\tau`$ on every required coordinate with probability at least $`1-\delta`$.

## 3. Parallel local settings

Every pair of Paulis required by the reconstruction lies within one allowed patch. Color the patch-overlap graph. Its maximum degree is at most $`k(\nu-1)`$, so at most $`k(\nu-1)+1`$ colors suffice. Within a color the patches are disjoint.

For each color, cycle through the constant number of local ordered Pauli-pair settings on its patches, padding smaller patches with idle choices. At most a constant multiple of $`16^k`$ choices per color is needed, including baselines and known sign conventions. In one global repetition, apply the specified basis rotations on all active disjoint patches, draw the endpoint product Paulis on the entire register, use one common sampled time, and read all computational-basis bits. Each active patch yields its own signed parity.

Other patches can interact through the unknown dynamics. This does not affect the argument: every signal is a derivative of the same native global channel, and the character calculation isolates its specified input and output Pauli labels. Disjointness is used to implement compatible endpoint basis settings, not to assume dynamically independent subsystems.

The common Chebyshev degree, nodes and sampling probabilities depend only on the promised constants and target accuracy, so the same time can be used for every active patch. Correlations between their outcomes within a repetition are allowed. Concentration is applied separately to each coordinate across independent repetitions, followed by a union bound.

There are $`K=O_{k,\nu}(N)`$ coordinates and $`S_0=O_{k,\nu}(1)`$ global settings. With

```math
z_*=r_pr_m,
\qquad
\Lambda=
\frac{1/z_*+2Jk/z_*^2}{\sqrt{z_*}},
\qquad
\tau=\frac{\epsilon}{4\Lambda L_{\max}},
\tag{8}
```

equations (5)–(8) and the deterministic reconstruction bound prove Theorem 1. The total repetitions are

```math
M_{\mathrm{tot}}
=O_{k,\nu,J,r_p,r_m}\!\left(
\epsilon^{-2}\log^4(2/\epsilon)\log(2N/\delta)
\right).
\tag{9}
```

The interpolation, patch coloring and support sums are explicit finite procedures. No global state or process tomography is performed.

## 4. Costs and precision assumptions

| Resource | Account |
|---|---|
| Fresh preparations and final measurements | One each per repetition; their total count is $`M_{\mathrm{tot}}`$. |
| Unknown evolution | At most $`T`$ per repetition, hence total at most $`TM_{\mathrm{tot}}`$. |
| Trusted one-qubit gates | $`O(N)`$ endpoint gates per repetition; total $`O(NM_{\mathrm{tot}})`$. |
| Classical outcomes | Up to $`N`$ bits per repetition. A logarithmic shot count still carries linear register readout cost. |
| Classical processing | $`O_{k,\nu}(NM_{\mathrm{tot}})`$ arithmetic operations, plus polynomial logarithmic precision work for weights and scheduling. |
| Storage | Local signal sums can be accumulated online with $`O_{k,\nu}(N)`$ accumulators; retaining all raw records costs $`O(NM_{\mathrm{tot}})`$ bits. |
| Time access | Samples include time zero and a fixed window $`[0,T]`$; the smallest positive Lobatto time is of order $`T/m^2`$. |

Finite constant factors include the exponential dependence on the fixed locality $`k`$ and inverse visibility factors. The theorem does not promise a useful practical sample count for every device. The [finite-count demonstration](../verification/README.md) reports its actual shot equivalents explicitly.

For a bounded timing error $`\xi_t`$ at each requested nonnegative time, the signed signal changes by at most $`D_0\xi_t`$. Indeed, the adjoint quantum semigroup contracts the operator norm and

```math
|F'(t)|
\le\|e^{t\mathcal L^\dagger}\mathcal L^\dagger(Q)\|_\infty
\le D_0.
```

The corresponding derivative bias is at most $`W_mD_0\xi_t`$. Thus any timing-imperfection allowance must improve with the target precision; it is sufficient to allocate $`\xi_t=O(\tau/(W_mD_0))`$ when $`D_0\gt0`$. The stated theorem assumes exact requested timing and trusted controls. It does not absorb arbitrary control drift into the SPAM cancellation.

The sampling rate is an achievable upper bound for this protocol. In particular, it does not exclude improved precision scaling in subfamilies that permit coherent long-time amplification or additional calibrated controls.
