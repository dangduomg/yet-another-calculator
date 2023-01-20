# yet another calculator

import logging

import colorama
import numpy as np
from lark import Lark

import transformer
import functions
import variables


calc = transformer.Calc(
    functions=vars(functions),
    variables=vars(variables),
)

with open('calc.lark') as f:
    parser = Lark(f, parser='lalr', start='expr', transformer=calc)


def calc_repr(o):
    if isinstance(o, float):
        return str(o)
    elif isinstance(o, (bool, np.bool_)):
        return str(o).lower()
    elif isinstance(o, np.ndarray):
        return f'[{", ".join(calc_repr(x) for x in o)}]'
    else:
        return f'python: {o}'


def main():
    colorama.init()
    logging.basicConfig(format='\033[91m%(levelname)s: %(message)s\033[m')

    while True:
        calc_input = input('calc> ')
        try:
            res = parser.parse(calc_input)
            print(calc_repr(res))
            calc.set(('_', res))
        except Exception as e:
            logging.error(e)


if __name__ == '__main__':
    main()
