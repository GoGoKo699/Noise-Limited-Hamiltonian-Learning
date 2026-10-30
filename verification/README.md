# Reproduce the finite checks

The proofs establish the general guarantees. This suite checks matrix conventions, the explicit indistinguishable family, the nontrivial local reconstruction, and finite-count behavior of the estimator.

With Python 3.12 and the pinned numerical dependencies, run from the repository root:

```bash
python3 -m pip install -r verification/requirements.txt
python3 verification/run_all.py
```

The command raises an error and exits nonzero if a stated check fails. It prints a compact summary and does not overwrite the committed reference. To retain a fresh detailed report at a chosen path:

```bash
python3 verification/run_all.py --output /tmp/noise-limited-hamiltonian-checks.json
```

The [recorded result](expected/results.json) contains the numerical values, parameter grids, random seeds, all finite-count estimates, and the Python/NumPy/SciPy versions of the recorded run. Different floating-point environments can change the last digits. The command validates the stated analytical conditions with explicit tolerances; it does not require byte-for-byte agreement with the historical report.

## What is checked

| Check | Independent calculation or failure mode addressed |
|---|---|
| Canonical projection | A dense complex positive Kossakowski matrix and all 15 two-qubit Hamiltonian targets. Direct Lindblad matrix action, Pauli-block averages, and a separate left/right superoperator projection must recover the same canonical coefficients. |
| Physical lower family | The direct matrix generator must agree with all four analytic blocks, the complete gauge similarity, the positive Kossakowski spectrum, and the quantitative Hamiltonian-separation bound. |
| Controlled experiments | All four final computational-basis probabilities agree after sampled sequences of product-unitary pulses and evolution times, using the explicit transformed preparation/readout channels. |
| Exterior spectators | A four-qubit model with allowed patches $`123`$ and $`124`$ tests imaginary spectator contributions and their cancellation using probes of weight at most three. |
| Uniform reciprocal stability | 42,000 specified combinations include positive/negative/zero target coefficients, the singular product surface, zero leakage, gain imbalance, and additive coordinate errors. |
| Finite observations | Exact binomial signed-parity counts, empirical zero-time calibration factors, Chebyshev derivative estimates, and the full reciprocal estimator. The estimator receives neither exact slopes nor exact SPAM gains. |

The controlled-circuit check is finite. The [similarity proof](../science/lower_bound.md#4-equality-for-every-allowed-controlled-experiment) supplies equality for every permitted sequence and every finite adaptive data protocol. Likewise, the stability grid does not replace the [uniform analytical bound](../science/estimator.md).

## Matrix and spectator results

The recorded canonical block projection differs from the supplied Hamiltonian coefficients by at most $`5.56\times10^{-17}`$. The full lower-family similarity differs by at most $`2.23\times10^{-16}`$, and the sampled controlled readout probabilities differ by at most $`5.56\times10^{-17}`$. Small negative computed eigenvalues at floating-point scale are checked against the $`10^{-11}`$ tolerance; physicality is established analytically by the positive $`2\times2`$ blocks.

The spectator model has target $`H=0.2\,ZZII`$ and two imaginary Kossakowski pairs,

```math
(IIXI,ZZXI),\qquad(IIIY,ZZIY).
```

Their separate shifts are of order $`\sqrt\eta`$. The canonical patch values obey

```math
h=f(\{3\})+f(\{4\})-f(\varnothing)
```

to floating-point precision. After replacing each canonical block by its reciprocal estimate, the reconstructed bias is:

| Weak diagonal rate $`\eta`$ | Absolute bias | Bias divided by $`\eta`$ |
|---:|---:|---:|
| $`10^{-2}`$ | $`1.24907\times10^{-3}`$ | $`0.124907`$ |
| $`10^{-3}`$ | $`1.22734\times10^{-4}`$ | $`0.122734`$ |
| $`10^{-4}`$ | $`1.22523\times10^{-5}`$ | $`0.122523`$ |
| $`10^{-5}`$ | $`1.22502\times10^{-6}`$ | $`0.122502`$ |

This example tests the cancellation needed for the strong-interaction rate: an uncancelled spectator shift would scale as $`\sqrt\eta`$ instead.

## Finite-count reconstruction

The two-qubit simulation uses

```math
h=0.3,\qquad c=0.045,\qquad
\Gamma=0.03,\qquad\eta=0.02.
```

The physicality condition $`|c|\le2\sqrt{\Gamma\eta}`$ holds. Preparation and readout have unknown depolarizing multipliers $`0.9`$ and $`0.85`$. Their values determine the simulated data distribution but are not supplied to the estimator. The algorithm estimates its two zero-time factors from separate counts and clips them at $`0.125`$, consistent with the declared preparation/readout visibility bounds $`r_p=r_m=0.5`$.

The derivative estimator interpolates degree-five polynomials at six Chebyshev–Lobatto times in $`[0,1.5]`$. This fixed two-qubit example uses an interval whose interpolation bias is computed directly; the general theorem chooses an interval from its locality and strength bounds. For a cross response, $`F_{QP}(0)=0`$ is an exact identity for distinct Pauli labels, so this endpoint requires no cross-response samples. All five other times are sampled, with counts allocated in proportion to the absolute differentiation weights. Every baseline count is included in the total cost.

For each randomized experiment, the character-corrected parity is a $`\pm1`$ variable with mean

```math
F_{QP}(t)=m_{\mathrm{supp}Q}s_{\mathrm{supp}P}
\frac{\mathrm{Tr}[Qe^{t\mathcal L}(P)]}{4}.
```

The code samples the resulting binomial count directly. This is the exact distribution of the aggregated signed observations after averaging the independently randomized Pauli pulses and physical readout outcomes. It compresses their simulation; it does not supply a noiseless expectation or use Gaussian surrogate observations.

All four reciprocal Pauli blocks are reconstructed independently and averaged. The infinite-data value is

```math
h_{\mathrm{rec}}=\sqrt{h^2-c^2}
=0.2966057989992778.
```

Its physical bias is approximately $`0.0033942010`$. The chosen polynomial interpolation adds a deterministic bias of approximately $`-3.9253\times10^{-6}`$, reported separately. Each row below uses all 32 fixed seeds $`0,\ldots,31`$; the detailed report includes every estimate, including the less accurate small-budget reconstructions.

| Total shots per reconstruction | Mean estimate | RMSE relative to $`h_{\mathrm{rec}}`$ | RMSE relative to true $`h`$ |
|---:|---:|---:|---:|
| 88,000 | 0.263119 | 0.062540 | 0.064421 |
| 880,000 | 0.292794 | 0.016128 | 0.017249 |
| 8,800,000 | 0.294921 | 0.006330 | 0.007939 |
| 88,000,000 | 0.296547 | 0.002177 | 0.004081 |
| 880,000,000 | 0.296605 | 0.000570 | 0.003442 |

The statistical spread contracts around the reciprocal invariant while the error relative to the true coupling approaches a nonzero value. The [lower-bound construction](../science/lower_bound.md) explains why a uniformly valid method cannot remove the corresponding ambiguity over the model class.

These are large paid sample budgets. The largest row uses 880 million physical-shot equivalents **per reconstruction**, and its total native evolution time is approximately $`3.273\times10^8`$ in the normalized time units. The 32 simulated reconstructions are independent repeats of that budget. Binomial aggregation makes this a small computation, but does not reduce the physical resource count. This experiment checks the mechanism; it is not a hardware crossover or a practical resource advantage demonstration.

## Scope and file map

### Reproduce the scientific figure

The [two-panel figure](../science/figures/calibration_modulus.svg) plots the derived modulus and the already-recorded finite-count data. Its horizontal bias line is the specified reciprocal estimator's infinite-data bias, rather than an exact minimax constant. Figure generation does not run new simulations and is optional for the core verification suite:

```bash
python3 -m pip install -r verification/requirements-plot.txt
python3 verification/plot_results.py
```

The script saves an SVG and a 200-dpi PNG under `science/figures/`. Both carry the input report's SHA256 in their metadata. The [PNG](../science/figures/calibration_modulus.png) is convenient for raster previews; the SVG preserves scaling for publication or presentation. The figure was visually checked for axis labels, legend, regime annotations, and unclipped mathematical text.

### Files

- [pauli.py](pauli.py) contains the direct matrix generator and independent representation conversions.
- [checks.py](checks.py) contains the specified instances, deterministic acceptance conditions, and observation simulation.
- [run_all.py](run_all.py) runs the checks and optionally writes a fresh report.
- [requirements.txt](requirements.txt) pins the numerical libraries used for the recorded result.
- [plot_results.py](plot_results.py) regenerates the scientific figure with the optional [plotting requirements](requirements-plot.txt).
- [expected/results.json](expected/results.json) preserves the actual reference output.

The suite does not certify every analytic proof, exhaustive novelty, arbitrary control errors, or optimally narrow confidence intervals inferred from data. The theorem is an error guarantee in the true diagonal dissipative rates. The uniform proof, model assumptions, and full resource statement remain authoritative for claims beyond these finite checks.
