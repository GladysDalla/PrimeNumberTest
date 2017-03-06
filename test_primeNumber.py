import unittest
from solution_prime import is_prime_number

class TestPrimeNumbers(unittest.TestCase):
	"""tests for 'solution_prime.py'."""

	def test_input_is_true(self):
		"""tests if the output ranging from 2 to 10 are prime numbers"""
		self.assertTrue(is_prime_number(2, 10))

if __name__ == '__main__':
    unittest.main()

