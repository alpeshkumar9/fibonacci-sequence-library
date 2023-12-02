"""
Unit tests for the Fibonacci class.

This test module contains a series of unit tests that validate the functionality
of the Fibonacci sequence generator in different scenarios, including edge cases
and invalid inputs. Tests cover all methods of the Fibonacci class.
"""

import unittest
import logging
from fibonaccisequencelib.fibonacci import Fibonacci


class TestFibonacci(unittest.TestCase):
    """
    Test suite for the Fibonacci class.

    This class contains a series of unit tests for testing the functionality of
    the Fibonacci sequence generator implemented in the Fibonacci class.
    """

    test_data = [
        (0, []),
        (1, [0]),
        (2, [0, 1]),
        (5, [0, 1, 1, 2, 3]),
        (10, [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]),
    ]

    @classmethod
    def setUpClass(cls):
        """
        Set up class method for initializing logging before running tests.
        """
        logging.basicConfig(level=logging.INFO,
                            format='%(asctime)s - %(levelname)s - %(message)s')

    def test_invalid_type_input(self):
        """
        Test the handling of invalid input and types.

        This test ensures that the Fibonacci class correctly raises exceptions
        for inputs that are not non-negative integers.
        """
        with self.assertRaises(ValueError):
            Fibonacci(-1)
        with self.assertRaises(TypeError):
            Fibonacci("a string")
        with self.assertRaises(TypeError):
            Fibonacci(5.5)
        with self.assertRaises(TypeError):
            Fibonacci(None)
        with self.assertRaises(TypeError):
            Fibonacci([1, 2, 3])
        with self.assertRaises(TypeError):
            Fibonacci({"a": 1})

    def test_recursive_fibonacci(self):
        """
        Test the recursive method of the Fibonacci class.

        This test checks if the recursive method correctly generates the Fibonacci
        sequence for a range of input values.
        """

        for input_n, expected_output in self.test_data:
            with self.subTest(f"Testing recursive method with input {input_n}"):
                fib = Fibonacci(input_n)
                self.assertEqual(fib.recursive(), expected_output)

    def test_iterative_fibonacci(self):
        """
        Test the non-recursive method of the Fibonacci class.

        This test checks if the non-recursive method correctly generates the Fibonacci
        sequence for a range of input values.
        """

        for input_n, expected_output in self.test_data:
            with self.subTest(f"Testing non-recursive method with input {input_n}"):
                fib = Fibonacci(input_n)
                self.assertEqual(fib.non_recursive(), expected_output)

    def test_generator_fibonacci(self):
        """
        Test the generator method of the Fibonacci class.

        This test checks if the generator method correctly yields the Fibonacci
        sequence for a range of input values.
        """

        for input_n, expected_output in self.test_data:
            with self.subTest(f"Testing generator method with input {input_n}"):
                fib = Fibonacci(input_n)
                self.assertEqual(list(fib.generator()), expected_output)

    def test_large_input_non_recursive(self):
        """
        Test the non-recursive method with a large input value.

        This test ensures that the non-recursive method can handle a large
        Fibonacci sequence (up to 1000 numbers) correctly.
        """

        fib = Fibonacci(1000)
        result = fib.non_recursive()
        self.assertEqual(len(result), 1000)
        self.assertTrue(all(isinstance(x, int) for x in result))

    def test_large_input_generator(self):
        """
        Test the generator method with a large input value.

        This test ensures that the generator method can handle a large
        Fibonacci sequence (up to 1000 numbers) correctly.
        """

        fib = Fibonacci(1000)
        result = list(fib.generator())
        self.assertEqual(len(result), 1000)
        self.assertTrue(all(isinstance(x, int) for x in result))

    def test_generator_state(self):
        """
        Test the state maintenance of the generator method.

        This test checks if the generator can maintain its state across
        multiple iterations to generate the correct sequence.
        """

        fib = Fibonacci(10)
        gen = fib.generator()
        first_five = [next(gen) for _ in range(5)]
        self.assertEqual(first_five, [0, 1, 1, 2, 3],
                         "First five Fibonacci numbers are incorrect.")
        next_five = [next(gen) for _ in range(5)]
        self.assertEqual(next_five, [5, 8, 13, 21, 34],
                         "Next five Fibonacci numbers are incorrect.")

    def test_logging_activity_decorator(self):
        """
        Test the logging activity of each method in the Fibonacci class.

        This test ensures that the logging decorator correctly logs the start
        and end of each method in the Fibonacci class.
        """

        for method_name in ['recursive', 'non_recursive', 'generator']:
            with self.subTest(f"Testing logging for {method_name} method"):
                with self.assertLogs(level='INFO') as log:
                    fib = Fibonacci(5)
                    if method_name != 'generator':
                        getattr(fib, method_name)()
                    else:
                        list(getattr(fib, method_name)())
                self.assertTrue(
                    any(
                        f"Starting function '{method_name}'" in log_msg for log_msg in log.output),
                    f"Log for the start of '{method_name}' method not found.")
                self.assertTrue(
                    any(
                        f"Finished function '{method_name}'" in log_msg for log_msg in log.output),
                    f"Log for the end of '{method_name}' method not found.")


if __name__ == "__main__":
    unittest.main()
