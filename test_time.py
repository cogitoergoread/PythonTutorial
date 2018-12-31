from unittest import TestCase

from TimeOld import TimeOld

class TestTime(TestCase):
    def test_init_hms(self):
        time = TimeOld(23, 59, 59)
        self.assertEqual(time.hours, 23)
        self.assertEqual(time.minutes, 59)
        self.assertEqual(time.seconds, 59)

    def test_eq(self):
        t1 = TimeOld(1, 2, 3)
        t2 = TimeOld(1, 2, 3)
        t3 = TimeOld(0, 2, 3)
        self.assertEqual(t1, t1)
        self.assertEqual(t1, t2)
        self.assertNotEqual (t3, t1)

    def test_comparisions(self):
        t1 = TimeOld(1, 2, 3)
        t2 = TimeOld(1, 0, 3)
        self.assertEqual(True, t1 > t2)
        self.assertEqual(False, t1 == t2)
        self.assertEqual(True, t1 >= t2)
        self.assertEqual(False, t2 > t2)
        self.assertEqual(True, t2 >= t2)
        self.assertEqual(False, t2 > t1)
        self.assertEqual(False, t2 >= t1)

    def test_to_str_max(self):
        time = TimeOld(23, 59, 59)
        self.assertEqual("23:59:59", time.__str__())

    def test_to_str_short(self):
        time: TimeOld = TimeOld(1, 2, 3)
        self.assertEqual("01:02:03", time.__str__())

    def test_make_time(self):
        time = TimeOld.make_time(23 * 3600 + 60 * 59 + 59)
        self.assertEqual(time.hours, 23)
        self.assertEqual(time.minutes, 59)
        self.assertEqual(time.seconds, 59)

    def test_add_small(self):
        time = TimeOld(1, 2, 3)
        t2 = TimeOld(4, 5, 6)
        t3 = time.add_time(t2)
        self.assertEqual(TimeOld(5, 7, 9), t3)

    def test_add_large(self):
        time = TimeOld(1, 40, 50)
        t2 = TimeOld(4, 50, 55)
        t3 = time.add_time(t2)
        self.assertEqual(t3.hours, 6)
        self.assertEqual(t3.minutes, 31)
        self.assertEqual(t3.seconds, 45)

    def test_increment(self):
        time = TimeOld(1, 59, 59)
        time = time.increment_seconds(1)
        self.assertEqual(TimeOld(2, 0, 0), time)

    def test_convert_to_seconds(self):
        time = TimeOld(1, 59, 59)
        self.assertEqual(7199, time.convert_to_seconds())