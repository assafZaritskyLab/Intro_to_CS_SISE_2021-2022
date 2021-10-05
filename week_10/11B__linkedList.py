class Node:
    def __init__(self, val):
        self.value = val
        self.next = None

    def __repr__(self):
        return '[' + str(self.value) + ']'


class Linked_List:
    def __init__(self):
        self.head = None
        self.len = 0

    def __repr__(self):
        out = ''
        p = self.head
        while p != None:
            out += str(p) + '->'
            p = p.next
        return out

    def __len__(self):
        return self.len

    def add_at_start(self, val):
        p = Node(val)
        p.next = self.head
        self.head = p
        self.len += 1


lnk = Linked_List()
lnk.add_at_start(6)
lnk.add_at_start(4)
lnk.add_at_start(3)
lnk.add_at_start(5)
print(lnk)
