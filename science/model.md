# The model and learning guarantee

The Hamiltonian of an open quantum system describes its coherent interactions. When both the preparations used to probe that system and the final measurements are imperfectly known, some changes in those interactions can be absorbed into changes in the calibration model. This project determines how accurately local interaction coefficients can nevertheless be learned near a specified dissipative boundary.

The result has two parts: a constructive, simultaneous learning guarantee and a physical family attaining its noise dependence. The main assumptions follow the local Lindbladian and SPAM framework of [Flammia, Sinha and Tong (FST2026)](../references/RELATED_WORK.md). Their boundary condition, gauge obstruction and experimental primitives are established ingredients. The new statement quantifies the achievable error and matching ambiguity as one moves away from that boundary.

## 1. Generator, locality and strength

There are $`N`$ qubits. Write $`\mathcal P_N=\{I,X,Y,Z\}^{\otimes N}`$ for the canonical Hermitian Pauli representatives, with no overall minus sign. The projective product $`A\star B`$ discards the phase of $`AB`$. Supports refer to nonidentity tensor factors. The unknown time-independent generator is

```math
\mathcal L(\rho)
=-i\sum_{C\in\mathcal I_h}h_C[C,\rho]
+\sum_{(A,B)\in\mathcal I_d}\alpha_{AB}
\left(A\rho B-\frac12\{BA,\rho\}\right),
\qquad \boldsymbol\alpha\succeq0.
\tag{1}
```

Every index in $`\mathcal I_h`$ and both indices in $`\mathcal I_d`$ are nonidentity Paulis. The Hamiltonian is traceless, its coefficients are real, and $`\alpha_{BA}=\overline{\alpha_{AB}}`$. Equation (1), with these traceless Pauli jump coordinates, fixes the canonical Hamiltonian convention. An identity component of the Hamiltonian has no dynamical effect and is not an estimation target.

A known patch family $`\mathsf P`$ specifies locality. Each patch contains at most $`k`$ qubits, and each qubit belongs to at most $`\nu`$ patches. The set $`\mathcal I_h`$ contains the nonidentity Pauli labels supported within an allowed patch. The ordered set $`\mathcal I_d`$ contains pairs whose joint support lies within an allowed patch. Structurally forbidden coefficients are zero. A known sparser coefficient pattern is also permitted; keeping the full patch family only changes constant overheads.

For a concrete strength convention, group the canonical terms into local, trace-annihilating summands $`\mathcal L_B`$ supported on allowed patches, assigning each term to one patch that contains its support. Assume a known bound

```math
\mathcal L=\sum_B\mathcal L_B,
\qquad
\sup_i\sum_{B\ni i}
\|\mathcal L_B^\dagger\|_{\infty\to\infty}\le J.
\tag{2}
```

The norm is the induced operator norm on observables of the embedded map on the full register, including its identity action on spectator qubits. A bare local induced norm for a non-completely-positive summand need not have this stability under extension. Each summand annihilates trace, so $`\mathcal L_B^\dagger(I)=0`$. The summands need not individually generate completely positive semigroups; the full generator in (1) does. Bounded canonical coefficients, fixed $`k`$ and fixed $`\nu`$ imply a size-independent bound of the form (2): each Pauli left/right multiplication has embedded norm one, so each commutator or dissipator in (1) has embedded norm at most two before multiplication by its coefficient. All constants below may depend on these local parameters, but not on $`N`$.

For fixed locality and incidence, the number of possible coefficients is $`O(N)`$. A known pattern and a bounded local strength are genuine inputs to the learning problem. They do not supply the unknown nonzero coefficients or their signs.

## 2. Experimental access and SPAM

Each independent repetition begins with the same unknown state $`\rho_0`$. The available coherent controls are trusted products of single-qubit unitaries, with requested native evolution intervals $`e^{t\mathcal L}`$. Final computational-basis measurement is preceded by the same unknown channel $`\mathcal E`$. All measured bits are available. Classical randomization and adaptation between repetitions are permitted.

Preparation and readout errors may be correlated across the register. For every nonempty support $`S`$ of size at most $`k`$, assume known conservative promise bounds $`r_p,r_m\gt0`$ such that

```math
s_S:=\operatorname{Tr}(Z_S\rho_0)\ge r_p,
\qquad
m_S:=2^{-N}\operatorname{Tr}
\left[Z_S\mathcal E^\dagger(Z_S)\right]\ge r_m.
\tag{3}
```

The individual gains $`s_S,m_S`$ remain unknown. Their positive lower bounds fix the sign and prevent loss of all local information; they do not require the global preparation or measurement channel to be close to ideal. The same fixed system and SPAM model is used across repetitions. Drift and memory between repetitions are outside this contract.

The implemented upper-bound protocol uses only endpoint product Clifford/Pauli gates, one native evolution interval, and final measurement. The lower bound permits arbitrary finite sequences of trusted product unitaries and native evolution intervals within each repetition, as well as adaptive choices between repetitions. It supplies no intermediate measurement, reset instrument, calibrated entangling operation or ancillary interaction. Additional calibrated access can change the information-theoretic limit.

Control gates and time settings are ideal in the stated model. [Resources](resources.md) records their counts, the required time interval, and how bounded timing errors enter the derivative estimate.

## 3. The relevant noise scale

For any target coefficient $`h_C`$, define the ordered leakage sum

```math
\boxed{
\Delta_C=
\sum_{\substack{(A,B)\in\mathcal I_d\\A\star B=C}}
\sqrt{\alpha_{AA}\alpha_{BB}}.
}
\tag{4}
```

Both orders of a distinct pair are included. Only structurally allowed pairs enter this definition. Positivity implies $`|\alpha_{AB}|\le\sqrt{\alpha_{AA}\alpha_{BB}}`$, so $`\Delta_C`$ controls every possible offdiagonal dissipative contribution in the product sector of $`C`$. Its summand count is bounded for each target by locality and patch incidence.

The diagonal rates are invariant under the support-diagonal SPAM gauges in FST and can be learned by their separate protocol. The estimator here does not need to estimate those rates or know $`\Delta_C`$ in advance. The error theorem is expressed in the true physical rates.

At $`\Delta_C=0`$, all allowed dissipative coefficients with product $`C`$ vanish. This includes the sufficient boundary condition in FST Theorem 31 and, with a fixed structural promise, its immediate sparse-pattern version. The condition is sufficient. It is not a classification of every identifiable boundary coefficient.

The scale in (4) is not the norm of the entire dissipator or of a perturbation to it. For diagonal rates $`\Gamma`$ and $`\eta`$, a physical cross coefficient can already be of order $`\sqrt{\Gamma\eta}`$. A square-root dependence on a weak diagonal rate therefore has a different meaning from square-root sensitivity to the full generator perturbation.

## 4. Simultaneous learning theorem

Let

```math
L_C=1+\sum_{F\in\mathcal F_C}2^{|F|},
\qquad
L_{\max}=1+\nu(3^{k-1}-1),
\qquad
\psi_h(D)=\frac{D^2}{|h|+D},
\quad\psi_0(0)=0,
```

where $`\mathcal F_C`$ is the known family of nonempty exterior supports defined in [local reconstruction](local_reconstruction.md#3-a-support-formula-using-only-allowed-patches). In particular $`L_C\le L_{\max}`$.

**Theorem 1 — achievable calibration.** Under (1)–(3), for $`0\lt\epsilon\le1/2`$ in the chosen time units and $`0\lt\delta\lt1`$, there is an explicit estimator which simultaneously satisfies, with probability at least $`1-\delta`$,

```math
\boxed{
|\widehat h_C-h_C|
\le\epsilon+3L_C\frac{\Delta_C^2}{|h_C|+\Delta_C}
\quad\text{for every }C\in\mathcal I_h.
}
\tag{5}
```

Its total experimental repetitions and total unknown-evolution time are at most

```math
O_{k,\nu,J,r_p,r_m}\!\left(
\epsilon^{-2}\log^4(2/\epsilon)
\log(2N/\delta)
\right).
\tag{6}
```

Each repetition uses $`O(N)`$ single-qubit gates and returns $`N`$ measured bits. Classical processing is linear in the number of collected bits up to fixed-locality factors and logarithmic precision overhead. These costs remain present when the shot count grows only logarithmically with $`N`$.

**Proof route.** The [reciprocal experiment](estimator.md) cancels unknown gains and proves a uniform finite-data bound for each transfer block. [Canonical averaging and local reconstruction](local_reconstruction.md) recover the global coefficient with absolute linear-combination weight $`L_C`$, using supports of size at most $`k`$. The [resource theorem](resources.md) supplies all required derivatives and baselines at accuracy $`\tau=\epsilon/(4\Lambda L_{\max})`$, where $`\Lambda`$ is the explicit visibility constant in the estimator proof. Substitution gives (5), and patch coloring gives (6). No minimum nonzero coupling is assumed.

## 5. Matching noise dependence and its quantifiers

The [physical lower family](lower_bound.md) uses two qubits, $`C=ZZ`$, and fixed diagonal rates $`\Gamma,\eta`$. It has $`\Delta_{ZZ}=8\sqrt{\Gamma\eta}`$. For a stated constant parameter range and nonzero SPAM uncertainty, it contains two models with exactly the same complete experimental distributions, but different Hamiltonian coefficients. Every estimator, with arbitrarily much data and all permitted controls, obeys

```math
\max_{i=0,1}\mathbb E_i|\widehat h-h_i|
\ge
\frac{\Delta_{ZZ}^2}{256(h_0+\Delta_{ZZ})}
\tag{7}
```

for the explicit visibility constants used in the construction. For any fixed $`0\lt r_p,r_m\lt1`$, the same scaling holds with a positive constant depending on the visibility allowance. The construction and a corresponding probability statement are proved in the lower-bound page. Perfectly calibrated access is a different limiting case.

Thus the dependence $`\Delta^2/(|h|+\Delta)`$ is achievable in general and unavoidable in the worst case over the allowed multi-qubit model class. Equation (7) is not a lower bound for every noise pattern or every coefficient. Single-qubit Hamiltonian coefficients are already universally learnable by FST, and (5) can be loose for them. Additional structural knowledge can also remove ambiguity that the broader class permits.

The statistical repetition bound is an upper bound, not an assertion of optimal metrological scaling. The rate-dependent error inequality does not by itself produce an optimally narrow confidence interval from empirical noise-rate estimates.
