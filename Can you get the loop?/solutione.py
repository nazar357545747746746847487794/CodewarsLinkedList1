class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

def loop_size(node):
    slow = node
    fast = node

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            break

    size = 1
    fast = fast.next
    while fast != slow:
        fast = fast.next
        size += 1

    return size
