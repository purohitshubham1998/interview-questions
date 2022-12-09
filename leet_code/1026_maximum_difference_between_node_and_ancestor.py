class Node:
    def __init__(self, val, left=None, right=None) -> None:
        self.val = val
        self.left = left
        self.right = right

class Track:
    def __init__(self, maxParent) -> None:
        self.currentMax = 0
        self.maxParent = maxParent

def func(node, currentMax, lst):
    if node is None:
        return currentMax
    for i in lst:
        currentMax = max(currentMax, abs(i-node.val))
    lst.append(node.val)
    left = func(node.left, currentMax, lst)
    right = func(node.right, currentMax, lst)
    lst.pop()
    return max(left, right)

# a = Node(8)
# b = Node(3)
# c = Node(10)
# d = Node(1)
# e = Node(6)
# f = Node(14)
# g = Node(4)
# h = Node(7)
# i = Node(13)

# a.left, a.right = b, c
# b.left, b.right = d, e
# c.right = f
# f.left = i
# e.left, e.right = g, h


a = Node(1)
b = Node(2)
c = Node(0)
d = Node(3)
a.right, b.right = b, c
c.left = d


# a = Node(0)
# b = Node(1)
# a.right = b

result = func(a, 0, [])
print(result)