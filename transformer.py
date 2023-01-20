# transformer (evaluator) for calculator

import numpy as np
from lark import Transformer


class Calc(Transformer):
    def __init__(self, *, functions=None, variables=None):
        self.functions = functions if functions else {}
        self.variables = variables if variables else {}

    def num(self, items):
        num, = items
        return float(num)

    def var(self, items):
        varname, = items
        try:
            return self.variables[varname]
        except KeyError as e:
            raise RuntimeError(f'Variable `{varname}` not found') from e

    def set(self, items):
        varname, value = items
        self.variables[varname] = value
        return self.variables[varname]

    def add(self, items):
        a, b = items
        return a + b

    def iadd(self, items):
        varname, value = items
        self.variables[varname] += value
        return self.variables[varname]

    def sub(self, items):
        a, b = items
        return a - b

    def isub(self, items):
        varname, value = items
        self.variables[varname] -= value
        return self.variables[varname]

    def mul(self, items):
        a, b = items
        return a * b

    def imul(self, items):
        varname, value = items
        self.variables[varname] *= value
        return self.variables[varname]

    def div(self, items):
        a, b = items
        return a / b

    def idiv(self, items):
        varname, value = items
        self.variables[varname] /= value
        return self.variables[varname]

    def pow(self, items):
        a, b = items
        return a ** b

    def ipow(self, items):
        varname, value = items
        self.variables[varname] **= value
        return self.variables[varname]

    def pos(self, items):
        a, = items
        return +a

    def neg(self, items):
        a, = items
        return -a

    def eq(self, items):
        a, b = items
        return a == b

    def ne(self, items):
        a, b = items
        return a != b

    def lt(self, items):
        a, b = items
        return a < b

    def le(self, items):
        a, b = items
        return a <= b

    def gt(self, items):
        a, b = items
        return a > b

    def ge(self, items):
        a, b = items
        return a >= b

    def call(self, items):
        callee, *args = items
        try:
            return self.functions[callee](*args)
        except KeyError as e:
            raise RuntimeError(f'`{callee}` is not a function') from e

    def array(self, items):
        return np.array(items)

    def array_shorthand(self, items):
        return np.array(items)

    def shorthand_row(self, items):
        return np.array(items)