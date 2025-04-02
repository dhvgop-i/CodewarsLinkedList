class Node(object):
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

def reverse(head):
    last = None
    while head is not None:
        last = Node(head.data, last)
        head = head.next
    return last
