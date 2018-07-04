class Node:
    pass


class BinaryNode(Node):
    def __init__(self, l, op, r):
        self.left = l
        self.op = op
        self.right = r


class NumNode(Node):
    def __init__(self, value):
        self.value = value
