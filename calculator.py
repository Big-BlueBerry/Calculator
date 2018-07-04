from node import *
from lexer import lex
from bparser import parse


def calc(n):
    if isinstance(n, BinaryNode):
        if n.op == '+':
            return calc(n.left) + calc(n.right)
        elif n.op == '-':
            return calc(n.left) - calc(n.right)
    return n.value


if __name__ == '__main__':
    print(calc(parse(lex(input()))))