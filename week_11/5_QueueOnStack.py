
class Stack:
    def __init__(self):
        self.stack_vals = []
        self.len = 0

    def push(self, val):
        self.stack_vals.append(val)
        self.len += 1

    def pop(self):
        if self.is_empty():
            return None
        res = self.stack_vals[-1]
        self.stack_vals = self.stack_vals[0:-1]
        self.len -= 1
        return res

    def __repr__(self):
        out = '|'
        for i in range(self.len):
            out += str(self.stack_vals[i]) + ' '
        out += '<-top'
        return out

    def peek(self):
        if self.is_empty():
            return None
        return self.stack_vals[-1]

    def __len__(self):
        return self.len

    def is_empty(self):
        return self.len == 0


class Queue:
    def __init__(self):
        self.stack = Stack()

    def enqueue(self, val):
        self.stack.push(val)

    def rear(self):
        if self.is_empty():
            return None
        return self.stack.peek()

    def dequeue(self):
        if self.is_empty():
            return None
        self.reverse_stack()
        res = self.stack.pop()
        self.reverse_stack()
        return res

    def reverse_stack(self):
        temp = Stack()
        while not self.stack.is_empty():
            temp.push(self.stack.pop())
        self.stack = temp

    def front(self):
        if self.is_empty():
            return None
        self.reverse_stack()
        res = self.stack.peek()
        self.reverse_stack()
        return res

    def __repr__(self):
        if self.is_empty():
            return 'empty queue'
        s = 'rear->'
        temp = Stack()
        while not self.stack.is_empty():
            temp.push(self.stack.pop())
            s += str(temp.peek()) + ','
        while not temp.is_empty():
            self.stack.push(temp.pop())
        return s[:-1]+'<-front'

    def __len__(self):
        return len(self.stack)

    def is_empty(self):
        return self.__len__() == 0


q1 = Queue()
print(q1)
q1.enqueue(4)
print(q1)
q1.enqueue(44)
q1.enqueue(444)
print(q1)
print(q1.dequeue())
print(q1)
print(len(q1))
print(q1)
print(q1.front())
print(q1.rear())


