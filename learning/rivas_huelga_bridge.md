# From open quantum systems to noise-limited Hamiltonian learning

Suppose two qubits interact while also exchanging information with their surroundings. An experiment prepares them, lets them evolve, and records measurement outcomes. The aim is to infer an interaction strength. The difficulty studied here is that the preparation and readout are also imperfectly known: different physical interactions can sometimes produce exactly the same observable data.

Rivas and Huelga provide the open-system foundations. This bridge supplies the steps from those foundations to the repository's learning problem, using one small Pauli example throughout. The exact theorem and proofs remain in [the scientific account](../science/README.md); the [milestone map](milestones.md) organizes the broader understanding route.

## 1. One anchor, two numbering systems

The selected educational anchor is **Ángel Rivas and Susana F. Huelga, *Open Quantum Systems: An Introduction*, SpringerBriefs in Physics, first edition, ©2012**, DOI [10.1007/978-3-642-23354-8](https://link.springer.com/book/10.1007/978-3-642-23354-8). The authors' [book preprint, arXiv:1104.5242v2](https://arxiv.org/abs/1104.5242v2), revised 9 February 2012, is available as [HTML](https://arxiv.org/html/1104.5242v2) and [PDF](https://arxiv.org/pdf/1104.5242v2).

The preprint includes an introductory Section 1, so its main section numbers are one higher than the corresponding published book chapters. Source pointers below explicitly use **preprint** numbering.

| Foundation needed here | Published book | Author preprint v2 |
|---|---|---|
| Norms, exponentials, and semigroups | Ch. 1, *Mathematical Tools* | Sections 2.1–2.3 |
| Hamiltonian evolution | Ch. 2, *Time Evolution in Closed Quantum Systems* | Section 3 |
| Channels and complete positivity | Ch. 3, *Time Evolution in Open Quantum Systems* | Sections 4.1–4.2 |
| Physical inverses and temporal composition | Ch. 3 | Sections 4.4–4.5 |
| Positive generator coefficients and the GKSL form | Ch. 4, *Quantum Markov Process: Mathematical Structure* | Section 5.2, Theorem 5.1 and its proof; homogeneous form in Eq. (51) |

The main route is preprint Sections 4.2, 4.5, and 5.2, returning to Sections 2.1–2.3 when a norm or semigroup step needs clarification. In particular, the positive coefficient matrix used below is developed in the proof in **Section 5.2**. Section 5.3 discusses a related criterion for positive semigroups; complete positivity is essential for the coefficient-matrix argument here.

The book supplies channels, semigroups, and physical generators. The unknown-SPAM access model, reciprocal learning protocol, quantitative error law, and matching ambiguity construction require the research sources and proofs identified in [Related work](../references/RELATED_WORK.md).

## 2. From a quantum channel to a local generator

A density operator $`\rho`$ represents the prepared quantum state. It is positive semidefinite and has trace one. A measurement outcome represented by an effect $`M`$, with $`0\le M\le I`$, has probability $`\mathrm{Tr}(M\rho)`$. A quantum channel $`\Phi`$ maps states to states linearly and preserves trace. Complete positivity requires $`\Phi\otimes\mathrm{id}`$ to remain positive when a spectator system is included, even if that spectator is entangled with the measured system.

The spectator in this definition is a consistency test for the physical model. It does not give the learning protocol access to an ancillary qubit. Preprint Section 4.2 develops the channel description; Sections 4.4–4.5 distinguish physical reversibility and temporal composition.

Here the native evolution is assumed to have a fixed generator:

```math
\Phi_t=e^{t\mathcal L},
\qquad
\Phi_{t+s}=\Phi_t\Phi_s,
\qquad
\mathcal L(\rho)=
\left.\frac{d}{dt}\Phi_t(\rho)\right|_{t=0}.
```

The generator records the instantaneous change. This is a time-homogeneous Markovian model of the full register. A family of channels at individual times does not automatically have this composition property. Likewise, a small part of a Markovian register need not have autonomous Markovian dynamics after its neighbors are discarded.

### The Pauli convention

For $`N`$ qubits, let $`d=2^N`$. The matrices $`I,X,Y,Z`$ and their tensor products form an operator basis. The canonical representatives have no overall minus sign and obey

```math
\frac1d\mathrm{Tr}(AB)=\delta_{AB}.
```

For example, $`IX`$ means $`I\otimes X`$, and its support is the second qubit. A Pauli product can contain a phase: $`XY=iZ`$. The projective product $`A\star B`$ keeps the Pauli label and discards that phase.

With $`\hbar=1`$, the repository writes the generator as

```math
\mathcal L(\rho)
=-i\sum_{C\ne I}h_C[C,\rho]
+\sum_{A,B\ne I}\alpha_{AB}
\left(A\rho B-\frac12\{BA,\rho\}\right),
\qquad
\boldsymbol\alpha\succeq0.
```

The commutator is $`[C,\rho]=C\rho-\rho C`$; the anticommutator is $`\{BA,\rho\}=BA\rho+\rho BA`$. The real coefficients $`h_C`$ specify coherent interactions. The Hermitian matrix $`\boldsymbol\alpha`$ specifies dissipative combinations of Pauli directions. Its positivity means $`v^\dagger\boldsymbol\alpha v\ge0`$ for every complex vector $`v`$; it is not a density matrix and need not have trace one.

The notation translation from preprint Section 5.2 is:

| Source notation or convention | Repository convention |
|---|---|
| $`N`$ denotes the Hilbert-space dimension in the generator proof | $`N`$ counts qubits; the Hilbert-space dimension is $`d=2^N`$ |
| $`F_j`$ is orthonormal under the ordinary Hilbert–Schmidt trace | Choose $`F_A=A/\sqrt d`$; the repository uses unnormalized Paulis and a normalized trace |
| $`a_{AB}`$ multiplies $`F_A\rho F_B^\dagger-\{F_B^\dagger F_A,\rho\}/2`$ | $`\alpha_{AB}=a_{AB}/d`$ multiplies the corresponding Pauli expression |
| $`\mathcal E_{(t_1,t_0)}`$ denotes an evolution map | This bridge uses $`\Phi_t`$ for native evolution; $`\mathcal E`$ in the project denotes the readout-noise channel |

The coefficient rescaling follows by substituting $`F_A=A/\sqrt d`$ into both quadratic terms. It preserves positive semidefiniteness. If a Hamiltonian is expanded as $`H=\sum_A\xi_AF_A`$, then $`h_A=\xi_A/\sqrt d`$ in the repository basis.

To see why positivity enters, expand traceless jump operators as $`V_\mu=\sum_Av_{\mu A}A`$. A sum of dissipators with nonnegative rates $`\gamma_\mu`$ gives

```math
\alpha_{AB}=\sum_\mu\gamma_\mu
v_{\mu A}\overline{v_{\mu B}},
\qquad
x^\dagger\boldsymbol\alpha x
=\sum_\mu\gamma_\mu
\left|\sum_A\overline{x_A}v_{\mu A}\right|^2
\ge0.
```

Conversely, factoring a positive matrix produces jump operators. This basis calculation is the connection between the diagonal-jump form in the anchor and the matrix form used here.

Identity pieces of jump operators can be absorbed into a Hamiltonian term before fixing this representation. The project fixes traceless Pauli jump coordinates and a traceless Hamiltonian. That convention prevents an arbitrary identity shift or a different jump decomposition from being mistaken for the physical ambiguity proved later.

## 3. A positive two-qubit noise block

Take a two-qubit interaction $`H=hC`$ with

```math
C=ZZ,\qquad A=IX,\qquad B=ZY.
```

These satisfy $`AB=iC`$, $`[C,A]=2iB`$, and $`[C,B]=-2iA`$. Let the only populated dissipative directions be $`A,B`$, with a real cross coefficient $`q`$:

```math
\boldsymbol\alpha_{\{A,B\}}
=
\begin{pmatrix}
\Gamma&q\\
q&\eta
\end{pmatrix},
\qquad
\Gamma,\eta\ge0.
```

A two-by-two Hermitian matrix is positive semidefinite exactly when its diagonal entries and determinant are nonnegative. Thus this generator is physical precisely when

```math
q^2\le\Gamma\eta.
```

This explains a boundary effect. If $`\eta=0`$, positivity forces $`q=0`$, even when $`\Gamma`$ remains substantial. If $`\eta`$ becomes small and positive, a cross coefficient of order $`\sqrt{\Gamma\eta}`$ becomes possible.

For a numerical illustration in fixed inverse-time units, let $`\Gamma=0.04`$ and $`\eta=0.0001`$. Then $`q=0.002`$ is allowed. At equality the noise matrix has rank one and is realized by the single jump operator

```math
V=0.2A+0.01B,
\qquad
\mathcal D_V(\rho)
=V\rho V^\dagger-\frac12\{V^\dagger V,\rho\}.
```

The cross coefficient is twenty times the weak diagonal rate. That fact causes no physical inconsistency: positivity constrains it by a geometric mean. It also means that a square-root law in $`\eta`$ is not a square-root amplification relative to the entire dissipative perturbation; the cross term itself is already that large.

The same example exposes what an instantaneous experiment sees. Substitution into the generator gives

```math
\mathcal L(A)=-2\eta A+2(h+q)B,
\qquad
\mathcal L(B)=2(q-h)A-2\Gamma B.
```

For clarity, the cross terms contribute $`2qB`$ to $`\mathcal L(A)`$: each of the two ordered dissipators contributes $`qB`$, while their anticommutator contribution vanishes because $`A`$ and $`B`$ anticommute. The Hamiltonian contributes $`2hB`$. The diagonal rate $`\eta`$ damps $`A`$ without contributing to its transfer into $`B`$.

Define the Pauli-transfer slope by

```math
T_{QP}=\frac1d\mathrm{Tr}[Q\mathcal L(P)].
```

Then

```math
T_{BA}=2(h+q),
\qquad
T_{AB}=2(q-h),
\qquad
-T_{BA}T_{AB}=4(h^2-q^2).
```

When $`\eta=0`$, the forced value $`q=0`$ leaves opposite slopes with magnitude $`2|h|`$. Dissipation along $`A`$ can still be present. The learnable boundary is defined by missing product-sector noise, rather than by requiring all dissipation to disappear.

For this example the ordered leakage sum is $`\Delta_C=2\sqrt{\Gamma\eta}`$, counting $`(A,B)`$ and $`(B,A)`$. The full lower-bound family in the scientific proof uses four unordered pairs and has a different factor, $`\Delta_{ZZ}=8\sqrt{\Gamma\eta}`$. This small block illustrates positivity and reciprocal bias; it is not a substitute for that all-experiment indistinguishability construction.

## 4. What unknown SPAM changes

State-preparation-and-measurement noise is abbreviated **SPAM**. With an unknown prepared state $`\rho_0`$ and an unknown effective measurement effect $`M`$, the observed probability is

```math
p(t)=\mathrm{Tr}[M\Phi_t(\rho_0)].
```

Repeating an experiment estimates $`p(t)`$ more accurately. It does not automatically determine how that probability divides into a preparation, a generator, and a measurement.

For an invertible linear map $`\mathcal G`$, consider

```math
\rho_0'=\mathcal G(\rho_0),
\qquad
M'=(\mathcal G^{-1})^\dagger(M),
\qquad
\mathcal L'=\mathcal G\mathcal L\mathcal G^{-1}.
```

The transformed exponential is $`e^{t\mathcal L'}=\mathcal G e^{t\mathcal L}\mathcal G^{-1}`$. Inserting it into the probability cancels the adjacent maps and gives the same $`p(t)`$. If $`\mathcal G`$ also commutes with every trusted control operation, the cancellation extends through a whole controlled sequence.

This becomes an identifiability obstruction only when the transformed state, measurement, and generator all remain physical and satisfy the access promises. An arbitrary similarity transformation does not establish a physical lower bound. [The lower-bound proof](../science/lower_bound.md#3-physical-preparation-and-measurement) constructs admissible transformed preparations and readout explicitly.

The map $`\mathcal G^{-1}`$ need not be a quantum operation that the experimenter can implement. This is consistent with the physical-inverse restriction in preprint Section 4.4: the argument compares two admissible descriptions of a device, rather than applying an unphysical inverse in the laboratory.

Sampling error and identifiability therefore answer different questions. Sampling error measures uncertainty about observable probabilities with finite repetitions. Identifiability asks whether even exact knowledge of all accessible probabilities specifies the target coefficient. The repository's physical pair shows that some coefficient uncertainty survives the latter idealization.

## 5. Reciprocal measurements and the error law

The protocol does not independently calibrate every preparation and readout gain. Trusted endpoint rotations and random Pauli gates, together with signed classical outcomes, isolate a signal of the form

```math
F_{QP}(t)
=m_Qs_P\frac1d\mathrm{Tr}[Qe^{t\mathcal L}(P)].
```

Here $`s_P`$ is a preparation visibility and $`m_Q`$ a readout visibility. A signed parity is an ordinary measured parity multiplied by a known sign; no nonpositive state is prepared. The [signal proof](../science/estimator.md#1-a-measured-signal-with-one-preparation-and-one-readout-factor) establishes this identity even when SPAM is correlated across qubits.

At time zero define

```math
d_{QP}=F'_{QP}(0)=m_Qs_PT_{QP},
\qquad
z_P=F_{PP}(0)=m_Ps_P.
```

Swapping $`P,Q`$ gives a reciprocal experiment. Its derivative product satisfies

```math
-\frac{d_{QP}d_{PQ}}{z_Pz_Q}
=-T_{QP}T_{PQ}.
```

The four unknown gains cancel because the same preparation and readout conventions are reused. Positive visibility preserves the relevant sign and keeps the denominator away from zero.

Return to the two-qubit example with $`h>|q|`$. Taking one half of the positive square root of the normalized product gives

```math
\phi=\sqrt{h^2-q^2},
\qquad
h-\phi=\frac{q^2}{h+\sqrt{h^2-q^2}}.
```

The expression on the right comes from multiplying numerator and denominator by the conjugate. For a well-resolved interaction it is quadratic in the cross term, divided by the interaction scale. With $`h=0.1`$ and $`q=0.002`$, it gives $`\phi\simeq0.099979998`$ and a bias of about $`0.000020002`$.

A general generator is harder. Its reciprocal block can contain both a symmetric contamination and a dissipative shift of the antisymmetric part. A single block's antisymmetric entry need not equal the canonical Hamiltonian coefficient. The proof therefore averages suitable blocks, cancels the first-order dissipative skew contribution, and subtracts exterior spectator contributions using regions of size at most the promised locality.

Together with a uniform treatment of sign changes and the square-root singularity, those steps give the [simultaneous theorem](../science/model.md#4-simultaneous-learning-theorem):

```math
|\widehat h_C-h_C|
\le
\epsilon+3L_C\frac{\Delta_C^2}{|h_C|+\Delta_C},
\qquad
\Delta_C=
\sum_{\substack{(A,B)\in\mathcal I_d\\A\star B=C}}
\sqrt{\alpha_{AA}\alpha_{BB}}.
```

The known constant $`L_C`$ bounds the amplification from local reconstruction. The sum is ordered and includes only structurally allowed pairs. The fraction is defined as zero when both arguments vanish.

There are three regimes:

| Condition | Consequence of the upper bound |
|---|---|
| $`\Delta_C=0`$ | The noise-dependent term vanishes; statistical precision controls the error. |
| $`\lvert h_C\rvert\lesssim\Delta_C`$ | The permitted error scale is $`O(\Delta_C)`$. |
| $`\lvert h_C\rvert\gg\Delta_C`$ | The noise-dependent scale improves to $`O(\Delta_C^2/\lvert h_C\rvert)`$. |

The positive two-qubit gauge family in [the lower bound](../science/lower_bound.md#6-estimation-lower-bound-and-matching-regimes) attains the same dependence up to constants. This sharpness is worst-case over the allowed multi-qubit models, not a claim that every coefficient has this ambiguity. Zero leakage is a sufficient condition, not a classification of the entire identifiable boundary.

## 6. Assumptions and resources

The book's physical framework does not by itself supply an experimental learning theorem. The following promises carry specific parts of the argument; their complete form is in [the model](../science/model.md).

| Promise | Why the learning result needs it |
|---|---|
| Fixed native generator and fixed SPAM across independent repetitions | Signals collected at different settings refer to one device model and admit concentration estimates. |
| Known patches of at most $`k`$ qubits, bounded patch incidence, and bounded local strength | Only a constant number of local ingredients enters each coefficient; local derivatives have bounds independent of register size. |
| Known conservative positive preparation and readout parity visibilities on supports of size at most $`k`$ | Reciprocal normalization is stable and signs are meaningful. Exact gains remain unknown. |
| Trusted product single-qubit controls and requested evolution times | Endpoint character selection and the timing-based derivative estimate have their stated meanings. |
| Final noisy measurement, without additional calibrated instruments | This specifies the experiments for which the physical ambiguity is proved. |

Correlations among the registered qubits in the prepared state are allowed. They are a different issue from correlations with an unmodelled environment that would invalidate the assumed native semigroup. The protocol does not infer a Markovian model from arbitrary data or absorb control drift into its SPAM cancellation.

The statistical accuracy $`\epsilon`$ can be improved with repetitions. The intrinsic noise term depends on the true diagonal rates and need not disappear with additional data. The estimator does not need those rates as input, but the inequality is not automatically an empirical confidence radius.

The [resource proof](../science/resources.md) estimates derivatives of the native global signal over a fixed short-time window. Locality gives an analytic neighborhood; polynomial interpolation then controls derivative bias and sampling error. Compatible local settings can be measured in parallel. For fixed locality, incidence, strength, and visibility promises, the total repetitions and unknown-evolution time are bounded by

```math
O\!\left(
\epsilon^{-2}\log^4(2/\epsilon)
\log(2N/\delta)
\right),
```

with simultaneous success probability at least $`1-\delta`$. Each repetition still uses $`O(N)`$ one-qubit gates and returns $`N`$ measured bits. Timing precision, classical work, and constants are charged in the resource account.

Matching the irreducible calibration scale does not prove an optimal number of repetitions. Other subfamilies or access models may permit better precision scaling. Likewise, a logarithmic dependence of shot count on register size does not erase the cost of operating and reading the register.

## 7. Route into the proofs

The complete reasoning has several distinct dependencies. The following route connects each conceptual step to its authoritative home without replacing the proof with the worked example.

| Question after reading this bridge | Exact project page |
|---|---|
| Which canonical coefficient is estimated, under which promises? | [Model, Sections 1–4](../science/model.md) |
| How are signed signals formed, and why are finite-data errors additive even at zero coupling? | [Estimator, Sections 1–4](../science/estimator.md) |
| Why does canonical averaging remove dissipative shifts, and why do small regions suffice? | [Local reconstruction](../science/local_reconstruction.md) |
| How are derivatives sampled without a reduced-semigroup assumption? | [Resources, Sections 1–3](../science/resources.md) |
| How can two different physical Hamiltonians agree under every permitted control sequence? | [Lower bound, Sections 1–6](../science/lower_bound.md) |
| What do finite numerical checks establish? | [Verification and its stated limits](../verification/README.md) |

The foundational channel and generator results belong to Rivas–Huelga's account and the original work it cites. The learning framework also inherits the commuting-gauge obstruction, exact-boundary condition, signed experiments, and derivative-estimation machinery from Flammia–Sinha–Tong; the explicit dissipative sector has antecedents in Malekakhlagh and collaborators. Those research dependencies remain credited in [Related work](../references/RELATED_WORK.md).

The additional result developed here is the quantitative calibration law, its local estimator, and a physical near-boundary family matching that law. The book explains why the generators are physical; the research proofs establish what can be learned from the stated experiments.
