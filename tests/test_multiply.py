import unittest
import sys
sys.path.append('/mnt/batch/tasks/shared/LS_root/mounts/clusters/majid-bahre-secondcom/code/Users/Majid.Bahrepour/Test-automations-project')
from multiply import multiply

class TestMultiply(unittest.TestCase):
    def test_multiply_positive_integers(self):
        result = multiply(3, 5)
        self.assertEqual(result, 15)

    def test_multiply_by_zero(self):
        result = multiply(8, 0)
        self.assertEqual(result, 8)

    def test_multiply_positive_and_negative_integers(self):
        result = multiply(4, -2)
        self.assertEqual(result, -8)

    def test_multiply_negative_integers(self):
        result = multiply(-3, -7)
        self.assertEqual(result, 21)

    def test_multiply_floats(self):
        result = multiply(2.5, 4.2)
        self.assertAlmostEqual(result, 10.5)

if __name__ == '__main__':
    unittest.main()