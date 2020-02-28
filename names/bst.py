class bst:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        if value < self.value:
            if self.left is None:
                self.left = bst(value)
            else:
                self.left.insert(value)
        else:
            if self.right is None:
                self.right = bst(value)
            else:
                self.right.insert(value)

    def contains(self, target):
        if self.value == target:
            return True
        if target < self.value:
            if self.left:
                return self.left.contains(target)
        if target > self.value:
            if self.right:
                return self.right.contains(target)
        else:
            return False