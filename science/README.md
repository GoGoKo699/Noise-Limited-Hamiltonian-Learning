# Scientific reading map

The central question is how accurately an interaction can be learned when preparation and readout are not separately calibrated. The answer depends on both the interaction strength and which dissipative directions are populated. Complete positivity limits the cross terms that can imitate a change of interaction; reciprocal experiments turn that limit into an achievable error guarantee.

| Step | Authoritative page | Main result |
|---|---|---|
| 1 | [Model](model.md) | Exact access, canonical coefficients, ordered noise scale, simultaneous theorem and lower-bound quantifiers |
| 2 | [Estimator](estimator.md) | Signed experiments, gain cancellation and a uniform finite-data reciprocal bound |
| 3 | [Local reconstruction](local_reconstruction.md) | Canonical block averaging and support correction within the original local visibility promise |
| 4 | [Resources](resources.md) | Native derivative sampling, parallel local settings and complete physical cost account |
| 5 | [Lower bound](lower_bound.md) | Positive two-qubit generators with identical distributions for every permitted controlled experiment |
| 6 | [Interpretation](interpretation.md) | Boundary recovery, weak/strong crossover, worked examples and practical limits |

For the constructive proof, read Steps 1–4 in order. For the information-theoretic obstruction, read Step 1 followed by Step 5. The [related-work account](../references/RELATED_WORK.md) separates inherited tools from the quantitative contribution. The [verification suite](../verification/README.md) tests explicit formulas and finite observations; it supports the proof rather than replacing its general quantifiers.

The common conventions are fixed in [model](model.md): canonical Hermitian Paulis, a traceless Hamiltonian, the dissipator ordering $`A\rho B-\{BA,\rho\}/2`$, ordered leakage pairs, and fixed positive local visibilities. Every theorem uses those conventions.

For a foundations-first route, use the [learning map](../learning/README.md) and [Rivas–Huelga bridge](../learning/rivas_huelga_bridge.md). The scientific pages above remain the authoritative statements and proofs.
