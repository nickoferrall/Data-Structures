class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        if self.value == None:
            self.value = value
        elif self.value < value:
            if self.right is None:
                self.right = BinarySearchTree(value)
            else:
                self.right.insert(value)
        elif self.value > value:
            if self.left is None:
                self.left = BinarySearchTree(value)
            else:
                self.left.insert(value)

    def contains(self, target):
        print("SELF", self.value, target)
        if self.value == None:
            return False
        elif self.value == target:
            return True
        elif self.value < target:
            if self.right is None:
                return False
            else:
                return self.right.contains(target)
        elif self.value > target:
            if self.left is None:
                return False
            else:
                return self.left.contains(target)

    def get_max(self):
        if self.value == None:
            return None
        else:
            if self.right == None:
                return self.value
            else:
                return self.right.get_max()

    def for_each(self, cb):
        cb(self.value)
        print("SELF RIGHT", self.right)
        if self.right:
            # cb(self.right)
            self.right.for_each(cb)
        print("SELF LEFT", self.left)
        if self.left:
            self.left.for_each(cb)


BST = BinarySearchTree(5)

# print("Root", BST.root)

print(BST.insert(2))
print(BST.insert(3))
print(BST.insert(7))
# print(BST.contains(7))
print(BST.contains(8))

print(BST.get_max())

# print("Final Val:", BST.left)

arr = []


def cb(x): return arr.append(x)


print("----------------")
print(BST.for_each(cb))
print("Arr:", arr)
