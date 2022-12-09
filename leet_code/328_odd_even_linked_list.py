class Node:
    def __init__(self, val, next=None) -> None:
        self.val = val
        self.next = next


# def odd_even_linked_list(head):
#     first = head
#     second = None
#     if first.next:
#         second = first.next
#     secondHead = temp = Node(-1)
#     i = 1
#     while first and second:
#         if not i & 1:
#             temp.next = first
#             temp = second.next
#         first.next = second.next
#         first = second
#         second = second.next
#         i += 1
#     first.next = secondHead.next
#     return head

def odd_even_linked_list(head):
    if not head:
        return head
    odd = head
    even = None
    temp = None
    if odd:
        temp = even = odd.next
    prev = None
    while even and odd:
        if odd.next:
            temp1 = odd.next.next
            odd.next = temp1
            prev = odd
            odd = temp1
        if even.next:
            temp2 = even.next.next
            even.next = temp2
            even = temp2
    if odd:
        odd.next = temp
    elif prev:
        prev.next = temp
    print_list(head)
    return head

def print_list(head: Node):
    temp = head
    while temp:
        print(temp.val)
        temp = temp.next

a = Node(1)
b = Node(2)
c = Node(3)
d = Node(4)
e = Node(5)
f = Node(6)
g = Node(7)
h = Node(8)
a.next, b.next = b, c
# a.next, b.next, c.next, d.next, e.next, f.next, g.next = b, c, d, e, f, g, h
head = odd_even_linked_list(a)