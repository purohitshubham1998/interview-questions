class Node:
    def __init__(self, val, left=None, right=None) -> None:
        self.left = left
        self.right = right
        self.val = val

def level_order_traversal(root: Node):
    queue = [(root, 0)]
    level = [[]]
    while len(queue) != 0:
        node, order = queue.pop(0)
        level[order].append(node.val)
        nextOrder = order + 1
        if node.left:                
            queue.append((node.left, nextOrder))
        if node.right:
            queue.append((node.right, nextOrder))
    print(level)


a = Node(3)
b = Node(9)
d = Node(20)
e = Node(15)
f = Node(7)
a.left, a.right = b, d
d.left, d.right = e, f
print(level_order_traversal(a))
