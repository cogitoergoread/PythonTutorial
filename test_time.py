from unittest import TestCase

from Time import Time

class TestTime(TestCase):
    def test_init(self):
        time = Time(23, 59, 59)
        self.assertEqual(time.hours, 23)
        self.assertEqual(time.minutes, 59)
        self.assertEqual(time.seconds, 59)

    def test_to_str_max(self):
        time = Time(23, 59, 59)
        self.assertEqual("23:59:59", time.__str__())

    def test_to_str_short(self):
        time = Time(1, 2, 3)
        self.assertEqual("01:02:03", time.__str__())