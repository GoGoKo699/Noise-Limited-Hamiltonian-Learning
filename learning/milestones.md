# Thirty milestones for noise-limited Hamiltonian learning

This map states the understanding targets of the project, from its physical ingredients to the complete calibration guarantee and limitation. It contains **12 background/preliminaries milestones and 18 narrative/innovation milestones**. The allocation and reading routes are explained in the [learning entrypoint](README.md). SPAM abbreviates state preparation and measurement.

The selected anchor is Rivas–Huelga, *Open Quantum Systems: An Introduction*. **RH section numbers below refer to [arXiv:1104.5242v2][rh], not to the published book's chapter numbers.** The [anchor bridge](rivas_huelga_bridge.md) supplies the numbering correspondence and the source-to-project translation. The canonical scientific statements and proofs live under [science](../science/README.md).

FST refers to [Flammia, Sinha, and Tong, arXiv:2609.35265v1][fst]. MCGS refers to [Malekakhlagh, Chen, Govia, and Seif, arXiv:2607.02481v1][mcgs]. These are primary research references for precise attribution. Every milestone points to the relevant proof, model statement, or worked example; the map does not attempt to enumerate every technical step in those sources.

## Phase I: background and preliminaries

### M01. States and observable probabilities

**Central question.** What is physically observed when a quantum system is prepared and measured?

**Understanding target.** Relate a positive trace-one density operator, an observable, and the expectation $`\mathrm{Tr}(O\rho)`$. For a Pauli parity, distinguish an individual outcome in $`\{-1,1\}`$ from its expectation and from an unknown coefficient of the generator.

**Dependencies and story role.** No earlier milestone is required. This introduces the observable data from which the rest of the learning problem is built.

**Conceptual connection.** The estimator's elementary data are bounded parity outcomes; the Hamiltonian appears through how their expectations change with time.

**Sources.** [RH §4, opening discussion of reduced states and measurement probabilities][rh]; [bridge §2](rivas_huelga_bridge.md#2-from-a-quantum-channel-to-a-local-generator); [estimator §1](../science/estimator.md#1-a-measured-signal-with-one-preparation-and-one-readout-factor).

### M02. Composite systems and reduced descriptions

**Central question.** What information is retained when only part of a many-qubit system is observed?

**Understanding target.** Interpret tensor products, operator support, and the partial trace. A reduced state can arise from a correlated global state. Restricting an observable to a small region does not establish independence of that region's dynamics, preparation, or measurement.

**Dependencies and story role.** Uses M01. It extends a single observation to the many-body setting and establishes why locality must be stated separately from independence.

**Conceptual connection.** Correlated SPAM is allowed, while local observables and allowed patches keep the learning task finite. The same distinction later prevents an unjustified reduced-semigroup assumption.

**Sources.** [RH §4, Eq. (29), and §4.1][rh]; [model §§1–2](../science/model.md#1-generator-locality-and-strength); [local reconstruction §2](../science/local_reconstruction.md#2-what-a-local-region-actually-reveals).

### M03. Coherent evolution and interaction coefficients

**Central question.** What does a Hamiltonian coefficient mean operationally?

**Understanding target.** Interpret the coherent derivative $`-i[H,\rho]`$ and the expansion $`H=\sum_C h_C C`$ in Hermitian Pauli strings. Understand why $`h_C`$ is real, why adding an identity term has no effect, and why an overall factor in the Hamiltonian convention changes inferred coefficients.

**Dependencies and story role.** Uses M01–M02. It identifies the parameter being learned before dissipative evolution and calibration enter.

**Conceptual connection.** The oriented Pauli response later has slope $`2h_C`$ in a pure target block. Its sign and factor two follow from this convention.

**Sources.** [RH §3][rh]; [model §1, Eq. (1)](../science/model.md#1-generator-locality-and-strength); [estimator §2, Eq. (5)](../science/estimator.md#2-oriented-pauli-pairs-isolate-the-target-sector).

### M04. Channels and their adjoints

**Central question.** How can one describe the same experiment through either states or observables?

**Understanding target.** Recognize a completely positive trace-preserving map as a physical channel and use $`\mathrm{Tr}[O\mathcal E(\rho)]=\mathrm{Tr}[\mathcal E^\dagger(O)\rho]`$. Identify how trace preservation becomes unitality of the adjoint and how readout noise becomes an effective observable.

**Dependencies and story role.** Uses M01–M03. This gives the mathematical language for combining dynamics, trusted gates, and an unknown measurement channel.

**Conceptual connection.** The experiment's readout visibility is a coefficient of $`\mathcal E^\dagger(Z_S)`$. Its location relative to the trusted basis rotation determines the cancellation formula.

**Sources.** [RH §§4.2–4.3][rh]; [bridge §4](rivas_huelga_bridge.md#4-what-unknown-spam-changes); [estimator §1](../science/estimator.md#1-a-measured-signal-with-one-preparation-and-one-readout-factor).

### M05. Semigroups and infinitesimal generators

**Central question.** What additional structure is assumed by a time-independent Lindblad model?

**Understanding target.** Connect a generator $`\mathcal L`$, the channel family $`e^{t\mathcal L}`$, and the derivative at time zero. Understand the semigroup composition rule and $`\mathcal L^\dagger(I)=0`$. Separate this global dynamical assumption from any claim that a subsystem evolves autonomously.

**Dependencies and story role.** Uses M03–M04. It connects observed time dependence to the unknown local generator.

**Conceptual connection.** Native short-time data can reveal transfer derivatives even when tracing out spectators does not produce a finite-time semigroup on the observed region.

**Sources.** [RH §§2.2–2.3, §4.5, and §5.2, Eq. (51)][rh]; [model §1](../science/model.md#1-generator-locality-and-strength); [local reconstruction §2](../science/local_reconstruction.md#2-what-a-local-region-actually-reveals).

### M06. Canonical Lindblad coordinates

**Central question.** How is a Hamiltonian defined unambiguously inside a dissipative generator?

**Understanding target.** Read the canonical representation with nonidentity Pauli jump coordinates, real Hamiltonian coefficients, and a Hermitian positive semidefinite Kossakowski matrix. Track the ordering $`A\rho B-\{BA,\rho\}/2`$. Understand why identity components in jump operators must be absorbed into the Hamiltonian before comparing coefficients.

**Dependencies and story role.** Uses M03–M05. It fixes the coordinates in which every upper and lower bound will be stated.

**Conceptual connection.** Orthogonal Hamiltonian projection and the physical lower family must use the same canonical normalization. A change of representation alone is not a physical ambiguity between models.

**Sources.** [RH §5.2, proof of Theorem 5.1 and Eq. (51)][rh]; [bridge §2](rivas_huelga_bridge.md#2-from-a-quantum-channel-to-a-local-generator); [model §1](../science/model.md#1-generator-locality-and-strength).

### M07. Positive noise matrices and their boundary

**Central question.** How does complete positivity constrain dissipative cross terms?

**Understanding target.** Derive $`|\alpha_{AB}|^2\le\alpha_{AA}\alpha_{BB}`$ from a two-dimensional principal submatrix. Recognize that a zero diagonal entry forces the corresponding row and column to vanish, while a weak positive diagonal rate permits a cross coefficient on a square-root scale.

**Dependencies and story role.** Uses M06. This supplies the physical inequality behind both learnability at the boundary and ambiguity near it.

**Conceptual connection.** The same positive matrix constraint controls contamination of a measured response and makes the lower-bound generators physical.

**Sources.** [RH §5.2, positive coefficient matrix in the proof of Theorem 5.1][rh]; [bridge §3](rivas_huelga_bridge.md#3-a-positive-two-qubit-noise-block); [model §3](../science/model.md#3-the-relevant-noise-scale).

### M08. Pauli transfers and product sectors

**Central question.** Which terms of the generator can contribute to a chosen Pauli response?

**Understanding target.** Use normalized transfer entries $`T_{QP}=2^{-N}\mathrm{Tr}[Q\mathcal L(P)]`$, distinguish canonical labels from signed Pauli representatives, and interpret the phase-free product $`A\star B`$. For an anticommuting target pair, track the orientation $`Q=-iCP`$.

**Dependencies and story role.** Uses M02–M03 and M06. It turns the generator representation into particular observables with controlled signs and normalization.

**Conceptual connection.** The product condition $`A\star B=C`$ selects precisely the dissipative sector that can interfere with the target Hamiltonian response.

**Sources.** [bridge §§2–3](rivas_huelga_bridge.md#2-from-a-quantum-channel-to-a-local-generator); [estimator §2](../science/estimator.md#2-oriented-pauli-pairs-isolate-the-target-sector); [local reconstruction §1](../science/local_reconstruction.md#1-canonical-hamiltonian-projection).

### M09. Locality and paid resources

**Central question.** What makes learning many coefficients possible with bounded local overhead?

**Understanding target.** Interpret the known patch size $`k`$, site incidence $`\nu`$, and incident strength bound $`J`$. Distinguish the number of experimental repetitions from total native-evolution time, gate count, readout bits, and classical work. Understand why the strength contract uses norms stable under embedding among spectator qubits.

**Dependencies and story role.** Uses M02, M05, and M08. It extends individual response coordinates to a family of $`O(N)`$ possible local targets.

**Conceptual connection.** Locality controls derivative growth, compatible experimental settings, and support reconstruction. Logarithmic dependence of shot count on system size still carries a linear register-level cost per repetition.

**Sources.** [RH §2.1 for induced norms][rh]; [model §1, Eq. (2)](../science/model.md#1-generator-locality-and-strength); [resources §§3–4](../science/resources.md#3-parallel-local-settings).

### M10. Unknown SPAM with positive local visibility

**Central question.** What calibration knowledge is sufficient when preparation and readout may be globally correlated?

**Understanding target.** State the fixed-state and fixed-readout-channel model and its support-dependent gains $`s_S,m_S`$. Distinguish unknown gains from known positive lower bounds $`r_p,r_m`$. Place the readout channel after the trusted final basis rotation and identify the independent-repetition assumption.

**Dependencies and story role.** Uses M02, M04, and M09. This completes the observational part of the model without assuming independent errors across qubits.

**Conceptual connection.** Positive visibility supplies sign information and stable normalization; randomization later isolates these gains. Arbitrary drift between repetitions or untrusted control gates would alter the contract.

**Sources.** [model §2, Eq. (3)](../science/model.md#2-experimental-access-and-spam); [estimator §1](../science/estimator.md#1-a-measured-signal-with-one-preparation-and-one-readout-factor); [related work, SPAM comparison with FST Definition 8](../references/RELATED_WORK.md#boundaries-of-the-claim).

### M11. Physical calibration gauges

**Central question.** When can different generators give the same observations?

**Understanding target.** Follow a simultaneous similarity transformation of the generator, preparation, and readout. Identify the need for commutation with trusted controls and for both resulting models to be physical. An inverse similarity map need not itself be a channel if the transformed preparation and composed readout are physical.

**Dependencies and story role.** Uses M04, M06, and M10. It introduces identifiability as a property of an entire experimental model.

**Conceptual connection.** Calibration freedom can change a canonical Hamiltonian coefficient while preserving all observable probabilities. This is the obstruction that the constructive estimator must approach.

**Sources.** [RH §4.4 for inverses of physical maps][rh]; [FST Proposition 10][fst]; [bridge §4](rivas_huelga_bridge.md#4-what-unknown-spam-changes); [lower bound §3](../science/lower_bound.md#3-physical-preparation-and-measurement).

### M12. The complete learning problem

**Central question.** What exactly must a valid learning theorem promise?

**Understanding target.** Combine the canonical generator, known locality and strength, unknown fixed SPAM, trusted product controls, target coefficients, accuracy, confidence, and charged resources into one operational statement. Distinguish identifiability with unlimited observations from finite-sample estimation and from a worst-case impossibility result.

**Dependencies and story role.** Integrates M01–M11. This closes the background phase by making the question precise enough for both a constructive answer and a counterexample family.

**Conceptual connection.** The upper and lower arguments share an access model. Their comparison is meaningful only when the parameter convention, calibration allowance, physicality conditions, and error criterion agree.

**Sources.** [model §§1–5](../science/model.md); [bridge §6](rivas_huelga_bridge.md#6-assumptions-and-resources); [related work, boundaries of the claim](../references/RELATED_WORK.md#boundaries-of-the-claim).

## Phase II: narrative and innovation

### M13. Signed Pauli randomization

**Central question.** How can correlated preparation and readout produce one isolated transfer signal?

**Understanding target.** Follow the endpoint Pauli character averages and the trusted rotations satisfying $`U_PZ_{S_P}U_P^\dagger=P`$. Understand the bounded signed-parity experiment with mean $`F_{QP}(t)=m_Qs_P\,2^{-N}\mathrm{Tr}[Qe^{t\mathcal L}(P)]`$, including signed orientations.

**Dependencies and story role.** Uses M08, M10, and M12. It supplies the first concrete experimental primitive in the constructive argument.

**Conceptual connection.** Character orthogonality removes unwanted global components while leaving positive support-dependent gains. It works with correlated SPAM and the native global channel.

**Sources.** [estimator §1, Eqs. (1)–(3)](../science/estimator.md#1-a-measured-signal-with-one-preparation-and-one-readout-factor); [FST Eq. (94)][fst]; [bridge §5](rivas_huelga_bridge.md#5-reciprocal-measurements-and-the-error-law).

### M14. Reciprocal cancellation of unknown gains

**Central question.** Which measured combination removes both preparation and readout gains?

**Understanding target.** Combine the two slopes $`d_{QP},d_{PQ}`$ with the zero-time baselines $`z_P,z_Q`$ to obtain $`-d_{QP}d_{PQ}/(z_Pz_Q)=-T_{QP}T_{PQ}`$. Track the factor one half and positive-visibility sign convention in the reciprocal square root.

**Dependencies and story role.** Uses M08, M10, and M13. It turns the randomized primitive into a calibration-independent response statistic.

**Conceptual connection.** Multiplicative nuisance gains cancel across reciprocal experiments. The remaining issue is the difference between that invariant response statistic and the canonical Hamiltonian.

**Sources.** [estimator §§1–3, Eqs. (4)–(8)](../science/estimator.md#1-a-measured-signal-with-one-preparation-and-one-readout-factor); [FST Theorem 31 proof, Eq. (117)][fst]; [bridge §5](rivas_huelga_bridge.md#5-reciprocal-measurements-and-the-error-law).

### M15. Exact recovery at the specified boundary

**Central question.** Why does a dissipative boundary restore the target Hamiltonian response?

**Understanding target.** When every allowed product-sector term has zero diagonal-rate product, use positivity to remove all corresponding cross coefficients. The oriented reciprocal block then returns $`h_C`$ in the ideal-data limit. Noise in other sectors can remain substantial.

**Dependencies and story role.** Uses M07–M08 and M14. It establishes the reference point from which the quantitative near-boundary result departs.

**Conceptual connection.** The condition $`\Delta_C=0`$ includes FST's sufficient boundary condition and its sparse-pattern version under promised structural zeros. It supplies a sufficient identifiable boundary, without classifying every boundary invariant.

**Sources.** [model §3](../science/model.md#3-the-relevant-noise-scale); [estimator §§2–3](../science/estimator.md#2-oriented-pauli-pairs-isolate-the-target-sector); [FST Theorem 31][fst]; [related work](../references/RELATED_WORK.md#the-closest-continuous-time-result).

### M16. Quantifying product-sector contamination

**Central question.** How much dissipative contamination is allowed away from that boundary?

**Understanding target.** Define the ordered sum $`\Delta_C=\sum_{(A,B)\in\mathcal I_d,\ A\star B=C}\sqrt{\alpha_{AA}\alpha_{BB}}`$. For $`a=(T_{QP}+T_{PQ})/4`$ and $`b=(T_{QP}-T_{PQ})/4`$, establish $`|a|\le\Delta_C`$ and $`|b-h_C|\le\Delta_C`$. Count both orders and exclude structurally forbidden pairs.

**Dependencies and story role.** Uses M07–M08 and M15. It replaces the exact-boundary vanishing statement with uniform inequalities.

**Conceptual connection.** The theorem uses the true diagonal rates as an error descriptor; the implemented estimator does not need their values in advance. The sector scale differs from the total dissipative strength.

**Sources.** [model §3, Eq. (4)](../science/model.md#3-the-relevant-noise-scale); [estimator §2, Eq. (7)](../science/estimator.md#2-oriented-pauli-pairs-isolate-the-target-sector).

### M17. The uniform reciprocal bias

**Central question.** Why is the residual bias quadratic for a resolved Hamiltonian signal and linear for a weak one?

**Understanding target.** Analyze $`\phi(b,a)=\mathrm{sgn}(b+a)\sqrt{[b^2-a^2]_+}`$ in both regimes and understand $`|\phi(b,a)-b|\le3\Delta_C^2/(|h_C|+\Delta_C)`$. Include the vanishing radicand and $`h_C=0`$ cases.

**Dependencies and story role.** Uses M14 and M16. It identifies the modulus that will survive the full reconstruction.

**Conceptual connection.** The comparison is with the block coefficient $`b`$. Canonical averaging must still remove the possible linear dissipative shift in $`b-h_C`$; this is why a single reciprocal block is insufficient in general.

**Sources.** [estimator §3, Lemma 1](../science/estimator.md#3-the-reciprocal-functional); [bridge §5](rivas_huelga_bridge.md#5-reciprocal-measurements-and-the-error-law); [interpretation §2](../science/interpretation.md#2-weak-and-resolved-interactions).

### M18. Finite-data stability at a singular square root

**Central question.** How can an estimator remain useful without a lower bound on the unknown coupling?

**Understanding target.** Understand baseline clipping using $`z_*=r_pr_m`$, the bounded imbalance of unknown gains, and the auxiliary perturbed coordinates used in the proof. Raw errors at most $`\tau`$ produce an additional error at most $`4\Lambda\tau`$ beyond the physical noise modulus, uniformly through zero slopes.

**Dependencies and story role.** Uses M10 and M14–M17. It converts an exact response identity into a statistically stable procedure.

**Conceptual connection.** A square root has no uniform Lipschitz constant on arbitrary noisy inputs. The physical inequalities and the Lipschitz dependence of $`\psi_h(\Delta)`$ on $`\Delta`$ supply the stability needed here, without a minimum nonzero $`h_C`$ or a calibrated gain ratio.

**Sources.** [estimator §4](../science/estimator.md#4-finite-data-stability-at-every-coupling-strength); [model §4](../science/model.md#4-simultaneous-learning-theorem).

### M19. Canonical averaging of response blocks

**Central question.** How does a collection of response blocks isolate the canonical Hamiltonian?

**Understanding target.** Understand the superoperator inner-product projection onto $`\mathcal K_C=-i[C,\cdot]`$. Its squared norm is $`2q^2`$ on a region of dimension $`q`$, and canonical dissipators with two traceless indices are orthogonal to it. Averaging the $`q^2/4`$ oriented unordered blocks gives the region's canonical coefficient.

**Dependencies and story role.** Uses M06, M08, and M17–M18. It removes the dissipative contribution that can remain in an individual antisymmetric block.

**Conceptual connection.** A canonical generator decomposition is made operational through a normalized projection. The averaging step is exact in the block coefficients; the reciprocal estimation errors are then bounded separately.

**Sources.** [local reconstruction §1, Lemma 1 and Eqs. (2)–(3)](../science/local_reconstruction.md#1-canonical-hamiltonian-projection); [estimator §5](../science/estimator.md#5-from-pair-estimates-to-the-hamiltonian).

### M20. What exterior spectators leave behind

**Central question.** Why can a correctly reconstructed local Hamiltonian still differ from the global target coefficient?

**Understanding target.** Interpret the instantaneous restriction $`\mathcal L_W(X)=2^{-|W^c|}\mathrm{Tr}_{W^c}[\mathcal L(X\otimes I)]`$. An exterior pair $`(V,CV)`$ can leave the shift $`\mathrm{Im}\alpha_{V,CV}`$ in the coefficient of $`C`$. Track its sign and the absence of an extra factor two.

**Dependencies and story role.** Uses M02, M05–M06, and M19. It identifies the remaining obstruction to using only local measured regions.

**Conceptual connection.** The restricted derivative has a well-defined canonical coefficient even though finite reduced dynamics need not equal $`e^{t\mathcal L_W}`$. Exterior dissipative labels can become identity labels locally and shift that coefficient.

**Sources.** [local reconstruction §2, Eqs. (4)–(7)](../science/local_reconstruction.md#2-what-a-local-region-actually-reveals); [RH §4.1 for reduced dynamics][rh].

### M21. Spectator cancellation within allowed patches

**Central question.** How can exterior shifts be removed without demanding stronger visibility on larger regions?

**Understanding target.** Use the known downward-closed spectator-support family, its inclusion–exclusion identity, and the coefficient-weight bound $`L_C\le1+\nu(3^{k-|\mathrm{supp}(C)|}-1)`$. For patches $`\{1,2,3\}`$ and $`\{1,2,4\}`$ with target $`Z_1Z_2`$, understand $`h_C=f(\{3\})+f(\{4\})-f(\varnothing)`$.

**Dependencies and story role.** Uses M09 and M18–M20. It joins block estimation and canonical projection into a global coefficient estimator.

**Conceptual connection.** Support information replaces an enlarged-neighborhood experiment. Every measured region remains inside one original patch, and the absolute reconstruction weights quantify error amplification.

**Sources.** [local reconstruction §§3–5](../science/local_reconstruction.md#3-a-support-formula-using-only-allowed-patches); [FST §5.1.1 for support elimination][fst]; [interpretation §4](../science/interpretation.md#4-why-local-correction-matters).

### M22. Derivatives from native short-time evolution

**Central question.** What justifies estimating a derivative from finite-time experimental signals?

**Understanding target.** Follow the growth of support in repeated local-generator applications and the bound $`\|(\mathcal L^\dagger)^nQ\|_\infty\le(Jk)^n n!`$. Understand the resulting analytic neighborhood and the fixed window $`T=1/(4\max\{1,Jk\})`$, independent of total system size.

**Dependencies and story role.** Uses M05, M09, and M13. It supplies the analytic input needed to realize the derivative estimates used in M18 and M21.

**Conceptual connection.** Locality controls a globally evolving observable at short times. The estimator does not receive a derivative oracle and does not require independent reduced dynamics.

**Sources.** [resources §1, Eqs. (1)–(3)](../science/resources.md#1-local-observables-have-a-uniform-analytic-neighborhood); [FST Appendix A, Eqs. (128)–(129)][fst]; [RH §§2.1–2.3 for operator norms and semigroups][rh].

### M23. Finite sampling and parallel resource costs

**Central question.** How are all required derivatives obtained at a stated physical cost?

**Understanding target.** Connect Chebyshev–Lobatto interpolation, the endpoint weight sum $`W_m=2m^2/T`$, analytic interpolation bias, and weighted bounded-outcome sampling. Understand why patch coloring gives a constant number of compatible global settings and why a union bound permits correlations among local outcomes within one repetition.

**Dependencies and story role.** Uses M09–M10, M18, M21, and M22. It converts the algebraic estimator into a finite experiment with a simultaneous guarantee.

**Conceptual connection.** Independent repetitions support concentration; independence between qubits is unnecessary. The logarithmic system-size factor coexists with $`O(N)`$ gates and measured bits per repetition, fixed-locality overheads, and timing precision that improves with the target accuracy.

**Sources.** [resources §§2–4](../science/resources.md#2-a-derivative-estimate-with-charged-repetitions); [FST Lemma 28][fst]; [model §4, Eq. (6)](../science/model.md#4-simultaneous-learning-theorem).

### M24. The complete achievable theorem

**Central question.** What guarantee follows after the experimental and reconstruction errors are combined?

**Understanding target.** Assemble the simultaneous inequality $`|\widehat h_C-h_C|\le\epsilon+3L_C\Delta_C^2/(|h_C|+\Delta_C)`$, with the fraction defined as zero at $`h_C=\Delta_C=0`$. Explain the choice $`\tau=\epsilon/(4\Lambda L_{\max})`$, the confidence $`1-\delta`$, and which fixed model parameters enter the repetition and time bounds.

**Dependencies and story role.** Integrates M13–M23 with the model fixed in M12. It closes the constructive branch of the narrative.

**Conceptual connection.** Reciprocal cancellation, uniform stability, canonical averaging, support subtraction, and finite sampling each solve a distinct obstruction. Their combination gives one estimator for all target coefficients without assuming a minimum interaction strength.

**Sources.** [model §4, Theorem 1](../science/model.md#4-simultaneous-learning-theorem); [local reconstruction §4](../science/local_reconstruction.md#4-the-reconstruction-has-bounded-amplification); [resources §3, Eq. (8)](../science/resources.md#3-parallel-local-settings).

### M25. A physical two-qubit ambiguity family

**Central question.** Which positive noise family can hide a change in a coherent interaction?

**Understanding target.** Read the full $`H=hZZ`$ construction: four active two-dimensional Kossakowski blocks with diagonal rates $`\Gamma,\eta`$ and cross entries $`\pm c/2`$. Understand the exact condition $`|c|\le2\sqrt{\Gamma\eta}`$, the signed Pauli response blocks, and the ordered count $`\Delta_{ZZ}=8\sqrt{\Gamma\eta}`$.

**Dependencies and story role.** Uses M06–M08, M11–M12, and M16. It opens the lower-bound branch with an explicit physical generator.

**Conceptual connection.** The positivity constraint used in the upper proof now supplies room for indistinguishable models. The four-pair Pauli sector is inherited from MCGS; the full quantitative family must also satisfy the project's continuous-time model.

**Sources.** [lower bound §§1–2, Eqs. (L1)–(L4)](../science/lower_bound.md#1-a-two-qubit-physical-family); [MCGS Result 1 and its following four-pair example][mcgs]; [related work](../references/RELATED_WORK.md#pauli-noise-symmetry-and-positivity).

### M26. A gauge absorbed by physical SPAM

**Central question.** Can a change in the interaction be absorbed while both experimental models remain physical?

**Understanding target.** Follow the support-depolarizing similarity and the hyperbolic mixing of $`h`$ and $`c`$, which preserves $`h^2-c^2`$. Verify why the gauge commutes with trusted product unitaries, why the transformed preparation and composed readout are physical, and how the chosen gauge size preserves the noise matrix's positivity margin.

**Dependencies and story role.** Uses M10–M11 and M25. It elevates an algebraic invariant to a pair of admissible physical models with the same diagonal rates.

**Conceptual connection.** Physicality must hold for the whole transformed experiment. An inverse map that is not completely positive can still yield a physical composed readout for the selected SPAM allowance.

**Sources.** [lower bound §§2–3 and §5, Eqs. (L5)–(L7) and (L10)–(L12)](../science/lower_bound.md#2-exact-pauli-blocks-and-the-gauge-transformation); [FST Proposition 10 and Theorem 18][fst]; [bridge §4](rivas_huelga_bridge.md#4-what-unknown-spam-changes).

### M27. Identical data imply an estimation lower bound

**Central question.** Why can no amount of allowed experimental data resolve this pair?

**Understanding target.** Follow gauge cancellation through arbitrary finite sequences of native evolution and product-unitary pulses, then through adaptive choices between repetitions. Equality of complete transcript laws implies that one of two models separated by $`g`$ has expected absolute error at least $`g/2`$; the corresponding probability obstruction also follows.

**Dependencies and story role.** Uses M12 and M25–M26. It turns a physical construction into an information-theoretic limitation for every allowed estimator.

**Conceptual connection.** Equality of one reciprocal statistic would be insufficient. Equality of the complete accessible distributions rules out improvements from more samples, different permitted pulses, or classical adaptation.

**Sources.** [lower bound §4, Eqs. (L8)–(L9)](../science/lower_bound.md#4-equality-for-every-allowed-controlled-experiment); [lower bound §6, Eqs. (L13)–(L14)](../science/lower_bound.md#6-estimation-lower-bound-and-matching-regimes); [FST Theorem 18 for the general obstruction][fst].

### M28. Matching regimes and the meaning of a noise rate

**Central question.** In what sense does the physical obstruction match the estimator's noise dependence?

**Understanding target.** Compare the upper modulus with the family's separation of order $`\Gamma\eta/(h+\sqrt{\Gamma\eta})`$. Distinguish weak signals, with ambiguity of order $`\sqrt{\Gamma\eta}`$, from resolved signals, with ambiguity of order $`\Gamma\eta/h`$. State that matching sharpness is worst-case over the allowed multi-qubit class.

**Dependencies and story role.** Uses M16–M17, M24, and M25–M27. It joins the constructive and impossibility branches quantitatively.

**Conceptual connection.** The weak parameter $`\eta`$ is a diagonal rate. Cross coefficients are already permitted at order $`\sqrt{\Gamma\eta}`$, so this square root is not an amplification relative to the norm of the complete dissipative perturbation.

**Sources.** [lower bound §§5–6](../science/lower_bound.md#5-a-quantitative-pair-with-a-uniform-positivity-margin); [model §§3 and 5](../science/model.md#5-matching-noise-dependence-and-its-quantifiers); [interpretation §2](../science/interpretation.md#2-weak-and-resolved-interactions).

### M29. Evidence and attribution

**Central question.** What supports the claim, and which parts come from prior research?

**Understanding target.** Distinguish analytical proofs from finite matrix checks, sampled controlled circuits, and binomial-count simulations. Interpret the demonstrated statistical spread, interpolation bias, and residual estimator bias separately; the largest reported reconstruction uses 880 million physical-shot equivalents despite compressed classical simulation. Locate the inherited FST primitives and gauge arguments, the MCGS sector, and the project's quantitative modulus.

**Dependencies and story role.** Uses M19–M28. It relates the mathematical result to its reproducible evidence and its scientific provenance.

**Conceptual connection.** Numerical checks can expose normalization and implementation errors; universal quantifiers come from the proofs. Accurate resource reporting and attribution are part of interpreting what the result establishes.

**Sources.** [verification guide](../verification/README.md), especially [finite-count reconstruction](../verification/README.md#finite-count-reconstruction); [lower bound §7](../science/lower_bound.md#7-reproducible-checks-and-their-extent); [related work](../references/RELATED_WORK.md); [interpretation §5](../science/interpretation.md#5-what-the-experiment-demonstrates).

### M30. Synthesis of the calibration capability and limit

**Central question.** What can be learned under this access model, what remains ambiguous, and why?

**Understanding target.** Give a connected account from canonical local dynamics and positive visibility to an implementable simultaneous estimator, its precision-dependent costs, and a physical indistinguishability family. Explain the exact-boundary limit and the weak-to-resolved crossover. Retain the scope: the lower bound is worst-case, single-qubit coefficients can be easier, additional calibrated access can change the obstruction, and the true-rate error inequality is not by itself an empirical confidence-radius procedure.

**Dependencies and story role.** Integrates M12 and M24–M29, supported by the component arguments in M13–M23. It closes the narrative with the full scientific claim and its limits.

**Conceptual connection.** Complete positivity both constrains the nuisance dynamics enough to permit learning and permits a physical calibration ambiguity of precisely the same order. Statistics determines how closely the protocol approaches that ambiguity scale.

**Sources.** [model, Theorem 1 and §5](../science/model.md); [interpretation](../science/interpretation.md); [related work, boundaries of the claim](../references/RELATED_WORK.md#boundaries-of-the-claim); [bridge §7](rivas_huelga_bridge.md#7-route-into-the-proofs).

[rh]: https://arxiv.org/html/1104.5242v2
[fst]: https://arxiv.org/html/2609.35265v1
[mcgs]: https://arxiv.org/abs/2607.02481v1
