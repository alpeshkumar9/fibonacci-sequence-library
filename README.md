# Fibonacci Sequence Python Library

## Introduction

This Python library provides various methods to generate Fibonacci sequences. It offers a simple interface to produce sequences either through recursive, non-recursive approaches, or using a generator.

## Installation

Clone the Fibonacci Sequence Library from GitHub, first ensure you have Python 3.x & git are installed. Then run the following command:

```
git clone https://github.com/alpeshkumar9/fibonacci-sequence-library.git
```

Create and activate the virtual environment

```
cd fibonacci-sequence-library
python -m venv venv
source venv/bin/activate
```

To generate source and wheel distributions in the `dist/` directory,

```
pip install build
python -m build
```

To install the `fibonaccisequencelib` library use.

```
pip install dist/fibonaccisequencelib-0.1.0.tar.gz
```

Replace `fibonaccisequencelib-0.1.0.tar.gz` package name with the one inside the `dist` folder if different.

## Usage

### 1. Using command line:

Generate a Fibonacci sequence from the command line by executing the command:

```
fibonacci
```

It will ask for user input. Enter any value for `n`.
For n=5, it will generate below response:

```
Fibonacci Sequence Library Demonstration
Enter the length of the Fibonacci sequence (n): 5

Recursive Fibonacci:
[0, 1, 1, 2, 3]

Non-Recursive Fibonacci:
[0, 1, 1, 2, 3]

Fibonacci Generator:
0 1 1 2 3
```

### 2. Using Import

#### Importing the Library

```
from fibonaccisequencelib.fibonacci import Fibonacci
```

#### Generating a Fibonacci Sequence

The library offers three methods to generate a Fibonacci sequence:

1. Recursive Method:

```
fib = Fibonacci(10)
print(fib.recursive())
```

2. Non-Recursive Method:

```
fib = Fibonacci(10)
print(fib.non_recursive())
```

3. Using a Generator:

```
fib = Fibonacci(10)
for number in fib.generator():
    print(number, end=" ")
```

## Run the Tests with Coverage:

To run the tests with coverage measurement, use

```
pytest -v
```

In the terminal, the coverage percentage for each module or package that was tested will be shown.

![Screenshot 2023-12-02 at 4 26 28 pm](https://github.com/alpeshkumar9/fibonacci-sequence-library/assets/8064993/703ef14a-63d8-42ce-bb61-fcb1eb49aac6)

## License

This project is licensed under the GNU License - see the [LICENSE](/LICENSE) file for details.

## Contact

For any support or queries, feel free to reach out via [GitHub Issues](https://github.com/alpeshkumar9/fibonacci-sequence-library/issues).

# Improvements
## Packaging and Distribution
- Set up continuous integration and continuous deployment (CI/CD) pipelines for automated testing and distribution.
- Publish the package to PyPI for easier installation using pip.
