class Node:
    def __init__(self, val, next=None) -> None:
        self.val = val
        self.next = next


def findMiddle(head):
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    print(slow.val)

a = Node(1)
b = Node(2)
c = Node(3)
d = Node(4)
e = Node(5)
f = Node(6)
a.next, b.next = b, c
c.next, d.next = d, e
e.next = f
findMiddle(a)