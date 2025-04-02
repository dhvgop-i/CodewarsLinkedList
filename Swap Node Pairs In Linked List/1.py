from preloaded import Node

def swap_pairs(head):
    if head is None or head.next is None: return head
    new_head = head.next
    head.next = new_head.next
    new_head.next = head

    while head.next is not None and head.next.next is not None:
        new_last = head.next
        head.next = new_last.next
        new_last.next = head.next.next
        head.next.next = new_last
        head = new_last
    return new_head
