from main import is_prime
import unittest


class TestStringMethods(unittest.TestCase):

    def test_is_prime(self):
        self.assertTrue(is_prime(2))
        self.assertTrue(is_prime(73))
        self.assertTrue(is_prime(41))
        self.assertTrue(is_prime(113))
        self.assertTrue(is_prime(5099))

    def test_is_not_prime(self):
        self.assertFalse(is_prime(1))
        self.assertFalse(is_prime(-1))
        self.assertFalse(is_prime(0))
        self.assertFalse(is_prime(75))
        self.assertFalse(is_prime(4))

    def test_pseudo_prime(self):
        self.assertFalse(is_prime(341))
        self.assertFalse(is_prime(3277))
        self.assertFalse(is_prime(91))
        self.assertFalse(is_prime(121))
        self.assertFalse(is_prime(5907))


if __name__ == '__main__':
    unittest.main()