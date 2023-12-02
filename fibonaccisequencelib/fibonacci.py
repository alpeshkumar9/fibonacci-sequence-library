from .utils import logging_activity


class Fibonacci:
    """
    A class for generating Fibonacci sequences.

    Attributes:
        n (int): The length of the Fibonacci sequence to generate.

    Methods:
        recursive(): Generates the Fibonacci sequence recursively.
        non_recursive(): Generates the Fibonacci sequence non-recursively.
        generator(): A generator that yields the Fibonacci sequence.
    """

    def __init__(self, n):
        """
        Initializes a new Fibonacci instance with a given sequence length.

        Args:
            n (int): The length of the Fibonacci sequence to generate.

        Raises:
            TypeError: If n is not an integer.
            ValueError: If n is not a non-negative integer.
        """

        if not isinstance(n, int):
            raise TypeError(f"The input {n} must be an integer")
        if n < 0:
            raise ValueError(f"The input {n} must be a non-negative integer")
        self.n = n

    @logging_activity()
    def recursive(self):

        def _recurse(n):
            if n <= 0:
                return []
            elif n == 1:
                return [0]
            elif n == 2:
                return [0, 1]
            else:
                seq = _recurse(n - 1)
                seq.append(seq[-1] + seq[-2])
                return seq

        result = _recurse(self.n)
        return result

    @logging_activity()
    def non_recursive(self):
        if self.n <= 0:
            return []
        elif self.n == 1:
            return [0]

        a, b = 0, 1
        fib_sequence = [a]
        while len(fib_sequence) < self.n:
            a, b = b, a + b
            fib_sequence.append(a)

        return fib_sequence

    @logging_activity()
    def generator(self):
        a, b = 0, 1
        for _ in range(self.n):
            yield a
            a, b = b, a + b