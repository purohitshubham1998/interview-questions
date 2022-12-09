class Node:
    def __init__(self, value, left=None, right=None) -> None:
        self.left = left
        self.right = right
        self.value = value


def hasPathSum(root, targetSum: int):
    def func(node, currentSum):
        if node and node.left is None and node.right is None:
            return currentSum+node.value == targetSum
        left = right = False
        if node:
            left = func(node.left, currentSum+node.value)
            right = func(node.right, currentSum+node.value)
        return left or right
    return func(root, 0)

a = Node(5)
b = Node(4)
c = Node(8)
d = Node(11)
e = Node(2)
f = Node(7)
g = Node(13)
h = Node(4)
i = Node(1)

a.left = b
a.right = c
b.left = d
d.left = f
d.right = e
c.left = g
c.right = h
h.right = i

print(hasPathSum(root=a, targetSum=22))