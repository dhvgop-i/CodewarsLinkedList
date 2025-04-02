def linked_list_from_string(s):
    if s == "None": return None
    node = Node(int(s[:s.find(' -> ')]), linked_list_from_string(s[s.find(' -> ')+4:]))
    return node
