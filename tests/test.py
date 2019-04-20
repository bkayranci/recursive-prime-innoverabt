import unittest

from src.helper import Helper


class HelperTestCase(unittest.TestCase):
    def test_is_prime_function(self):
        test_data = {
            1: False,
            2: True,
            3: True,
            4: False,
            5: True
        }

        for number, is_prime in test_data.items():
            self.assertEqual(is_prime, Helper.is_prime(number))

    def test_is_prime_function_with_non_valid(self):
        self.assertRaises(ValueError, Helper.is_prime, 0)
        self.assertRaises(ValueError, Helper.is_prime, -1)

if __name__ == '__main__':
    unittest.main()
