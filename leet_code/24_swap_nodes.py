class Node:
    def __init__(self, val, next=None) -> None:
        self.val = val
        self.next = next


def swap_in_pairs(head):
    first = head
    if (second := first.next):
        head = second
    parent = None
    while first and second:
        if not first.next: break
        second = first.next
        temp = second.next
        second.next = first
        if parent:
            parent.next = second
        parent = first
        first.next = temp
        first = temp
    print_list(head)

def print_list(node: Node) -> None:
    head = node
    while head is not None:
        print(head.val)
        head = head.next







a = Node(1)
b = Node(2)
c = Node(3)
d = Node(4)

# a.next, b.next = b, c
# c.next = d
swap_in_pairs(a)