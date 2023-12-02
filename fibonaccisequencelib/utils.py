"""
This module provides utility functions to enhance the functionality
of the Fibonacci library. It currently includes a logging decorator that can be
applied to functions to track their execution and log results for debugging and
monitoring purposes.

Available Decorators:
- logging_activity(level=DEFAULT_LOG_LEVEL): Logs the start and finish of a function.
"""
import functools
import logging

DEFAULT_LOG_LEVEL = logging.INFO


def logging_activity(level=DEFAULT_LOG_LEVEL):
    """
    Decorator that logs the start and end of the execution of the function it wraps.
    It provides a message with the function name and the result upon completion.

    This decorator can be stacked with others by preserving the function's signature
    and metadata, making it compatible with other decorators that might be used.

    Parameters:
    - level (int): The logging level (from the logging module) to use for messages.
                   Defaults to DEFAULT_LOG_LEVEL if not specified.

    Usage:
    @logging_activity(level=logging.INFO)
    def function_to_log(arg1, arg2):
        # Function implementation
        return result
    """
    def decorator(func):
        @functools.wraps(func)
        def func_wrapper(*args, **kwargs):
            if level <= logging.INFO:
                logging.info(
                    f"Starting function '{func.__name__}' with arguments {args} and keyword arguments {kwargs}")
            result = func(*args, **kwargs)
            if level <= logging.INFO:
                logging.info(
                    f"Finished function '{func.__name__}' with result: {result!r}")
            return result
        return func_wrapper
    return decorator
