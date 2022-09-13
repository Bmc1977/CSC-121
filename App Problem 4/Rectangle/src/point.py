class Point:
    """
    Represents a point in 2-dimensional Cartesian space. Style updated to conform
    to PEP 8 (lower-cased function and attribute names, corrected indentation)
    """

    def __init__(self, init_x, init_y):
        """ Create a new point at the given coordinates. """
        self.x = init_x
        self.y = init_y

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def distance_from_origin(self):
        # return ((self.x ** 2) + (self.y ** 2)) ** 0.5
        return self.distance_from(Point(0,0))

    def __str__(self):
        return f"Point:({self.x}, {self.y})"

    def midpoint(self, target):
        mx = (self.x + target.x) / 2
        my = (self.y + target.y) / 2
        return Point(mx, my)

    def distance_from(self, other):
        return (((self.x - other.x) ** 2) + ((self.y - other.y) ** 2)) ** 0.5

    def slope_to(self, b):
        try:
            slope = (b.y - self.y) / (b.x - self.x)
        except ZeroDivisionError:
            return float('inf')
        else:
            return slope

    def close_to(self, q, vicinity):
        return self.distance_from(q) < vicinity