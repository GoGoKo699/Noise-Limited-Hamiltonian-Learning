"""Checks chosen for the proof's consequential algebraic/statistical boundaries."""
import numpy as np
from scipy.linalg import expm

from pauli import PauliBasis, lower_family, signed_root


def require(condition, message):
    if not condition:
        raise AssertionError(message)


def check_canonical_projection():
    basis = PauliBasis(2)
    rng = np.random.default_rng(17429)
    z = rng.normal(size=(15, 15)) + 1j * rng.normal(size=(15, 15))
    a = np.zeros((16, 16), dtype=complex)
    a[1:, 1:] = z @ z.conj().T / 1000
    h = np.r_[0.0, rng.uniform(-0.3, 0.3, size=15)]
    transfer = basis.generator(np.einsum("a,aij->ij", h, basis.matrices), a)
    chi_h = basis.canonical_h_from_chi(transfer)
    errors, leakage_excess = [], []
    for ic, target in enumerate(basis.labels[1:], 1):
        blocks = basis.reciprocal_blocks(transfer, target)
        average = np.mean([row[4] for row in blocks])
        errors.append(abs(average - h[ic]))
        delta = 0.0
        for ia in range(1, 16):
            ib, _ = basis.identify(basis.matrices[ia] @ basis.matrices[ic])
            if ib:
                delta += np.sqrt(a[ia, ia].real * a[ib, ib].real)
        for row in blocks:
            leakage_excess.extend((abs(row[3]) - delta, abs(row[4] - h[ic]) - delta))
    result = {
        "targets_checked": 15,
        "block_average_max_error": float(max(errors)),
        "independent_chi_projection_max_error": float(np.max(abs(chi_h - h))),
        "trace_preservation_max_error": float(np.max(abs(transfer[0, :]))),
        "sector_bound_max_excess": float(max(leakage_excess)),
        "kossakowski_min_eigenvalue": float(np.linalg.eigvalsh(a[1:, 1:]).min()),
    }
    require(max(errors) < 1e-11, "Canonical block projection failed")
    require(result["independent_chi_projection_max_error"] < 1e-11, "Independent chi projection failed")
    require(result["trace_preservation_max_error"] < 1e-11, "Trace preservation failed")
    require(max(leakage_excess) < 1e-11, "PSD sector bound failed")
    return result


def check_lower_family():
    basis = PauliBasis(2)
    rng = np.random.default_rng(73915)
    diagonal_weights = basis.weights
    max_boost = max_probability = max_block = max_commutator = 0.0
    min_eigenvalue = 1.0
    rows = []
    pairs = (("IX", "ZY", 1), ("IY", "ZX", -1),
             ("XI", "YZ", 1), ("YI", "XZ", -1))
    for eta in (1e-2, 1e-4, 1e-6):
        gamma = 0.2
        r = 2 * np.sqrt(gamma * eta)
        for h in (0.0, r, 0.2):
            c = r / 2
            theta = r / (4 * (h + r))
            hp = h * np.cosh(theta) + c * np.sinh(theta)
            cp = c * np.cosh(theta) + h * np.sinh(theta)
            a, t = lower_family(basis, h, c, gamma, eta)
            ap, tp = lower_family(basis, hp, cp, gamma, eta)
            scale = np.exp(-theta * diagonal_weights)
            max_boost = max(max_boost, float(np.max(abs(tp - scale[:, None] * t / scale[None, :]))))
            min_eigenvalue = min(min_eigenvalue, float(np.linalg.eigvalsh(a[1:, 1:]).min()),
                                float(np.linalg.eigvalsh(ap[1:, 1:]).min()))
            for p, q, sign in pairs:
                ip, iq = basis.index[p], basis.index[q]
                actual = np.array([[t[ip, ip], sign * t[ip, iq]],
                                   [sign * t[iq, ip], t[iq, iq]]])
                formula = np.array([[-2 * gamma - 6 * eta, -2 * (h + c)],
                                    [2 * (h - c), -6 * gamma - 2 * eta]])
                max_block = max(max_block, float(np.max(abs(actual - formula))))
            lam = np.exp(-2.0)
            prep = np.array([lam**weight if set(label) <= set("IZ") else 0.0
                             for label, weight in zip(basis.labels, diagonal_weights)])
            for _ in range(4):
                state, state_prime = prep.copy(), scale * prep
                for _ in range(4):
                    pulse = basis.local_unitary_transfer(rng)
                    max_commutator = max(max_commutator,
                        float(np.max(abs(pulse * scale[None, :] - scale[:, None] * pulse))))
                    time = rng.uniform(0.0, 2.0)
                    state = expm(time * t) @ pulse @ state
                    state_prime = expm(time * tp) @ pulse @ state_prime
                out = lam**diagonal_weights * state
                out_prime = lam**diagonal_weights / scale * state_prime
                for z1, z2 in ((1, 1), (1, -1), (-1, 1), (-1, -1)):
                    def probability(vector):
                        return (vector[0] + z1 * vector[basis.index["ZI"]]
                                + z2 * vector[basis.index["IZ"]]
                                + z1 * z2 * vector[basis.index["ZZ"]]) / 4
                    max_probability = max(max_probability, abs(probability(out) - probability(out_prime)))
                    require(-1e-12 <= probability(out) <= 1 + 1e-12, "Invalid readout probability")
            gap_bound = r * r / (8 * (h + r))
            require(hp - h >= gap_bound - 1e-14, "Explicit Hamiltonian gap bound failed")
            require(cp <= 0.75 * r * np.cosh(0.25) + 1e-14, "Transformed PSD margin failed")
            rows.append({"gamma": gamma, "eta": eta, "h": h, "c": c,
                         "theta": theta, "h_prime": hp, "c_prime": cp,
                         "separation": hp - h, "separation_lower_bound": gap_bound,
                         "ordered_delta": 8 * np.sqrt(gamma * eta)})
    require(max_boost < 1e-11 and max_block < 1e-11, "Explicit lower-family algebra failed")
    require(min_eigenvalue > -1e-11, "A lower-family generator is not physical")
    require(max_probability < 1e-11 and max_commutator < 1e-11, "Controlled gauge equivalence failed")
    return {"analytic_block_max_error": max_block, "gauge_boost_max_error": max_boost,
            "local_control_commutator_max_error": max_commutator,
            "controlled_probability_max_error": float(max_probability),
            "kossakowski_min_eigenvalue": min_eigenvalue, "instances": rows}


def check_spectator_reconstruction():
    basis, small = PauliBasis(4), PauliBasis(2)
    h, gamma = 0.2, 0.1
    rows = []
    for eta in (1e-2, 1e-3, 1e-4, 1e-5):
        a = np.zeros((256, 256), dtype=complex)
        a2, _ = lower_family(small, h, 0.7 * np.sqrt(gamma * eta), gamma, eta)
        for i, j in zip(*np.nonzero(a2)):
            a[basis.index[small.labels[i] + "II"], basis.index[small.labels[j] + "II"]] = a2[i, j]
        beta3, beta4 = 0.5 * np.sqrt(gamma * eta), -0.3 * np.sqrt(gamma * eta)
        for left, right, beta in (("IIXI", "ZZXI", beta3), ("IIIY", "ZZIY", beta4)):
            i, j = basis.index[left], basis.index[right]
            a[i, i], a[j, j], a[i, j], a[j, i] = gamma, eta, 1j * beta, -1j * beta
        transfer = basis.generator(h * basis.matrices[basis.index["ZZII"]], a)
        f, reciprocal = [], []
        for region in ({0, 1}, {0, 1, 2}, {0, 1, 3}):
            blocks = basis.reciprocal_blocks(transfer, "ZZII", region)
            f.append(float(np.mean([row[4] for row in blocks])))
            reciprocal.append(float(np.mean([row[5] for row in blocks])))
        theoretical_f = [h + beta3 + beta4, h + beta4, h + beta3]
        require(np.max(abs(np.array(f) - theoretical_f)) < 1e-11, "Spectator shift formula failed")
        reconstructed = f[1] + f[2] - f[0]
        estimate = reciprocal[1] + reciprocal[2] - reciprocal[0]
        require(abs(reconstructed - h) < 1e-11, "Original-locality support reconstruction failed")
        active = np.flatnonzero(np.diag(a).real)
        require(np.linalg.eigvalsh(a[np.ix_(active, active)]).min() > -1e-11, "Spectator model not PSD")
        rows.append({"eta": eta, "h": h, "spectator3_shift": beta3,
                     "spectator4_shift": beta4, "local_canonical_coefficients": f,
                     "reconstructed_canonical_h": reconstructed,
                     "reciprocal_reconstruction": estimate,
                     "absolute_bias": abs(estimate - h), "bias_over_eta": abs(estimate - h) / eta})
    require(rows[-1]["absolute_bias"] < rows[0]["absolute_bias"] / 900,
            "Strong-signal cancellation did not persist across the specified weak-rate range")
    return {"allowed_patches": [[1, 2, 3], [1, 2, 4]], "largest_probe_weight": 3,
            "target": "ZZII", "instances": rows}


def check_uniform_stability():
    max_ideal_excess = max_noisy_excess = -np.inf
    cases = 0
    for h in (-1.0, -0.1, -1e-8, 0.0, 1e-8, 0.1, 1.0):
        for delta in (0.0, 1e-8, 1e-3, 0.1, 1.0):
            oracle = delta * delta / (abs(h) + delta) if abs(h) + delta else 0.0
            for u in (-1.0, -0.5, 0.0, 0.5, 1.0):
                for v in (-1.0, -0.5, 0.0, 0.5, 1.0):
                    b, a = h + u * delta, v * delta
                    phi = signed_root(b + a, b - a)
                    max_ideal_excess = max(max_ideal_excess, abs(phi - b) - 3 * oracle)
                    for kappa in (0.25, 1.0, 4.0):
                        x, y = kappa * (b + a), (b - a) / kappa
                        for tau in (0.0, 1e-9, 1e-4, 0.03):
                            perturbation_bound = (kappa + 1 / kappa) * tau / 2
                            for sx, sy in ((1, 1), (1, -1), (-1, 1), (-1, -1)):
                                estimate = signed_root(x + sx * tau, y + sy * tau)
                                excess = abs(estimate - b) - 3 * oracle - 4 * perturbation_bound
                                max_noisy_excess = max(max_noisy_excess, excess)
                                cases += 1
    require(max_ideal_excess < 2e-10 and max_noisy_excess < 2e-10,
            "Uniform reciprocal stability bound failed on the specified grid")
    return {"cases": cases, "includes_zero_and_sign_boundaries": True,
            "ideal_bound_max_excess": float(max_ideal_excess),
            "noisy_bound_max_excess": float(max_noisy_excess)}


def chebyshev_derivative_design(degree, window):
    x = -np.cos(np.pi * np.arange(degree + 1) / degree)
    times = (x + 1) * window / 2
    design = np.polynomial.chebyshev.chebvander(x, degree)
    derivative = np.array([0.0] + [(-1.0)**(k - 1) * k * k * 2 / window
                                  for k in range(1, degree + 1)])
    weights = np.linalg.solve(design.T, derivative)
    return times, weights


def check_finite_shots():
    """Exact binomial aggregation of physical signed-parity observations.

    Each randomized experiment's recorded statistic is +/-1 with mean F_QP(t).
    Its count distribution is therefore binomial, including the random Pauli
    choices and noisy quantum outcomes. No Gaussian observations or exact
    derivative samples are supplied to the estimator.
    """
    basis = PauliBasis(2)
    h, c, gamma, eta = 0.3, 0.045, 0.03, 0.02
    preparation, measurement = 0.9, 0.85
    degree, window, seeds = 5, 1.5, list(range(32))
    times, weights = chebyshev_derivative_design(degree, window)
    a, transfer = lower_family(basis, h, c, gamma, eta)
    require(np.linalg.eigvalsh(a[1:, 1:]).min() > -1e-12, "Finite-shot model not physical")
    pairs = (("IX", "ZY", 1), ("IY", "ZX", -1),
             ("XI", "YZ", 1), ("YI", "XZ", -1))
    evolutions = [expm(t * transfer) for t in times]
    forward_curves, backward_curves = [], []
    for p, q, sign in pairs:
        ip, iq = basis.index[p], basis.index[q]
        forward_curves.append(np.array([sign * e[iq, ip] * preparation * measurement**2 for e in evolutions]))
        backward_curves.append(np.array([sign * e[ip, iq] * preparation**2 * measurement for e in evolutions]))
    zp, zq = preparation * measurement, (preparation * measurement)**2
    exact_reciprocal = np.sqrt(h * h - c * c)
    interpolated = np.mean([
        0.5 * signed_root(np.dot(weights, f), -np.dot(weights, r)) / np.sqrt(zp * zq)
        for f, r in zip(forward_curves, backward_curves)
    ])
    require(abs(interpolated - exact_reciprocal) < 5e-6, "Chosen derivative interpolation bias exceeds stated tolerance")
    rows = []
    for budget in (10_000, 100_000, 1_000_000, 10_000_000, 100_000_000):
        # F_QP(0)=0 for distinct Pauli labels is known exactly, so t=0
        # needs no cross-response shots. All other counts are explicitly paid.
        allocation = np.floor(budget * abs(weights[1:]) / sum(abs(weights[1:]))).astype(np.int64)
        allocation[-1] += budget - int(allocation.sum())
        baseline_count = budget // 10
        estimates, clipped_baselines = [], 0
        for seed in seeds:
            rng = np.random.default_rng(102_401 + 1009 * seed + budget)
            blocks = []
            for forward, backward in zip(forward_curves, backward_curves):
                fhat = 2 * rng.binomial(allocation, (1 + forward[1:]) / 2) / allocation - 1
                rhat = 2 * rng.binomial(allocation, (1 + backward[1:]) / 2) / allocation - 1
                dforward, dbackward = weights[1:] @ fhat, weights[1:] @ rhat
                zphat = 2 * rng.binomial(baseline_count, (1 + zp) / 2) / baseline_count - 1
                zqhat = 2 * rng.binomial(baseline_count, (1 + zq) / 2) / baseline_count - 1
                clipped_baselines += int(zphat < 0.125) + int(zqhat < 0.125)
                zphat, zqhat = max(zphat, 0.125), max(zqhat, 0.125)
                blocks.append(0.5 * signed_root(dforward, -dbackward) / np.sqrt(zphat * zqhat))
            estimates.append(float(np.mean(blocks)))
        values = np.asarray(estimates)
        rows.append({
            "shots_per_cross_curve": budget, "cross_curve_shots_by_time": allocation.tolist(),
            "shots_per_zero_time_baseline": baseline_count,
            "total_shots_per_repetition": int(8 * budget + 8 * baseline_count),
            "total_native_evolution_time_per_repetition": float(8 * np.dot(allocation, times[1:])),
            "sampled_repetitions": len(seeds), "mean_estimate": float(np.mean(values)),
            "standard_deviation": float(np.std(values, ddof=1)),
            "median_absolute_error_to_h": float(np.median(abs(values - h))),
            "rmse_to_h": float(np.sqrt(np.mean((values - h)**2))),
            "rmse_to_infinite_data_estimator": float(np.sqrt(np.mean((values - exact_reciprocal)**2))),
            "clipped_baselines": clipped_baselines, "estimates": estimates,
        })
    require(rows[-1]["rmse_to_infinite_data_estimator"] < rows[0]["rmse_to_infinite_data_estimator"] / 20,
            "The finite-shot demonstration did not resolve its infinite-data estimator")
    return {
        "model": {"h": h, "c": c, "gamma": gamma, "eta": eta,
                  "preparation_depolarizing_multiplier": preparation,
                  "measurement_depolarizing_multiplier": measurement},
        "method": "Independent signed-parity binomial counts at Chebyshev-Lobatto times; empirical zero-time baselines; four reciprocal blocks",
        "polynomial_degree": degree, "time_window": window, "times": times.tolist(),
        "derivative_weights": weights.tolist(), "fixed_seeds": seeds,
        "infinite_data_estimator": float(exact_reciprocal),
        "irreducible_estimator_bias": float(h - exact_reciprocal),
        "interpolation_bias": float(interpolated - exact_reciprocal),
        "data_dependent_confidence_interval_claimed": False,
        "results": rows,
    }
