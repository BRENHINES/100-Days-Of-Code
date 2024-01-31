"""
Title : Simple Calculator

Objectifs : Create a console application for operations
Output: We will have a programme which ask to the user two inputs (numbers) and
        an opération , and display the output
Features: Command line , typing error management
"""


def addition(a: int, b: int) -> int:
    """Addition

    :param a: the first integer input
    :param b: the second integer input
    :return: The result of the addition between the two arguments : a + b
    """
    return a + b


def substraction(a: int, b: int) -> int:
    """Substraction

    :param a: the first integer input
    :param b: the second integer input
    :return: The result of the substraction between the two arguments : a - b
    """
    return a - b


def divide(a: int, b: int) -> float:
    """ Division

    :param a: the first integer input
    :param b: the second integer input
    :return: The result of the division between the two arguments : a / b
    """
    return a / b


def multiply(a: int, b: int) -> int:
    """Multiplication

    :param a: the first integer input
    :param b: the second integer input
    :return: The result of the multiplication between the two arguments : a * b
    """
    return a * b


def integer_divide(a: int, b: int) -> int:
    """Integer Division

    :param a: the first integer input
    :param b: the second integer input
    :return: An integer from the division between the two arguments
    """
    return a // b


def power(a: int, b: int) -> int:
    """Power

    :param a: the first integer input
    :param b: the second integer input
    :return: The result of the powered of a by b :  a ** b
    """
    return a ** b
