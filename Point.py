class Point:
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y

    def distance_from_origin(self):
        return (self.x * self.x + self.y * self.y) ** .5

    def distance(self, p):
        return