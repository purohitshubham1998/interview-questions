class Node:
    def __init__(self, val, left=None, right=None) -> None:
        self.left = left
        self.right = right
        self.val = val


def binary_tree_maximum_path_sum(root) -> int:
    memo = {}
    def func(node) -> int:
        if node is None:
            return 0
        left = max_path_sum(node.left, memo)
        right = max_path_sum(node.right, memo)
        currentMax = node.val + left + right
        return max(currentMax, func(node.left), func(node.right))

    def max_path_sum(node, memo) -> int:
        if node is None:
            return 0
        if node in memo:
            return memo[node]
        left = node.val + max_path_sum(node.left, memo)
        right = node.val + max_path_sum(node.right, memo)
        memo[node] = max(left, right)
        return memo[node]

    return func(root)

a = Node(-10)
b = Node(9)
c = Node(20)
d = Node(15)
f = Node(7)

a.left, a.right = b, c
c.left, c.right = d, f

result = binary_tree_maximum_path_sum(a)
print(result)