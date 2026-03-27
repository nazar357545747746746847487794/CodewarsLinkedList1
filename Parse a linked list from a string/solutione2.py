from preloaded import Node

def linked_list_from_string(s):
    parts = s.split(" -> ")
    if parts[0] == "None":
        return None

    head = Node(int(parts[0]))
    current = head

    for part in parts[1:-1]:
        current.next = Node(int(part))
        current = current.next

    return head
