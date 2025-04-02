class Node(object):
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next
    
class Context(object):
    def __init__(self, first, second):
        self.first = first
        self.second = second
    
def alternating_split(head):
    if head is None or head.next is None:
        raise ValueError("head must be a Node with not None next param")
    
    result = Context(head, head.next)
    
    first_last = result.first
    second_last = result.second
    while True:
        try:
            first_last.next = second_last.next
            first_last = first_last.next
            second_last.next = second_last.next.next
            second_last=second_last.next
        except AttributeError:
            break
    return result