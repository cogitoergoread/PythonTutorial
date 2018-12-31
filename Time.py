"""
http://www.openbookproject.net/thinkcs/python/english2e/ch14.html
"""
from functools import total_ordering

@total_ordering
class Time:
    def __init__(self, h=0, m=0, s=0):
        """
        Idő létrehozása Óra,Perc,Másodperc darabokból
        :param h: Órák
        :type h: int
        :param m: Percek
        :type m: int
        :param s: Másodpercek
        :type s: int
        """
        self.hours = h
        self.minutes = m
        self.seconds = s

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
            return self.convert_to_seconds() < other.convert_to_seconds()
        return NotImplemented

    def make_time(seconds=0):
        """
        Idő létrehozása másodpercből
        :param seconds: Másodperc
        :type seconds: int
        :return: Másodpercből konvertált idő
        :rtype: Time
        """
        time = Time()
        time.hours = seconds // 3600
        time.minutes = (seconds - 3600 * time.hours) // 60
        time.seconds = seconds - 3600 * time.hours - 60 * time.minutes
        return time

    def add_time(self, t1):
        """
        Idő hozzáadása az objeektum idejéhez
        :param t1: Hozzáadandó idő
        :type t1: Time
        :return: A két idő összege
        :rtype: Time
        """
        sum: Time = Time()
        # Első , naive változat
        # sum.seconds = self.seconds + t1.seconds
        # sum.minutes = self.minutes + t1.minutes
        # sum.hours = self.hours + t1.hours
        sum.seconds = self.seconds + t1.seconds
        sum.minutes = self.minutes + t1.minutes + sum.seconds // 60
        sum.seconds = sum.seconds % 60
        sum.hours = self.hours + t1.hours + sum.minutes // 60
        sum.minutes = sum.minutes % 60
        return sum

    def increment_seconds(self, sec):
        """
        Megnöveli az időt valahány másodperccel
        :param sec: Ennyi másodpercel nöcel
        :type sec: int
        :return: megnövelt idő
        :rtype: Time
        """
        result: Time = Time()
        result.seconds = self.seconds + sec
        result.minutes = self.minutes + result.seconds // 60
        result.seconds = result.seconds % 60
        result.hours = self.hours + result.minutes // 60
        result.minutes = result.minutes % 60
        return result

    def convert_to_seconds(self):
        """
        Másodpercekre konvertálja az időt.
        :return: az idő másodpercben
        :rtype: int
        """
        return self.seconds + 60 * self.minutes + 3600 * self.hours