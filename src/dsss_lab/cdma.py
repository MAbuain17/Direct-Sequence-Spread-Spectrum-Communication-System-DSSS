"""Symbol-synchronous direct-sequence CDMA with chip-phase offsets.

One unit-energy signature and one BPSK symbol are assigned to each user per
symbol interval. A chip-phase offset rotates a user's signature within that
interval; it does not model an asynchronous symbol boundary or multipath.
"""
from __future__ import annotations

import numpy as np

from .core import binary, bipolar, hardware_pn


def signatures(users: int, family: str = "walsh", chip_offset: int = 0) -> np.ndarray:
    """Return unit-energy signature rows, with user 0 as the desired user."""
    if not isinstance(users, (int, np.integer)) or not 1 <= users <= 16:
        raise ValueError("users must be an integer from 1 to 16")
    if not isinstance(chip_offset, (int, np.integer)):
        raise ValueError("chip_offset must be an integer")
    if family == "walsh":
        h = np.array([[1.0]])
        while len(h) < 32:
            h = np.block([[h, h], [h, -h]])
        order = [4, 5, 8, 9] + [i for i in range(1, 32) if i not in (4, 5, 8, 9)]
        codes = h[order[:users]].copy()  # Exclude the constant row.
    elif family == "pn_shift":
        pn = bipolar(hardware_pn(31)[0])
        codes = np.stack([np.roll(pn, 3 * k) for k in range(users)])
    else:
        raise ValueError("family must be 'walsh' or 'pn_shift'")
    if users > 1:
        codes[1:] = np.roll(codes[1:], int(chip_offset), axis=1)
    return codes / np.sqrt(codes.shape[1])


def transmit(bits: np.ndarray, codes: np.ndarray, power_db: np.ndarray | None = None) -> np.ndarray:
    """Sum user waveforms; power_db is per-user energy relative to user 0."""
    b = np.asarray(bits)
    c = np.asarray(codes, dtype=float)
    if b.ndim != 2 or c.ndim != 2 or b.shape[0] != c.shape[0]:
        raise ValueError("bits and signatures need the same user count")
    if not np.all((b == 0) | (b == 1)) or not np.allclose(np.sum(c*c, axis=1), 1):
        raise ValueError("binary bits and unit-energy signatures required")
    p = np.zeros(len(c)) if power_db is None else np.asarray(power_db, dtype=float)
    if p.shape != (len(c),) or not np.all(np.isfinite(p)):
        raise ValueError("one finite power value per user required")
    return (bipolar(b.ravel()).reshape(b.shape) * (10**(p/20))[:, None]).T @ c


def detect(rx: np.ndarray, codes: np.ndarray, method: str = "matched", ebn0_db: float = 10.,
           power_db: np.ndarray | None = None) -> tuple[np.ndarray, np.ndarray]:
    """Detect all users with matched, decorrelating, or linear MMSE filters."""
    c = np.asarray(codes, dtype=float)
    r = np.asarray(rx)
    if c.ndim != 2 or r.ndim != 2 or r.shape[1] != c.shape[1]:
        raise ValueError("expected symbols by chips and users by chips")
    gram = c @ c.T
    projection = r @ c.T
    if method == "matched":
        soft = projection
    elif method == "decorrelator":
        soft = np.linalg.solve(gram, projection.T).T
    elif method == "mmse":
        if not np.isfinite(ebn0_db):
            raise ValueError("finite Eb/N0 required for MMSE")
        p = np.zeros(len(c)) if power_db is None else np.asarray(power_db, dtype=float)
        if p.shape != (len(c),) or not np.all(np.isfinite(p)):
            raise ValueError("one finite power value per user required")
        n0_half = .5 * 10**(-ebn0_db/10)
        soft = np.linalg.solve(gram + np.diag(n0_half * 10**(-p/10)), projection.T).T
    else:
        raise ValueError("unknown detector")
    return (soft.real < 0).astype(np.uint8).T, soft.T


def trial(users=4, family="pn_shift", chip_offset=0, near_far_db=0., ebn0_db=8.,
          symbols=4000, method="matched", seed=20260927, jammer_db=None) -> dict:
    """Reproducible chip-rate Monte Carlo trial; BER refers to desired user 0."""
    if not isinstance(symbols, int) or symbols < 1:
        raise ValueError("symbols must be a positive integer")
    codes = signatures(users, family, chip_offset)
    rng = np.random.default_rng(seed)
    bits = rng.integers(0, 2, (users, symbols), dtype=np.uint8)
    powers = np.full(users, float(near_far_db)); powers[0] = 0.
    tx = transmit(bits, codes, powers)
    n0_half = .5 * 10**(-ebn0_db/10)
    rx = tx + rng.normal(0, np.sqrt(n0_half), tx.shape)
    if jammer_db is not None:
        phase = rng.uniform(0, 2*np.pi)
        chip = np.arange(rx.size)
        tone = np.sqrt(2*10**(jammer_db/10)/codes.shape[1]) * np.cos(2*np.pi*.073*chip + phase)
        rx += tone.reshape(rx.shape)
    decoded, soft = detect(rx, codes, method, ebn0_db, powers)
    errors = int(np.count_nonzero(bits[0] != decoded[0]))
    return dict(users=users, family=family, chip_offset=chip_offset,
                near_far_db=near_far_db, ebn0_db=ebn0_db, symbols=symbols,
                method=method, jammer_db=jammer_db, errors=errors,
                ber=errors/symbols, max_crosscorr=float(np.max(np.abs((codes@codes.T - np.eye(users))))))
