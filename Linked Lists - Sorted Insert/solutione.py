
class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None


def sorted_insert(head, data):
    node = Node(data)

    if head is None or data <= head.data:
        node.next = head
        return node

    current = head
    while current.next and current.next.data < data:
        current = current.next

    node.next = current.next
    current.next = node

    return head
