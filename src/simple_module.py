"""
simple_module.py

A minimal example module with a function to test.
"""

def sum_of_squares(a, b):
    """
    Returns the sum of the squares of a and b.
    For example:
    sum_of_squares(2, 3) -> 13
    """
    return a*a + b*b


def say_hello(name):
    """
    Returns a greeting string.
    For example:
    say_hello("Alice") -> "Hello, Alice!"
    """
    return f"Hello, {name}!"