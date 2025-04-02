def loop_size(node):
    fast = node.next.next
    slow = node.next
    while fast is not None and fast.next is not None:
        if fast == slow:
            break
        fast = fast.next.next
        slow = slow.next
    
    i = 1
    slow = slow.next
    while slow != fast:
        slow = slow.next
        i+=1
    return i
            