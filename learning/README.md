# Learning the calibration limit

How accurately can an unknown local Hamiltonian be learned when the preparations and measurements used to probe it are themselves imperfectly known? This project's answer connects complete positivity, reciprocal response measurements, local reconstruction, and an exact ambiguity between physical models.

The central quantity is

```math
\psi_h(\Delta)=\frac{\Delta^2}{|h|+\Delta},
\qquad \psi_0(0)=0.
```

Here $`h`$ is a canonical Hamiltonian coefficient and $`\Delta`$ is an ordered sum of geometric means of pairs of diagonal dissipative rates in its Pauli product sector. The estimator achieves an error controlled by this quantity plus statistical precision. A physical two-qubit family makes the same dependence unavoidable in the worst case. The [model and theorem](../science/model.md) specify the assumptions, constants, and quantifiers.

## The selected anchor

The single educational anchor is **Ángel Rivas and Susana F. Huelga, *Open Quantum Systems: An Introduction*, Springer, 2012**. Online references use the [public author preprint, arXiv:1104.5242v2, 9 February 2012](https://arxiv.org/html/1104.5242v2).

The [Rivas–Huelga bridge](rivas_huelga_bridge.md) connects its treatment of dynamical maps and Markov generators to the particular learning problem here. It translates the operator-basis normalization, works through a positive two-qubit noise block, and explains what unknown preparation and readout add to the problem. All section numbers in this learning route refer explicitly to the **preprint**; the bridge gives the correspondence with the published book.

The main source locations are preprint §§2.1–2.3 for operators and semigroups, §§3–4 for closed and open dynamics, and §5.2 for the completely positive generator and its coefficient matrix. In §5.2, the proof of Theorem 5.1 supplies the positive coefficient matrix; Eq. (51) gives the homogeneous generator. The project-specific bridge and proof pages supply the statistical, locality, and identifiability arguments.

## The 30-milestone map

The [milestone map](milestones.md) contains exactly **30 project-defined understanding targets** in two phases.

| Phase | Milestones | Scientific role |
|---|---|---|
| Background and preliminaries | M01–M12 | Build from states, observables, and channels to a canonical local generator, a physical calibration model, and a precise learning problem. |
| Narrative and innovation | M13–M30 | Assemble the reciprocal estimator and local reconstruction, account for their experiments, construct the matching physical ambiguity, and integrate the result with its evidence and attribution. |

The 12/18 allocation follows the structure of the problem. The background must bring together open-system dynamics and uncalibrated observations before the main question is well defined. The longer narrative then develops two complementary arguments: a constructive learning guarantee and a physical obstruction. M12 integrates the experimental framework; M30 integrates both proofs, their resources, and their scope. Dependencies within the map show how the component arguments fit together.

## Routes through the scientific account

| Reading purpose | Milestones | Authoritative pages |
|---|---|---|
| Understand the question and its assumptions | [M01–M12](milestones.md#m01-states-and-observable-probabilities) | [Anchor bridge](rivas_huelga_bridge.md), [model](../science/model.md) |
| Follow the achievable estimator | [M13–M24](milestones.md#m13-signed-pauli-randomization) | [Reciprocal estimator](../science/estimator.md), [local reconstruction](../science/local_reconstruction.md), [resources](../science/resources.md) |
| Understand the irreducible ambiguity | [M25–M28](milestones.md#m25-a-physical-two-qubit-ambiguity-family) | [Physical lower bound](../science/lower_bound.md) |
| Assess the whole claim and its evidence | [M29–M30](milestones.md#m29-evidence-and-attribution) | [Interpretation](../science/interpretation.md), [related work](../references/RELATED_WORK.md), [reproducible checks](../verification/README.md) |

The [science entrypoint](../science/README.md) provides the direct proof route. Readers who already know Lindblad dynamics can enter through the bridge's notation translation and the model, then follow the relevant narrative milestones.

## Distinctions that organize the route

**Canonical coefficients and measured slopes.** The Hamiltonian is defined in a fixed traceless Pauli representation of the generator. One antisymmetric response block can also contain dissipative contributions. Canonical averaging removes those contributions, and support cancellation removes the exterior terms left by a local restriction. These are separate steps in [local reconstruction](../science/local_reconstruction.md).

**Correlated SPAM and positive local visibility.** State preparation and measurement (SPAM) errors may be correlated across the register. The protocol needs known positive lower bounds on local parity visibility, while the actual gains remain unknown. Trusted endpoint rotations and signed Pauli randomization isolate signals that permit reciprocal cancellation; the [experiment derivation](../science/estimator.md#1-a-measured-signal-with-one-preparation-and-one-readout-factor) fixes their ordering.

**Noise rates and physical perturbations.** A weak diagonal rate $`\eta`$ beside a fixed rate $`\Gamma`$ permits cross coefficients of order $`\sqrt{\Gamma\eta}`$. The weak-signal error therefore has a square-root dependence on a diagonal rate. Its interpretation depends on keeping that rate separate from the size of the complete generator perturbation, as explained in the [lower-bound regimes](../science/lower_bound.md#6-estimation-lower-bound-and-matching-regimes).

**Statistical error and ambiguity.** More repetitions reduce statistical uncertainty. They cannot distinguish two physical models that give exactly the same accessible distributions. The [verification example](../verification/README.md#finite-count-reconstruction) separates sampling spread, interpolation bias, and the reciprocal estimator's residual bias, and reports its full shot equivalents.

The scientific sources also establish the contribution's boundaries. The [related-work account](../references/RELATED_WORK.md) credits the experimental primitives, boundary identities, gauge obstruction, and dissipative sector inherited from prior research. The quantitative modulus and its matching physical construction are the focus of this project. These primary research references provide provenance alongside the single educational anchor.
