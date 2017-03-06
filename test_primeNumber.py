import unittest
from solution_prime import is_prime_number

class TestPrimeNumbers(unittest.TestCase):
	"""tests for 'solution_prime.py'."""

	def test_method_is_true(self):
		"""tests if the output ranging from 2 to 10 are prime numbers"""
		self.assertTrue(is_prime_number(2, 10))
	def test_input_is_not_string(self):
		"""tests if string is passed"""
		self.assertFalse(is_prime_number('this', 10))
	def test_negative_number(self):
		"""tests when negative number is passed"""
		self.assertFalse(is_prime_number(-2,10))


if __name__ == '__main__':
    unittest.main()

