class Node:
    def __init__(self, val, left=None, right=None) -> None:
        self.left = left
        self.right = right
        self.val = val


def diameter_of_binary_tree(node, memo):
    if node is None:
        return 0
    # if node.val in memo:
    #     return memo[node.val]
    currentMax = maximum_height(node.right, memo)+maximum_height(node.left, memo)
    left = diameter_of_binary_tree(node.left, memo)
    right = diameter_of_binary_tree(node.right, memo)
    return max(currentMax, left, right)

def maximum_height(node, memo):
    if node is None:
        return 0
    if node.val in memo:
        print("From memo")
        return memo[node.val]
    left = 1 + maximum_height(node.left, memo)
    right = 1 + maximum_height(node.right, memo)
    memo[node.val] = max(left, right)
    return memo[node.val]


a = Node(1)
b = Node(2)
c = Node(3)
d = Node(4)
e = Node(7)
f = Node(5)
g = Node(6)
h = Node(8)
i = Node(9)

a.left, a.right = b, c
c.left, c.right = d, e
d.left = f
f.left = g
e.right = h
h.right = i
memo = {}
result = diameter_of_binary_tree(a, memo)
print(result)
