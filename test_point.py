from unittest import TestCase
from Point import Point


class TestPoint(TestCase):
    def test_distance_from_origin(self):
        point = Point(4, 3)
        self.assertEqual(point.distance_from_origin(), 5)

    def test_distance(self):
        point = Point(4, 3)
        point2 = Point(-4, -3)
        self.assertEqual(point.distance(point2), 10)
