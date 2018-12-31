"""
http://www.openbookproject.net/thinkcs/python/english2e/ch14.html
"""


class Time:
    def __init__(self, h=0, m=0, s=0):
        self.hours = h
        self.minutes = m
        self.seconds = s

    def __str__(self):
        return "{:02d}:{:02d}:{:02d}".format(self.hours, self.minutes, self.seconds)
