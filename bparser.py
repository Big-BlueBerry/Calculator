from node import *


class Parser:
    def __init__(self, tokens):
        self.i = 0
        self.tokens = tokens

    def pop(self):
        self.i += 1
        return self.tokens[self.i - 1]

    def top(self):
        return self.tokens[self.i]

    def parse(self):
        l = self.pop()
        if self.i < len(self.tokens):
            op = self.pop()
            r = self.parse()
            return BinaryNode(NumNode(l), op, r)
        return NumNode(l)


def parse(tokens) -> Node:
    return Parser(tokens).parse()