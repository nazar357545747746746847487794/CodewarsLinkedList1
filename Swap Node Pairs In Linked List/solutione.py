

class Node:
    def __init__(self, next=None):
        self.next = next

def swap_pairs(head):
    if head is None or head.next is None:
        return head

    dummy = Node(head)
    prev = dummy
    current = head

    while current and current.next:
        first = current
        second = current.next

        first.next = second.next
        second.next = first
        prev.next = second

        prev = first
        current = first.next

    return dummy.next
