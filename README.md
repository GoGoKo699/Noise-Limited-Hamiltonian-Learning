# Noise-Limited Hamiltonian Learning

Unknown state preparation and readout can make different quantum interactions experimentally indistinguishable. This project gives a local learning procedure and a matching worst-case limit near a dissipative boundary, where positivity restricts that ambiguity.

For a canonical Hamiltonian coefficient $`h_C`$, define the ordered noise scale

```math
\Delta_C=
\sum_{\substack{(A,B)\in\mathcal I_d\\A\star B=C}}
\sqrt{\alpha_{AA}\alpha_{BB}},
```

using structurally allowed Pauli pairs and the diagonal rates of the positive Kossakowski matrix. The estimator achieves

```math
\boxed{
|\widehat h_C-h_C|
\le K\left[
\epsilon+\frac{\Delta_C^2}{|h_C|+\Delta_C}
\right]
}
```

simultaneously for all local coefficients, with a constant independent of system size. The fraction is zero when both arguments vanish.

| Interaction regime | Noise-dependent error scale |
|---|---|
| Exact boundary: $`\Delta_C=0`$ | Arbitrarily accurate recovery as the statistical precision improves |
| Weak coupling: $`\lvert h_C\rvert\lesssim\Delta_C`$ | $`O(\Delta_C)`$ |
| Resolved coupling: $`\lvert h_C\rvert\gg\Delta_C`$ | $`O(\Delta_C^2/\lvert h_C\rvert)`$ |

A physical two-qubit family makes the same noise dependence unavoidable in the worst case, even with unlimited data and arbitrary permitted local-control sequences. The limit concerns the uncertainty allowed by the full model class; particular noise patterns and single-qubit coefficients can be more identifiable.

## Scientific account

Start with the [model and exact theorem](science/model.md), then follow the [science reading map](science/README.md).

| To understand | Read |
|---|---|
| What is unknown, trusted, and estimated | [Model and guarantees](science/model.md) |
| How two reciprocal experiments cancel SPAM gains | [Estimator and uniform stability](science/estimator.md) |
| Why block averaging and small-region correction recover the global coefficient | [Local reconstruction](science/local_reconstruction.md) |
| How many repetitions, gates, measured bits, and evolution time are used | [Resources](science/resources.md) |
| Why all allowed experiments can agree on different physical Hamiltonians | [Matching lower family](science/lower_bound.md) |
| What the boundary and two regimes mean for calibration | [Interpretation and examples](science/interpretation.md) |
| Established ingredients and the surviving contribution | [Related work](references/RELATED_WORK.md) and [bibliography](references/references.bib) |
| Exact calculations and finite-count experiments | [Verification](verification/README.md) |

The [LLM reading guide](llms.txt) maps scientific questions to their authoritative pages.

## Learning route

The [learning map](learning/README.md) connects the open-system foundations to this project's calibration question. It contains [30 milestones](learning/milestones.md), organized from the physical model to the estimator, resource account, and matching ambiguity.

The single educational anchor is Ángel Rivas and Susana F. Huelga, *Open Quantum Systems: An Introduction* (first edition, 2012). The [source-to-project bridge](learning/rivas_huelga_bridge.md) identifies the relevant sections, translates conventions, and supplies the steps from quantum dynamical maps to learning under unknown preparation and readout. It also distinguishes the published book's chapter numbers from the author preprint's section numbers.

## Access and resources

The generator has a known, bounded-degree local interaction pattern and bounded local strength. Preparation and measurement errors are fixed but unknown and may be correlated across the entire register. Only their local parity visibilities have positive lower bounds. The protocol uses trusted single-qubit gates, native evolution, and final computational-basis readout.

For fixed locality, degree, strength and visibility bounds, the total repetitions and unknown-evolution time are

```math
O\!\left(
\epsilon^{-2}\log^4(2/\epsilon)\log(2N/\delta)
\right),
```

where $`N`$ is the number of qubits and $`1-\delta`$ the simultaneous confidence. Each repetition still requires $`O(N)`$ local gates and register readout. The [resource account](science/resources.md) includes timing precision, classical processing and locality-dependent constants. The repetition bound is an achievable upper bound, not a metrological optimality claim.

## Reproduce the finite checks

With Python 3.12 and the pinned numerical dependencies, run from the repository root:

```bash
python3 -m pip install -r verification/requirements.txt
python3 verification/run_all.py
```

The suite independently checks canonical Hamiltonian projection, the physical gauge family, controlled outcome probabilities, cancellation across overlapping patches, and the uniform stability bound. A finite-count experiment uses actual binomial signed-parity observations and estimated SPAM baselines. Its largest reconstruction represents **880 million physical-shot equivalents**; the [recorded costs and results](verification/README.md#finite-count-reconstruction) distinguish a mechanism check from a practical resource advantage.

## Scope and attribution

The SPAM gauge framework, positivity boundary condition, signed Pauli experiments and derivative-estimation tools are established in Flammia–Sinha–Tong. The dissipative sector used in the explicit example also appears in Malekakhlagh and collaborators. The contribution developed here is the sharp, signal-dependent calibration law, its local constructive estimator, and a physical near-boundary family with the matching ambiguity. The [comparison](references/RELATED_WORK.md) identifies those dependencies precisely.

The theorem uses the true diagonal dissipative rates. It does not by itself supply optimally narrow confidence intervals from empirical rate estimates. The weak-rate square root is a geometric mean of diagonal rates; the allowed offdiagonal perturbation is already that large. Trusted control, fixed SPAM and the stated measurement access are part of the result's domain.

## Purpose and contact

This repository serves as a record of the work and a guide for the author’s self-directed learning. For discussion or potential collaboration, please contact Ruge Lin at [gogoko699@gmail.com](mailto:gogoko699@gmail.com).
