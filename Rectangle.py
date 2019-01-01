"""
http://openbookproject.net/thinkcs/python/english3e/classes_and_objects_II.html
"""
from Point import Point

class Rectangle:
    """
    A class to manufacture rectangle objects
    """
    def __init__(self, posn : Point, w : float, h: float):
        """
        Initialize rectangle at posn, with width w, height h
        :param posn: lower left corner of te rectangle
        :type posn: Point
        :param w: Width
        :type w: float
        :param h: Height
        :type h: float
        """
        self.corner = posn
        self.width = w
        self.height = h

    def __repr__(self):
        return "Rectangle(Corner:{},Width:{}, Height:{})".format(self.corner, self.width, self.height)

    def __str__(self):
        return "({},{},{})".format(self.corner, self.width, self.height)

    def __eq__(self, other):
        if type(other) is type(self):
            return self.__dict__ == other.__dict__
        return False

    def grow(self, delta_width, delta_height):
        """
        Grow (or shrink) this object by the deltas
        :param delta_width: Growth of width
        :type delta_width: float
        :param delta_height: Growth of height
        :type delta_height:  float
        """
        self.width += delta_width
        self.height += delta_height

    def move(self, dx, dy):
        """
        Move this object by the deltas
        :param dx: Move of the corner, delta,x
        :type dx: float
        :param dy: Move of the corner, delta,y
        :type dy: float
        """
        self.corner.x += dx
        self.corner.y += dy

    def area(self):
        """
        returns the area
        :return: Area of the rectangle
        :rtype: float
        """
        return self.height * self.width

    def perimeter(self):
        """
         find the perimeter of any rectangle
        :return: perimeter
        :rtype: float
        """
        return 2 * (self.height + self.width)

    def flip(self):
        """
        swaps the width and the height of any rectangle instance
        """
        self.width, self.height = self.height, self.width

    def contains(self, point : Point):
        """
        test if a Point falls within the rectangle
        :param point:
        :type point:
        :return: True, the point is in the rectangle
        :rtype: bool
        """
        return ( self.corner.x <= point.x <= (self.corner.x + self.width)
                 and self.corner.y <= point.y <= (self.corner.y + self.height))

    def intersect(self, rectangle):
        """
        determine whether two rectangles collide
        :param rectangle: other rectangle to test the intersection with
        :type rectangle: Rectangle
        :return: True, tha rectangles are intersect
        :rtype: bool
        """
        return self.contains(rectangle.corner) or rectangle.contains(self.corner)