import unittest
import numpy as np

from dsss_lab.cdma import signatures, transmit, detect, trial


class CDMATests(unittest.TestCase):
    def test_walsh_orthogonality_and_power(self):
        c = signatures(8, "walsh")
        np.testing.assert_allclose(c @ c.T, np.eye(8), atol=1e-14)
        b = np.zeros((8, 3), dtype=np.uint8)
        self.assertEqual(transmit(b, c).shape, (3, 32))

    def test_code_phase_changes_crosscorrelation(self):
        aligned = signatures(4, "walsh", 0)
        offset = signatures(4, "walsh", 1)
        self.assertAlmostEqual(float((aligned @ aligned.T)[0, 1]), 0.)
        self.assertGreater(float(np.max(np.abs(offset @ offset.T - np.eye(4)))), 0.)

    def test_noiseless_multiuser_recovery(self):
        rng = np.random.default_rng(19)
        b = rng.integers(0, 2, (4, 100), dtype=np.uint8)
        c = signatures(4, "pn_shift", 2)
        x = transmit(b, c, [0, 12, 12, 12])
        for mode in ("decorrelator", "mmse"):
            out, _ = detect(x, c, mode, 100)
            np.testing.assert_array_equal(out, b)

    def test_near_far_decorrelator(self):
        args = dict(users=4, family="pn_shift", chip_offset=2,
                    near_far_db=18, ebn0_db=12, symbols=2000, seed=9)
        matched = trial(**args, method="matched")
        decorrelated = trial(**args, method="decorrelator")
        mmse = trial(**args, method="mmse")
        self.assertGreater(matched["errors"], decorrelated["errors"])
        self.assertLess(mmse["errors"], matched["errors"])

    def test_bad_inputs(self):
        with self.assertRaises(ValueError): signatures(17)
        with self.assertRaises(ValueError): signatures(2, "unknown")
        with self.assertRaises(ValueError): detect(np.zeros((2, 7)), signatures(2))


if __name__ == "__main__":
    unittest.main()
