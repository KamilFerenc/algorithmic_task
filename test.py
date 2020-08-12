import unittest

from algorithm import reduce_elements, is_prime


class IsPrimeTest(unittest.TestCase):
    def test_is_prime_false(self):
        test_numbers = [6, 33, 69, 48, 98, 121]
        for number in test_numbers:
            self.assertFalse(is_prime(number), number)

    def test_is_prime_true(self):
        test_numbers = [2, 13, 37, 83, 3559]
        for number in test_numbers:
            self.assertTrue(is_prime(number), number)


class ReduceElementsTest(unittest.TestCase):
    def test_reduce_elements(self):
        sequence_a = [2, 3, 9, 2, 5, 1, 3, 7, 10]
        sequence_b = [2, 1, 3, 4, 3, 10, 6, 6, 1, 7, 10, 10, 10]
        sequence_c = [2, 9, 2, 5, 7, 10]
        self.assertEqual(reduce_elements(sequence_a, sequence_b), sequence_c)

    def test_reduce_elements_empty_list(self):
        sequence_a = []
        sequence_b = []
        sequence_c = []
        self.assertEqual(reduce_elements(sequence_a, sequence_b), sequence_c)


if __name__ == '__main__':
    unittest.main()
