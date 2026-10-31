"""
operations.py
All the math logic for the scientific calculator lives here, separate
from the menu/input handling in ui.py and the entry point in main.py.
"""

import math


def add(x, y):
    return x + y

def double(x):
    return x + x

def subtract(x, y):
    return x - y


def multiply(x, y):
    return x * y


def divide(x, y):
    if y == 0:
        raise ValueError("Cannot divide by zero.")
    return x / y


def power(x, y):
    return x ** y


def square_root(x):
    if x < 0:
        raise ValueError("Cannot take square root of a negative number.")
    return math.sqrt(x)


def sine(x):
    """x is in degrees."""
    return math.sin(math.radians(x))


def cosine(x):
    """x is in degrees."""
    return math.cos(math.radians(x))


def tangent(x):
    """x is in degrees."""
    return math.tan(math.radians(x))


def natural_log(x):
    if x <= 0:
        raise ValueError("Cannot take log of zero or a negative number.")
    return math.log(x)


def log_base_10(x):
    if x <= 0:
        raise ValueError("Cannot take log of zero or a negative number.")
    return math.log10(x)


def factorial(x):
    if x < 0 or int(x) != x:
        raise ValueError("Factorial requires a non-negative integer.")
    return math.factorial(int(x))
