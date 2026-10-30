"""Small-system matrix algebra used by the scientific verification.

The generator is assembled directly from its Hamiltonian and Kossakowski
matrix. Pauli transfer and left/right (chi) representations are computed
independently so that their agreement is a check, rather than a definition.
"""
from itertools import product
import numpy as np
from scipy.linalg import expm


SINGLE = {
    "I": np.eye(2, dtype=complex),
    "X": np.array([[0, 1], [1, 0]], dtype=complex),
    "Y": np.array([[0, -1j], [1j, 0]], dtype=complex),
    "Z": np.diag([1.0, -1.0]).astype(complex),
}


class PauliBasis:
    def __init__(self, n):
        self.n = n
        self.dimension = 2**n
        self.labels = ["".join(x) for x in product("IXYZ", repeat=n)]
        self.index = {label: i for i, label in enumerate(self.labels)}
        matrices = []
        for label in self.labels:
            matrix = np.array([[1.0]], dtype=complex)
            for p in label:
                matrix = np.kron(matrix, SINGLE[p])
            matrices.append(matrix)
        self.matrices = np.asarray(matrices)
        self.weights = np.array([sum(p != "I" for p in s) for s in self.labels])

    def identify(self, matrix):
        overlaps = np.einsum("aij,ji->a", self.matrices, matrix) / self.dimension
        index = int(np.argmax(abs(overlaps)))
        if abs(abs(overlaps[index]) - 1) > 1e-10:
            raise ValueError("The matrix is not a phase times a Pauli operator")
        return index, overlaps[index]

    def generator(self, hamiltonian, kossakowski):
        """PTM T[row,column]=Tr(P_row L(P_column))/dimension."""
        a = np.asarray(kossakowski)
        if a.shape != (len(self.labels), len(self.labels)):
            raise ValueError("Kossakowski matrix includes a zero identity row/column")
        if np.max(abs(a[0, :])) > 1e-14 or np.max(abs(a[:, 0])) > 1e-14:
            raise ValueError("Canonical dissipative labels must be traceless")
        active = list(zip(*np.nonzero(a)))
        columns = []
        for p in self.matrices:
            lp = -1j * (hamiltonian @ p - p @ hamiltonian)
            for ia, ib in active:
                left, right = self.matrices[ia], self.matrices[ib]
                rp = right @ left
                lp += a[ia, ib] * (left @ p @ right - (rp @ p + p @ rp) / 2)
            coefficients = np.einsum("aij,ji->a", self.matrices, lp) / self.dimension
            if np.max(abs(coefficients.imag)) > 2e-11:
                raise AssertionError("Generator is not Hermiticity preserving")
            columns.append(coefficients.real)
        return np.asarray(columns).T

    def canonical_h_from_chi(self, transfer):
        """Independent left/right superoperator projection; intended for n<=2."""
        d = self.dimension
        change = np.array([p.reshape(-1, order="F") for p in self.matrices]).T
        superoperator = change @ transfer @ change.conj().T / d
        return np.array([
            np.vdot(np.kron(p.T, self.matrices[0]), superoperator).imag / d**2
            for p in self.matrices
        ])

    def reciprocal_blocks(self, transfer, target, region=None):
        """Return oriented (P,Q,sign,a,b,reciprocal) blocks for Q=-iCP."""
        c = self.matrices[self.index[target]]
        region = set(range(self.n)) if region is None else set(region)
        eligible = {i for i, label in enumerate(self.labels)
                    if all(label[j] == "I" for j in range(self.n) if j not in region)}
        visited, blocks = set(), []
        for ip in sorted(eligible):
            if ip in visited:
                continue
            p = self.matrices[ip]
            if np.linalg.norm(c @ p + p @ c) > 1e-10:
                continue
            iq, phase = self.identify(-1j * c @ p)
            sign = float(phase.real)
            if iq not in eligible or abs(phase.imag) > 1e-12:
                raise AssertionError("Oriented pair left the intended local patch")
            forward = sign * transfer[iq, ip]
            backward = sign * transfer[ip, iq]
            a, b = (forward + backward) / 4, (forward - backward) / 4
            reciprocal = np.sign(forward) * np.sqrt(max(0.0, -forward * backward)) / 2
            blocks.append((ip, iq, sign, a, b, reciprocal))
            visited.update((ip, iq))
        expected = 4**len(region) // 4
        if len(blocks) != expected:
            raise AssertionError(f"Expected {expected} blocks, obtained {len(blocks)}")
        return blocks

    def local_unitary_transfer(self, rng):
        u = np.array([[1.0]], dtype=complex)
        for _ in range(self.n):
            axis = rng.normal(size=3)
            axis /= np.linalg.norm(axis)
            generator = sum(x * SINGLE[p] for x, p in zip(axis, "XYZ"))
            u = np.kron(u, expm(-1j * rng.uniform(-2, 2) * generator))
        return np.array([
            [np.trace(p @ u @ q @ u.conj().T).real / self.dimension
             for q in self.matrices] for p in self.matrices
        ])


def lower_family(basis, h, c, gamma, eta):
    if basis.n != 2:
        raise ValueError("The explicit lower family has two qubits")
    a = np.zeros((16, 16), dtype=complex)
    for label in ("IX", "IY", "XI", "YI"):
        a[basis.index[label], basis.index[label]] = gamma
    for label in ("ZY", "ZX", "YZ", "XZ"):
        a[basis.index[label], basis.index[label]] = eta
    for left, right, sign in (("IX", "ZY", -1), ("XI", "YZ", -1),
                              ("IY", "ZX", 1), ("XZ", "YI", 1)):
        i, j = basis.index[left], basis.index[right]
        a[i, j] = a[j, i] = sign * c / 2
    return a, basis.generator(h * basis.matrices[basis.index["ZZ"]], a)


def signed_root(x, y):
    return np.sign(x) * np.sqrt(np.maximum(0.0, x * y))
