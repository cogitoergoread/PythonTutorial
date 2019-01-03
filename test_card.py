from unittest import TestCase
from Cards import Card

class TestCard(TestCase):
    def test_to_rannum(self):
        self.assertEqual( 15, Card(1,1).to_rannum())

    def test_order(self):
        c1 = Card(1,1)
        c2 = Card(1,1)
        c3 = Card(2,2)
        self.assertTrue(c1 == c1)
        self.assertTrue(c1 == c2)
        self.assertTrue(c1 < c3)
        self.assertTrue(c1 <= c2)
        self.assertFalse(c1 == c3)
        self.assertFalse(c1 > c3)
        self.assertFalse(c1 >= c3)

