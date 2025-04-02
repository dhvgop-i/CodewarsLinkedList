class Node(object):
    """Node class for reference"""
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

def get_nth(node, index):
    i = 0
    if node is None:
        raise ValueError("linked list should not be None")
    while node is not None:
        if i == index:
            return node
        node = node.next
        i += 1
    raise ValueError("index out of range")