from fibonaccisequencelib.fibonacci import Fibonacci


def main():
    """
    Demonstrates the Fibonacci Sequence Library.

    This function prompts the user to enter the length of the Fibonacci sequence (n) and then generates
    the sequence using various methods provided by the library.

    Usage:
    - Enter a non-negative integer value for n to generate the sequence.
    - Displays the recursive, non-recursive, and generator-based sequences.

    Exceptions:
    - Catches and displays any exception that may occur during execution.

    Returns:
    - None
    """

    print("Fibonacci Sequence Library Demonstration")

    try:
        n = int(input("Enter the length of the Fibonacci sequence (n): "))
        fib = Fibonacci(n)

        print("\nRecursive Fibonacci:")
        print(fib.recursive())

        print("\nNon-Recursive Fibonacci:")
        print(fib.non_recursive())

        print("\nFibonacci Generator:")
        for num in fib.generator():
            print(num, end=" ")
        print()
    except Exception as e:
        print("An error occurred:", e)
        return


if __name__ == "__main__":
    main()
