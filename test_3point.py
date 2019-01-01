from unittest import TestCase
from Point import Point

class TestPoint(TestCase):
    def test_init(self):
        point = Point(3,4)
        self.assertEqual(3, point.x)
        self.assertEqual(4, point.y)

    def test_str_and_repr(self):
        point = Point(3, 4)
        self.assertEqual("Point(X:3,Y:4)", point.__repr__())
        self.assertEqual("(3,4)", point.__str__())

    def test_eq(self):
        p1 = Point(3, 4)
        p2 = Point(3, 4)
        p3 = Point(12, 13)
        self.assertEqual(True, p1 == p1)
        self.assertEqual(True, p1 == p2)
        self.assertEqual(False, p1 == p3)
        self.assertEqual(True, p1 != p3)
        self.assertEqual(False, p1 != p2)
        self.assertEqual(False, p1 != p1)

    def test_distance_from_origin(self):
        p1 = Point(3, 4)
        self.assertEqual(5, p1.distance_from_origin())

    def test_halfway(self):
        self.assertEqual(Point(3,4), Point().halfway(Point(6,8)))

    def test_diatance(self):
        self.assertEqual(10, Point(-3,-4).distance(Point(3,4)))

    def test_reflection(self):
        self.assertEqual(Point(3,4), Point(3,-4).reflect_x())

    def test_slope_from_orogin(self):
        self.assertEqual(1, Point(2,2).slope_from_origin())
        self.assertIsNone(Point(0,3).slope_from_origin())

    def test_get_line_to(self):
        self.assertEqual((2,3), Point(4,11).get_line_to(Point(6,15)))