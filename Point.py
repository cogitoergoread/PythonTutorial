"""
http://www.openbookproject.net/thinkcs/python/english2e/ch13.html
"""
from math import sqrt


class Point:
    """
    Egy két dimenziós pont adatszerkezete
    """
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y

    def distance_from_origin(self):
        return sqrt(self.x * self.x + self.y * self.y)

    def distance(self, p):
        """
        Az adott pont és a paraméterként kapott pont távolságát adja vissza.
        :param p: Ettől mért távolságot vesszük.
        :type p: Point
        :return: Descart távolság a pont és a paramter között
        :rtype: int
        """
        return sqrt((self.x - p.x)**2 + (self.y - p.y) ** 2 )