class Node(object):
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

def remove_duplicates(head):
    # Your code goes here.
    # Remember to return the head of the list.
    if head is None: return head
    has = set()
    has.add(head.data)
    body = head
    while body.next is not None:
        if not body.next.data in has:
            has.add(body.next.data)
            body = body.next
        else:
            body.next = body.next.next
    return head
