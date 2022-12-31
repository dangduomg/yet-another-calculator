# yet another calculator

import logging
from decimal import Decimal

import colorama
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


def main():
    colorama.init()
    logging.basicConfig(format='\033[91m%(levelname)s: %(message)s\033[m')

    while True:
        calc_input = input('calc> ')
        try:
            res = parser.parse(calc_input)
            print(res)
            calc.set(('_', res))
        except Exception as e:
            logging.error(e)


if __name__ == '__main__':
    main()
