# mathematical functions provided for calculator

from decimal import Decimal
import math


def exp(x):
    return x.exp()


def ln(x):
    return x.ln()


def log10(x):
    return x.log10()


def sqrt(x):
    return x.sqrt()


def sin(x):
    return Decimal(math.sin(x))


def cos(x):
    return Decimal(math.cos(x))


def tan(x):
    return Decimal(math.tan(x))


def asin(x):
    return Decimal(math.asin(x))


def acos(x):
    return Decimal(math.acos(x))


def atan(x):
    return Decimal(math.atan(x))


def atan2(x, y):
    return Decimal(math.atan2(x, y))


del Decimal, math