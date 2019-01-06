from unittest import TestCase
from Queue import Queue, ImprovedQueue, PriorityQueue, Golfer, ListQueue

class TestQueueClasses(TestCase):
    def setUp(self):
        self.queue = Queue()

    def test_is_empty(self):
        self.assertTrue(self.queue.is_empty())

    def test_insert(self):
        self.queue.insert(1)
        self.assertEqual(1, self.queue.head.cargo)

    def test_remove(self):
        self.queue.insert(1)
        self.assertEqual(1, self.queue.remove())

    def test_insert_remove_multi(self):
        self.queue.insert(1)
        self.queue.insert(2)
        self.queue.insert(3)
        self.assertEqual(1, self.queue.remove())
        self.assertEqual(2, self.queue.remove())
        self.assertEqual(3, self.queue.remove())


class TestImporvedQueue(TestQueueClasses):
    def setUp(self):
        self.queue = ImprovedQueue()


class TestPriorityQueue(TestQueueClasses):
    def setUp(self):
        self.queue = PriorityQueue()

    def test_insert(self):
        self.queue.insert(1)
        self.assertEqual(1, self.queue.items[0])

    def test_insert_remove_multi(self):
        self.queue.insert(1)
        self.queue.insert(2)
        self.queue.insert(3)
        self.assertEqual(3, self.queue.remove())
        self.assertEqual(2, self.queue.remove())
        self.assertEqual(1, self.queue.remove())

class TestGolfer(TestPriorityQueue):

    def test_golfer(self):
        g1 = Golfer("Tiger Woods", 61)
        g2 = Golfer("Phil Mickelson", 72)
        g3 = Golfer("Hal Sutton", 69)
        self.queue.insert(g1)
        self.queue.insert(g2)
        self.queue.insert(g3)
        self.assertEqual(g1, self.queue.remove())
        self.assertEqual(g3, self.queue.remove())
        self.assertEqual(g2, self.queue.remove())

    def test_str(self):
        g1 = Golfer("Tiger Woods", 61)
        self.assertEqual("Tiger Woods     : 61", g1.__str__())

class TestListQueue(TestQueueClasses):
    def setUp(self):
        self.queue = ListQueue()

    def test_insert(self):
        self.queue.insert(1)
        self.assertEqual(1, self.queue.items[0])
