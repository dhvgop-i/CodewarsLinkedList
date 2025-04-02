class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None

def sorted_insert(head, data):
    if head is None:
        n = Node(data)
        n.next = head
        return n
    if data <= head.data:
        ins = Node(data)
        ins.next = head
        return ins
    elif head.next is None or head.data <= data <= head.next.data:
        ins = Node(data)
        ins.next = head.next
        head.next = ins
    else:
        sorted_insert(head.next, data)
    return head