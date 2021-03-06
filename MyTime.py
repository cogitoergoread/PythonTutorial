"""
http://openbookproject.net/thinkcs/python/english3e/even_more_oop.html
"""
from functools import total_ordering

@total_ordering
class MyTime:
    """
    Records the time of day
    """
    def __init__(self, hrs: int = 0, mins: int = 0, secs: int = 0) -> object:
        """
        Create a new MyTime object initialized to hrs, mins, secs.
        The values of mins and secs may be outside the range 0-59,
          but the resulting MyTime object will be normalized.
        :param hrs: hours
        :type hrs: int
        :param mins: minutes
        :type mins: int
        :param secs: seconds
        :type secs: int
        """
        # Calculate total seconds to represent
        totalsecs = hrs * 3600 + mins * 60 + secs
        self.hours = totalsecs // 3600  # Split in h, m, s
        leftoversecs = totalsecs % 3600
        self.minutes = leftoversecs // 60
        self.seconds = leftoversecs % 60

    def __str__(self):
        return "{:02d}:{:02d}:{:02d}".format(self.hours, self.minutes, self.seconds)

    def __repr__(self):
        return "Time(H:{:02d}, M:{:02d}, S:{:02d})".format(self.hours, self.minutes, self.seconds)

    def __eq__(self, other):
        if type(other) is type(self):
            return self.__dict__ == other.__dict__
        return False

    def __lt__(self, other):
        if type(other) is type(self):
            return self.to_seconds() < other.to_seconds()
        return NotImplemented

    def increment_seconds(self, sec):
        """
        Megnöveli az időt valahány másodperccel
        :param sec: Ennyi másodpercel nöcel
        :type sec: int
        :return: megnövelt idő
        :rtype: MyTime
        """
        # Naive way
        # result: MyTime = MyTime()
        # result.seconds = self.seconds + sec
        # result.minutes = self.minutes + result.seconds // 60
        # result.seconds = result.seconds % 60
        # result.hours = self.hours + result.minutes // 60
        # result.minutes = result.minutes % 60
        # return result
        return MyTime(self.hours, self.minutes, self.seconds + sec)

    def to_seconds(self):
        """
        Másodpercekre konvertálja az időt.
        :return: az idő másodpercben
        :rtype: int
        """
        return self.seconds + 60 * self.minutes + 3600 * self.hours

    def __add__(self, other):
        """
        Overload default add to add two times
        :param other: time to add to self
        :type other: MyTime
        :return: the result of the addition
        :rtype: MyTime
        """
        return MyTime(0, 0, self.to_seconds() + other.to_seconds())

    def between(self, other_sm, other_lg):
        """
        takes two MyTime objects, t1 and t2, as arguments, and returns True if the invoking object falls between the
        two times. Assume t1 <= t2, and make the test closed at the lower bound and open at the upper bound,
        i.e. return True if t1 <= obj < t2.
        :param other_sm: tí, Time
        :type other_sm: MyTime
        :param other_lg: t2 time
        :type other_lg: MyTime
        :return:  eturn True if t1 <= obj < t2
        :rtype: bool
        """
        return other_sm <= self < other_lg