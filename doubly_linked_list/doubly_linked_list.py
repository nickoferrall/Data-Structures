"""Each ListNode holds a reference to its previous node
as well as its next node in the List."""


class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.value = value
        self.prev = prev
        self.next = next

    """Wrap the given value in a ListNode and insert it
  after this node. Note that this node could already
  have a next node it is point to."""

    def insert_after(self, value):
        current_next = self.next
        self.next = ListNode(value, self, current_next)
        if current_next:
            current_next.prev = self.next

    """Wrap the given value in a ListNode and insert it
  before this node. Note that this node could already
  have a previous node it is point to."""

    def insert_before(self, value):
        current_prev = self.prev
        self.prev = ListNode(value, current_prev, self)
        if current_prev:
            current_prev.next = self.prev

    """Rearranges this ListNode's previous and next pointers
  accordingly, effectively deleting this ListNode."""

    def delete(self):
        if self.prev:
            self.prev.next = self.next
        if self.next:
            self.next.prev = self.prev


"""Our doubly-linked list class. It holds references to
the list's head and tail nodes."""


class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length

    def add_to_head(self, value):
        new_node = ListNode(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.head.insert_before(value)
            self.head = self.head.prev
        self.length += 1

    def remove_from_head(self):
        oldHead = self.head
        if self.length <= 1:
            self.head = None
            self.tail = None
        else:
            self.head.delete()
        self.length -= 1
        return oldHead.value

    def add_to_tail(self, value):
        new_node = ListNode(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.insert_after(value)
            self.tail = self.tail.next
        self.length += 1
        return self.tail.value

    def remove_from_tail(self):
        to_be_removed = self.tail
        if self.length == 0:
            return None
        elif self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.tail.delete()
        self.length -= 1
        return to_be_removed.value

    def move_to_front(self, node):
        current = self.head
        new_node = ListNode(node)
        count = 0
        if self.length == 0:
            return None
        elif self.length == 1:
            return self.head.value
        elif self.length == 2:
            temporary = self.head.value
            self.head.value = self.tail.value
            self.tail.value = temporary
        else:
            while current.value != new_node.value:
                if count == self.length:
                    return None
                temp = self.head.value
                self.head.value = current.next.value
                self.head.next.value = temp
                count += 1
        return self.head.value

    def move_to_end(self, node):
        self.tail.insert_after(node.value)
        self.tail = self.tail.next
        if node is self.head:
            self.head = self.head.next
        node.delete()

    def delete(self, node):
        if node is self.head:
            self.head = self.head.next
        if node is self.tail:
            self.tail = self.tail.prev
        node.delete()
        self.length -= 1

    def get_max(self):
        if self.head is None:
            return None
        current_max = self.head.value
        current_node = self.head.next
        while current_node:
            if current_node.value > current_max:
                current_max = current_node.value
            current_node = current_node.next
        return current_max

    def print(self):
        arr = []
        test = self.head
        while test:
            arr.append(test.value)
            test = test.next
        return arr
