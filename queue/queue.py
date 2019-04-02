class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Queue:
    def __init__(self):
        self.size = 0
        # what data structure should we
        # use to store queue elements?
        # self.storage =
        self.first = None
        self.last = None

    def enqueue(self, item):
        new_node = Node(item)
        if self.first == None:
            self.first = new_node
            self.last = new_node
        else:
            self.last.next = new_node
            self.last = new_node
        self.size += 1
        return self.size

    def dequeue(self):
        if self.size == 0:
            return None
        elif self.first == self.last:
            self.last = None
        temp = self.first
        self.first = self.first.next
        self.size -= 1
        return temp.value

    def len(self):
        return self.size


q = Queue()

print(q.enqueue(100))
print(q.enqueue(101))
print(q.enqueue(105))
print(q.first.value)
# print(q.dequeue())
# print(q.first.value)
# print(q.size)
print(q.dequeue())
print(q.first.value)
