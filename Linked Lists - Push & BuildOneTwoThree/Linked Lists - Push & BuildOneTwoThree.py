from preloaded import Node

def push(head, data):
    # Your code goes here.
    node = Node(data)
    node.next = head
    return node

def build_one_two_three():
    # Your code goes here.
    head = None
    for x in range(3, 0, -1):
        t = Node(x)
        t.next = head
        head = t
    return head
