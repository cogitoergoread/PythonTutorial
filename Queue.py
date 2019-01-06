""""
http://openbookproject.net/thinkcs/python/english3e/queues.html
"""
from LInkedList import Node


class Queue:
    """
     first implementation of the Queue ADT we will look at is called a linked queue
     because it is made up of linked Node objects
    """
    def __init__(self):
        self.length = 0
        self.head = None

    def is_empty(self):
        return self.length == 0

    def insert(self, cargo):
        node = Node(cargo)
        if self.head is None:
            # If list is empty the new node goes first
            self.head = node
        else:
            # Find the last node in the list
            last = self.head
            while last.next:
                last = last.next
            # Append the new node
            last.next = node
        self.length += 1

    def remove(self):
        cargo = self.head.cargo
        self.head = self.head.next
        self.length -= 1
        return cargo

class ImprovedQueue:
    """
    We would like an implementation of the Queue ADT that can perform all operations in constant time
    """
    def __init__(self):
        self.length = 0
        self.head = None
        self.last = None

    def is_empty(self):
        return self.length == 0

    def insert(self, cargo):
        node = Node(cargo)
        if self.length == 0:
            # If list is empty, the new node is head and last
            self.head = self.last = node
        else:
            # Find the last node
            last = self.last
            # Append the new node
            last.next = node
            self.last = node
        self.length += 1

    def remove(self):
        cargo = self.head.cargo
        self.head = self.head.next
        self.length -= 1
        if self.length == 0:
            self.last = None
        return cargo

class PriorityQueue:
    """
     semantic difference is that the item that is removed from the queue is not necessarily the first one
     that was added. Rather, it is the item in the queue that has the highest priority.
     What the priorities are and how they compare to each other are not specified by the Priority Queue
     implementation. It depends on which items are in the queue.
    """
    def __init__(self):
        self.items = []

    def is_empty(self):
        return not self.items

    def insert(self, item):
        self.items.append(item)

    def remove(self):
        maxi = 0
        for i in range(1, len(self.items)):
            if self.items[i] > self.items[maxi]:
                maxi = i
        item = self.items[maxi]
        del self.items[maxi]
        return item


class Golfer:
    """
    example of an object with an unusual definition of priority, let’s implement a class
    called Golfer that keeps track of the names and scores of golfers
    """
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def __str__(self):
        return "{0:16}: {1}".format(self.name, self.score)

    def __gt__(self, other):
        return self.score < other.score  # Less is more

class ListQueue:
    """
    Write an implementation of the Queue ADT using a Python list.
    """
    def __init__(self):
        self.items = list()

    def is_empty(self):
        return len(self.items) == 0

    def insert(self, cargo):
        self.items.append(cargo)

    def remove(self):
        return self.items.pop(0)
