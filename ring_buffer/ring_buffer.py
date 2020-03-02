from doubly_linked_list import DoublyLinkedList


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = None
        self.storage = DoublyLinkedList()

    def append(self, item):
        # if capacity is not met:
            # append new item to the tail of list
            # set current to track tail
        if self.storage.length < self.capacity:
            self.storage.add_to_tail(item)
            self.current = self.storage.tail
        
        # if capacity is met:
            # if current is at the tail:
                # move it to head if so
            # else:
                # move to the next of current
        if self.storage.length == self.capacity:
            self.current.value = item
            if self.current is self.storage.tail:
                self.current = self.storage.head
            else:
                self.current = self.current.next
                

    def get(self):
        # Note:  This is the only [] allowed
        list_buffer_contents = []

        # TODO: Your code here
        index = self.storage.head
        while index is not None:
            list_buffer_contents.append(index.value)
            index = index.next
        return list_buffer_contents

# ----------------Stretch Goal-------------------


class ArrayRingBuffer:
    def __init__(self, capacity):
        pass

    def append(self, item):
        pass

    def get(self):
        pass

# ring = RingBuffer(5)
# ring.append(1)
# print(ring.storage.head.value)
# print(ring.get())
# ring.append(2)
# ring.append(3)
# ring.append(4)
# ring.append(5)
# print(ring.get())