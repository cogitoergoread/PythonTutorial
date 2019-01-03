"""
http://openbookproject.net/thinkcs/python/english3e/classes_and_objects_I.html
"""

class Point:
    """
    Point class represents and manipulates x,y coords.
    """

    def __init__(self, x=0, y=0):
        """
        Create a point at x,y
        :param x: x coordinate of the point
        :type x: float
        :param y:  y  coordinate of the point
        :type y: float
        """
        self.x = x
        self.y = y

    def __repr__(self):
        return "Point(X:{},Y:{})".format(self.x, self.y)

    def __str__(self):
        return "({},{})".format(self.x, self.y)

    def __eq__(self, other):
        if type(other) is type(self):
            return self.__dict__ == other.__dict__
        return False

    def distance_from_origin(self):
        """
        Compute my distance from the origin
        :return: distnce from origin
        :rtype: float
        """
        return (self.x ** 2 + self.y ** 2) ** 0.5

    def halfway(self, target):
        """
        Return the halfway point between myself and the target
        :param target: point that a halfway is calculated to from the actual point
        :type target: Point
        :return: point of the middle
        :rtype: Point
        """
        return Point( (self.x + target.x) / 2, (self.y + target.y) / 2)

    def distance(self, target):
        """
        Return the distance of myself and the target
        :param target: The point the distance is calculated to
        :type target: Point
        :return: distance of the target and myself
        :rtype: float
        """
        return ((self.x - target.x) ** 2 + (self.y - target.y) ** 2) **.5

    def reflect_x(self):
        """
        Reurn a point that is a reflection of the point about the x-axis
        :return: x-axis reflection
        :rtype: Point
        """
        return Point(self.x, -self.y)

    def slope_from_origin(self):
        """
        returns the slope of the line joining the origin to the point
        :return: slope of the origin and the line
        :rtype: float
        """
        if self.x == 0:
            return None
        return self.y / self.x

    def get_line_to(self, target):
        """
        compute the equation of the straight line joining the target to myself
        :param target: the point the line connects to myself
        :type target: Point
        :return: (m, c): y = mx + c
        :rtype: tuple
        """
        if self.x == target.x:
            return None
        m : float = (self.y - target.y) / (self.x - target.x)
        c : float = self.y - m * self.x
        return (m, c)

    def __add__(self, other):
        """
        adding two points adds their respective (x, y) coordinates:
        :param other: other point to add
        :type other: Point
        :return: sum of appropriíte coordinates
        :rtype: Point
        """
        return Point(self.x + other.x, self.y + other.y)

    def __mul__(self, other):
        """
        computes the dot product of the two Points, defined according to the rules of linear algebra
        :param other: other point to multiply
        :type other: Point
        :return: dot product of two points
        :rtype: float
        """
        return self.x * other.x + self.y * other.y

    def __rmul__(self, other):
        """
        performs scalar multiplication
        :param other: scalar to multiply with
        :type other: float
        :return: scalar product
        :rtype: Point
        """
        return Point(other * self.x, other * self.y)

"""
Kimaradt:

Given four points that fall on the circumference of a circle, find the midpoint of the circle. When will this function fail?

Hint: You must know how to solve the geometry problem before you think of going anywhere near programming. You cannot program a solution to a problem if you don’t understand what you want the computer to do!
Hint: file:///F:/muszi/Letol/Haromszog%20kore%20irhato%20kor%20kozeppontjanak%20es%20sugaranak%20meghatarozasa%20szamitassal.pdf

"""