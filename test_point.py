from unittest import TestCase
from Point_Old import PointOld


class TestPoint(TestCase):
    def test_distance_from_origin(self):
        point = PointOld(4, 3)
        self.assertEqual(point.distance_from_origin(), 5)

    def test_distance(self):
        point = PointOld(4, 3)
        point2 = PointOld(-4, -3)
        self.assertEqual(point.distance(point2), 10)
