from unittest import TestCase
from Point import Point
from Rectangle import Rectangle

class TestRectangle(TestCase):
    def setUp(self):
        self.rect = Rectangle(Point(3,4), 6, 5)
    def test_grow(self):
        self.rect.grow(1, 3)
        self.assertEqual(Rectangle(Point(3,4), 7, 8), self.rect)

    def test_move(self):
        self.rect.move(2, -3)
        self.assertEqual(Rectangle(Point(5, 1), 6, 5), self.rect)

    def test_area(self):
        self.assertEqual(30, self.rect.area())

    def test_perimeter(self):
        self.assertEqual(22, self.rect.perimeter())

    def test_flip(self):
        self.rect.flip()
        self.assertEqual(Rectangle(Point(3, 4), 5, 6), self.rect)

    def test_contains(self):
        r = Rectangle(Point(0, 0), 10, 5)
        self.assertTrue(r.contains(Point(0, 0)))
        self.assertTrue(r.contains(Point(3, 3)))
        self.assertFalse(r.contains(Point(3, 7)))
        self.assertTrue(r.contains(Point(3, 5)))
        self.assertTrue(r.contains(Point(3, 4.99999)))
        self.assertFalse(r.contains(Point(-3, -3)))

    def test_intersect(self):
        self.assertTrue(self.rect.intersect(Rectangle(Point(4,5), 1, 2)))
        self.assertTrue(self.rect.intersect(Rectangle(Point(1,2), 7, 5)))
        self.assertFalse(self.rect.intersect(Rectangle(Point(1,2), 1, 1)))
