class Node:
    def __init__(self, val):
        self.value = val
        self.next = None

class Linked_List:
    def __init__(self):
        self.head = None
        self.len = 0

    def __len__(self):
        return self.len

    def add_at_start(self, val):
        p = Node(val)
        p.next = self.head
        self.head = p
        self.len += 1

    def insert(self, loc, val):
        if not (0 <= loc <= len(self)):
            print("Invalid location")
            return
        if loc == 0:
            self.add_at_start(val)
            return
        p = self.head
        for i in range(0, loc - 1):
            p = p.next
        tmp = p.next
        p.next = Node(val)
        p.next.next = tmp
        self.len += 1


lnk = Linked_List()
lnk.add_at_start(6)
lnk.add_at_start(4)
lnk.add_at_start(3)
lnk.add_at_start(5)
lnk.insert(2, 10)

