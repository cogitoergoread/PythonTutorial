from unittest import TestCase

from Time import Time

class TestTime(TestCase):
    def test_init_hms(self):
        time = Time(23, 59, 59)
        self.assertEqual(time.hours, 23)
        self.assertEqual(time.minutes, 59)
        self.assertEqual(time.seconds, 59)

    def test_eq(self):
        t1 = Time(1, 2, 3)
        t2 = Time(1, 2, 3)
        t3 = Time(0, 2, 3)
        self.assertEqual(t1, t1)
        self.assertEqual(t1, t2)
        self.assertNotEqual (t3, t1)

    def test_comparisions(self):
        t1 = Time(1, 2, 3)
        t2 = Time(1, 0, 3)
        self.assertEqual(True, t1 > t2)
        self.assertEqual(False, t1 == t2)
        self.assertEqual(True, t1 >= t2)
        self.assertEqual(False, t2 > t2)
        self.assertEqual(True, t2 >= t2)
        self.assertEqual(False, t2 > t1)
        self.assertEqual(False, t2 >= t1)

    def test_to_str_max(self):
        time = Time(23, 59, 59)
        self.assertEqual("23:59:59", time.__str__())

    def test_to_str_short(self):
        time: Time = Time(1, 2, 3)
        self.assertEqual("01:02:03", time.__str__())

    def test_make_time(self):
        time = Time.make_time(23 * 3600+ 60 * 59 + 59)
        self.assertEqual(time.hours, 23)
        self.assertEqual(time.minutes, 59)
        self.assertEqual(time.seconds, 59)

    def test_add_small(self):
        time = Time(1,2,3)
        t2 = Time(4,5,6)
        t3 = time.add_time(t2)
        self.assertEqual(Time(5,7,9), t3)

    def test_add_large(self):
        time = Time(1,40,50)
        t2 = Time(4,50,55)
        t3 = time.add_time(t2)
        self.assertEqual(t3.hours, 6)
        self.assertEqual(t3.minutes, 31)
        self.assertEqual(t3.seconds, 45)

    def test_increment(self):
        time = Time(1,59,59)
        time = time.increment_seconds(1)
        self.assertEqual(Time(2,0,0), time)

    def test_convert_to_seconds(self):
        time = Time(1,59,59)
        self.assertEqual(7199, time.convert_to_seconds())