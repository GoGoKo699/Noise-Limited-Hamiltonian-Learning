# Relation to prior work

The result studied here is a quantitative limitation on learning an unknown Hamiltonian inside a local Lindblad generator when preparation and readout are uncalibrated. The model and theorem are specified in [the model](../science/model.md), [the estimator](../science/estimator.md), [local reconstruction](../science/local_reconstruction.md), [the lower bound](../science/lower_bound.md), and [resource accounting](../science/resources.md). This comparison uses the primary versions listed below, checked on 30 October 2026.

The claimed dependence is

```math
|\widehat h_C-h_C|
\le K\left[\epsilon+\frac{\Delta_C^2}{|h_C|+\Delta_C}\right],
\qquad
\Delta_C=\sum_{\substack{(A,B)\in\mathcal I_d\\A\star B=C}}
\sqrt{\alpha_{AA}\alpha_{BB}}.
```

The sum is over ordered, structurally allowed pairs. The fraction is zero when both its arguments vanish. The matching lower construction concerns the dependence on the true Hamiltonian coefficient and the diagonal dissipative rates, up to constant factors. It is a worst-case statement over physical generators and physical preparation/readout models.

## The closest continuous-time result

[Flammia, Sinha, and Tong (FST2026)](https://arxiv.org/html/2609.35265v1) supplies the access framework and much of the machinery. Its Definition 8 permits correlated SPAM with positive local visibility; Proposition 10 supplies commuting support gauges. Theorem 18 already establishes physical models indistinguishable under every allowed controlled experiment. Theorem 31 gives a sufficient condition on the positivity boundary for Hamiltonian invariance; its proof, particularly Eq. (117), already contains reciprocal Hamiltonian transitions.

| Inherited ingredient | Precise source location |
|---|---|
| Invariant diagonal Kossakowski rates | Lemma 30 and Section 5.1 |
| Signed endpoint Pauli randomization | Eq. (94) |
| Bounded-sample Chebyshev derivative estimation | Lemma 28 |
| Size-independent local derivative bounds | Appendix A, Eqs. (128)–(129) |
| Support-based elimination of local coefficients | Section 5.1.1 |

The source's conclusion identifies robust learning near the boundary as an open direction. Its exact-boundary reciprocal identities and positivity inequality make an exact-boundary learner a short extension. Neither gauge freedom nor all-control indistinguishability is a new principle here.

The additional analysis in this repository is the uniform modulus above: reciprocal square roots are combined with cancellation of the dissipative skew contribution and a local spectator-support subtraction. This gives an operational estimator throughout the crossover between weak and resolved Hamiltonian signals. An explicit physical gauge orbit attains the same dependence in the worst case. Zero leakage includes the sufficient condition of Theorem 31 and its immediate extension using promised structural zeros. It is not a complete boundary characterization, and the theorem does not claim an algorithm for every additional invariant in Theorem 32.

## Pauli-noise symmetry and positivity

[Malekakhlagh, Chen, Govia, and Seif (MCGS2026)](https://arxiv.org/abs/2607.02481v1) studies finite Clifford gates with a specified ideal gate Hamiltonian. Its Results 1–3 identify dissipative product sectors that create first-order asymmetry between conjugate Pauli fidelities. The paragraph following Result 1 explicitly lists

```math
(IX,ZY),\quad (IY,ZX),\quad (XI,YZ),\quad (YI,XZ).
```

These are the same four unordered dissipative pairs used in our two-qubit lower construction. This selection pattern is prior work. Appendix F also stresses that an isolated off-diagonal dissipative coefficient cannot be varied freely under complete positivity and uses positive rank-one examples. Section IV and Appendix G implement a depolarizing SPAM gauge; the bias discussion after Eq. (18) relates an approximate symmetry condition to SPAM-estimation error.

Our target is an unknown canonical Hamiltonian coefficient of the native generator. The new calculations supply the signal-dependent denominator, an estimator under the stated local-visibility promise, and a physical indistinguishable family with the same rate. These are different claims from symmetry-based calibration of a known ideal finite gate. The shared sector selection, gauge structure, and positivity constraints deserve explicit credit.

## Hamiltonian learning and self-consistent tomography

| Work | Relevant established result | Relation to the present guarantee |
|---|---|---|
| [Yu, Sun, Han, and Yuan, Quantum 7, 1045 (YSHY2023)](https://quantum-journal.org/papers/q-2023-06-29-1045/) | Hamiltonian learning with robust randomized benchmarking ideas, under the paper's sparsity, signal-size, and implementation-noise assumptions. | Its Section 2.2 and Assumptions 1–3 specify a different model, including closed Hamiltonian evolution and gate-independent Pauli noise. Its SPAM promise depends on the signal and experimental parameters. It does not state the continuous-time Kossakowski-rate ambiguity law considered here. |
| [Huang, Tong, Fang, and Su, Physical Review Letters 130, 200403 (HTFS2023)](https://doi.org/10.1103/PhysRevLett.130.200403) | Trusted-control learning of interacting local Hamiltonians with inverse-precision total evolution time and robustness to preparation/readout error. | This is a useful resource comparison in the Hamiltonian setting. The present short-time, noisy-generator protocol gives an upper bound on shots and duration; it does not establish universal optimality of its precision exponent. |
| [Nielsen et al., Quantum 5, 557 (NielsenGST2021)](https://quantum-journal.org/papers/q-2021-10-05-557/) | Self-consistent characterization of gates, preparations, and measurements, including similarity-gauge freedom and gauge fixing. | The general gauge obstruction is established background. The present restriction to trusted product controls and local continuous-time dynamics determines which physical gauge transformations and coefficient errors matter. |

The generator representation and its positivity conditions rest on the foundational results of [Gorini, Kossakowski, and Sudarshan (GKSL1976)](https://doi.org/10.1063/1.522979) and [Lindblad (Lindblad1976)](https://doi.org/10.1007/BF01608499). Polynomial interpolation and differentiation are standard numerical-analysis tools; see [Trefethen (Trefethen2019)](https://doi.org/10.1137/1.9781611975949).

## Boundaries of the claim

The estimator does not require the exact preparation or measurement gains. Known conservative positive visibility bounds enter its stability constants and clipping rule. The implemented readout protocol needs positive computational-parity visibilities: its trusted basis changes precede the fixed readout channel, as proved in [the signal calculation](../science/estimator.md#1-a-measured-signal-with-one-preparation-and-one-readout-factor). FST Definition 8 imposes the broader positivity promise for all local Pauli observables.

The upper error bound applies simultaneously to all target coefficients. Matching sharpness is a worst-case property of the allowed multi-qubit class, not a lower bound for every coefficient or noise pattern. In particular, single-qubit Hamiltonian coefficients are already universally learnable in FST, and the present upper bound can be loose for them. The error expression is an oracle inequality in the true diagonal dissipative rates; it is not presented as a directly observed confidence radius.

For a strong diagonal rate $`\Gamma`$ and a weak rate $`\eta`$, the lower family has $`\Delta_C\asymp\sqrt{\Gamma\eta}`$. Positivity then permits off-diagonal coefficients of that same order. Consequently, the crossover

```math
\frac{\Gamma\eta}{|h_C|+\sqrt{\Gamma\eta}}
```

must not be described as a square-root dependence on the norm of the entire dissipative perturbation.

The source comparisons support a specific research claim about the estimator and physical ambiguity modulus. They do not establish a claim to the first gauge obstruction, the first robust Hamiltonian-learning algorithm, or a complete characterization of all boundary-identifiable coefficients.

Machine-readable bibliographic records are in [references.bib](references.bib).
