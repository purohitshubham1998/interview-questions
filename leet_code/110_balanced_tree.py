class Node:
    def __init__(self, val, left=None, right=None) -> None:
        self.left = left
        self.right = right
        self.val = val


def isBalanced(root: Node) -> bool:
    def func(node):
        if node is None:
            return 0
        left = 1 + func(node.left)
        right = 1 + func(node.right)
        if abs(left - right) <= 1:
            return min(left, right)
        return int(1e8)
    result: int = func(root)
    print(result)
    return False if result >= int(1e8) else True


a = Node(3)
b = Node(9)
d = Node(20)
e = Node(15)
f = Node(7)

a.left, a.right = b, d
d.left, d.right = e, f
print(isBalanced(a))

