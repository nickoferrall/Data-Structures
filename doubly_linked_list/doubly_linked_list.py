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
            # currentHead = self.head
            # new_node = ListNode(value, None, currentHead)
            # self.head = new_node
            self.head.prev = new_node
            self.head.prev.next = self.head
            self.head = new_node
        self.length += 1
        print("Head:", new_node)
        # return self.length

    # def remove_from_head(self):
    #     oldHead = self.head
    #     if self.length <= 1:
    #         self.head = None
    #         self.tail = None
    #     else:
    #         self.head = oldHead.next
    #         self.head.prev = None
    #         oldHead.next = None
    #         # followingHead = self.head.next
    #         # self.head = followingHead
    #     self.length -= 1
    #     return self.length

    def add_to_tail(self, value):
        pass

    def remove_from_tail(self):
        pass

    def move_to_front(self, node):
        pass

    def move_to_end(self, node):
        pass

    def delete(self, node):
        pass

    def get_max(self):
        pass


my_test = DoublyLinkedList(10)

# my_node = ListNode(14)

# print(my_node.insert_after(180))
# print(my_node.prev)
print(my_test.add_to_head(180))
# my_test.add_to_head(280)
# my_test.add_to_head(2800)
print(my_test.remove_from_head())
# print(my_test.add())
