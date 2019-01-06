from unittest import TestCase

from SMS import SMS, SMS_store

class TestSMS_store(TestCase):
    sms1 = SMS("+361224", "20190101 15:40", "BUÉK!")
    sms2 = SMS("+363012", "20191224 08:00", "Kellemes karácsonyt!")
    sms3 = SMS("+3619008", "20190501 15:40", "Éljen május 1!")

    def setUp(self):
        self.test_store = SMS_store()
        self.test_store.add_new_arrival(self.sms1.fromn, self.sms1.time, self.sms1.text)
        self.test_store.add_new_arrival(self.sms2.fromn, self.sms2.time, self.sms2.text)
        self.test_store.add_new_arrival(self.sms3.fromn, self.sms3.time, self.sms3.text)

    def test_add_new_arrival(self):
        self.assertEqual(self.sms1, self.test_store.store[0])
        self.assertEqual(self.sms2, self.test_store.store[1])
        self.assertEqual(self.sms3, self.test_store.store[2])

    def test_message_count(self):
        self.assertEqual(3, self.test_store.message_count())

    def test_get_unread_indexes(self):
        self.assertEqual([0,1,2], self.test_store.get_unread_indexes())

    def test_get_message(self):
        smscpy = SMS(self.sms2.fromn, self.sms2.time, self.sms2.text)
        smscpy.viewed = True
        self.assertEqual(smscpy, self.test_store.get_message(1))

    def test_delete(self):
        self.test_store.delete(1)
        self.assertEqual(self.sms1, self.test_store.store[0])
        self.assertEqual(self.sms3, self.test_store.store[1])
        self.assertEqual(2, self.test_store.message_count())

    def test_clear(self):
        self.test_store.clear()
        self.assertEqual(0, self.test_store.message_count())
