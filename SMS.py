"""
http://openbookproject.net/thinkcs/python/english3e/classes_and_objects_I.html
6, SMS Store
"""
from typing import List, Any


class SMS:
    """
    Each message will be represented as a tuple:
    (has_been_viewed, from_number, time_arrived, text_of_SMS)
    """
    def __init__(self, viewed=False, fromn, time, text):
        self.viewed = viewed
        self.fromn = fromn
        self.time = time
        self.text = text

    def __repr__(self):
        return "SMS(Viewes:{},FromNr:{}, TimeArrived:{}, Text:{})".format(self.viewed, self.fromn, self.time, self.text)

    def __str__(self):
        return "({},{},{},{})".format(self.viewed, self.fromn, self.time, self.text

    def __eq__(self, other):
        if type(other) is type(self):
            return self.__dict__ == other.__dict__
        return False

class SMS_store:
    """
    This store can hold multiple SMS messages
    """
    store: List[SMS]

    def __init__(self):
        self.store = list()

    def add_new_arrival(self, from_number, time_arrived, text_of_SMS):
        """
        Makes new SMS tuple, inserts it after other messages
        in the store. When creating this message, its
        has_been_viewed status is set False.

        :param from_number: The nr the SMS was sent from
        :type from_number: str
        :param time_arrived: Time of arrive
        :type time_arrived: str
        :param text_of_SMS: Text of the sms
        :type text_of_SMS: str
        :return:
        :rtype:
        """
        self.store.append(SMS(from_number, time_arrived, text_of_SMS))

    def message_count(self):
        """
        Returns the number of sms messages in the store
        :return: nr of SMS
        :rtype: int
        """
        return len(self.store)

    def get_unread_indexes(self):
        """
        Returns list of indexes of all not-yet-viewed SMS messages
        :return: indeces of unread  SMS
        :rtype: list
        """
        pass

    def get_message(self, i):
        """
        Return (from_number, time_arrived, text_of_sms) for message[i]
        Also change its state to "has been viewed".
        If there is no message at position i, return None
        :param i: the index of SMS to get
        :type i: int
        :return: SMS returned
        :rtype: SMS
        """
        if i > 0 and i < self.store.count():
            self.store[i].viewed = True
            return self.store[i]
        return None


    def delete(self, i):
        """
        Delete the message at index i
        :param i: the index of SMS to delete
        :type i: int
        """
        self.store.remove(i)

    def clear(self):
        """
        Delete all messages from inbox
        """
        self.store.clear()