class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left  = left
        self.right = right

tree1 = Node(1,
            Node(2,
                Node(3),
                Node(4)),
            Node(5,
                Node(6),
                Node(7)))

tree2 = Node(1,
            Node(2,
                Node(3)),
            Node(4))

def sum(tree):
    if tree:
        return sum(tree.left) + sum(tree.right) + tree.value
    else:
        return 0

assert(sum(tree1) == 28)
assert(sum(tree2) == 10)
