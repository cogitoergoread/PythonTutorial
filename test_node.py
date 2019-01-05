from unittest import TestCase
from LInkedList import Node, LinkedList

class TestNode(TestCase):
    def setUp(self):
        self.node1 = Node(1)
        self.node2 = Node(2)
        self.node3 = Node(3)
        self.node1.next = self.node2
        self.node2.next = self.node3

    def test_node_print(self):
        from LInkedList import str_list
        self.assertEqual('1 2 3 ', str_list(self.node1))

    def test_node_back(self):
        from LInkedList import str_backward
        self.assertEqual('3 2 1 ', str_backward(self.node1))

    def test_remove2nd(self):
        from LInkedList import str_list, remove_second
        self.assertEqual('1 2 3 ', str_list(self.node1))
        remove_second(self.node1)
        self.assertEqual('1 3 ', str_list(self.node1))

class TestLinkedList(TestCase):
    def setUp(self):
        self.lili = LinkedList()
        self.lili.add_first(3)
        self.lili.add_first(2)
        self.lili.add_first(1)

    def test_liliprint(self):
        from LInkedList import str_list
        self.assertEqual('1 2 3 ', str_list(self.lili.head))

    def test_str_back(self):
        self.assertEqual('[3 2 1]', self.lili.str_backward())

    def test_add_last(self):
        self.lili.add_last(0)
        from LInkedList import str_list
        self.assertEqual('1 2 3 0 ', str_list(self.lili.head))
        self.assertEqual('[0 3 2 1]', self.lili.str_backward())
