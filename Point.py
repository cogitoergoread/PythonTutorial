class Point:
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y

    def distance_from_origin(self):
        return (x *x + y * y) ** .5

    def distance(self, p):
