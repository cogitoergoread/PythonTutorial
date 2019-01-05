"""
http://openbookproject.net/thinkcs/python/english3e/linked_lists.html
"""

class Node:
    """
    Linked lists are made up of nodes, where each node contains a reference to the next node in the list.
    In addition, each node contains a unit of data called the cargo.
    A linked list is considered a recursive data structure because it has a recursive definition.
    A linked list is either:
      1, the empty list, represented by None, or
      2, a node that contains a cargo object and a reference to a linked list.
    """
    def __init__(self, cargo=None, next=None):
        self.cargo = cargo
        self.next  = next

    def __str__(self):
        return str(self.cargo)

    def str_backward(self):
        s: str = ""
        if self.next is not None:
            tail = self.next
            s += tail.str_backward() + " "
        s += self.cargo.__str__()
        return s

def str_list(node):
    s: str = ""
    while node is not None:
        s += node.__str__() + " "
        node = node.next
    return s

def str_backward(list: Node) -> str:
    """
    the following is a recursive algorithm for printing a list backwards:
      1, Separate the list into two pieces: the first node (called the head); and the rest (called the tail).
      2, Print the tail backward.
    Print the head.
    :param list: List to print
    :type list: Node
    :return: String printed
    :rtype: str
    """
    s: str = ""
    if list is None: return ""
    head = list
    tail = list.next
    s += str_backward(tail)
    s += head.__str__() + " "
    return s

def remove_second(list):
    """
    a method that removes the second node in the list and returns a reference to the removed node
    :param list: List ro remove the second from
    :type list: Node
    :return: shorter list
    :rtype: Node
    """
    if list is None: return
    first = list
    second = list.next
    # Make the first node refer to the third
    first.next = second.next
    # Separate the second node from the rest of the list
    second.next = None
    return second



class LinkedList:
    """"
    attributes are an integer that contains the length of the list and a reference to the first node
    """
    def __init__(self):
        self.length = 0
        self.head = None

    def str_backward(self):
        s: str = "["
        if self.head is not None:
             s+= self.head.str_backward()
        s += "]"
        return s

    def add_first(self, cargo):
        """
        akes an item of cargo as an argument and puts it at the beginning of the list
        :param cargo: item to add
        :type cargo:
        """
        node = Node(cargo)
        node.next = self.head
        self.head = node
        self.length += 1

    def add_last(self, cargo):
        """
        akes an item of cargo as an argument and puts it at the end of the list
        :param cargo: item to add
        :type cargo:
        """
        node = Node(cargo)
        nn: Node = self.head
        while nn.next is not None:
            nn = nn.next
        nn.next = node