from __future__ import annotations

from point import Point
from math import sqrt


class Rectangle:
    """
    Represents a rectangle in 2-dimensional Cartesian space.
    """

    def __init__(self, lower_left, width, length):
        """
        Creates a rectangle with a lower left point, width, and length.
        :param lower_left: Lower-left point of the rectangle.
        :param width: x-width of the rectangle.
        :param length: y-length of the rectangle
        """
        self._lower_left = lower_left
        self._width = width
        self._length = length

        self.crosses_axis = self.axis_intersection()

    def axis_intersection(self):
        """
        Tests if the rectangle crosses either of the axis.
        :return: bool representing if the rectangle cross the x or y axis.
        """
        if self.lower_left.x < 0 and (self.lower_left.x + self.width) > 0:
            return True
        elif self.lower_left.y < 0 and (self.lower_left.y + self.length) > 0:
            return True

        return False

    def y_axis_intersection(self):
        """
        Tests whether the rectangle crosses the y axis
        :return: bool representing if the rectangle crosses the y axis
        """
        return self.lower_left.x < 0 and (self.lower_left.x + self.width) > 0

    def x_axis_intersection(self):
        """
        Tests whether the rectangle crosses the x axis.
        :return: bool representing if the rectangle crosses the x axis
        """
        return self.lower_left.y < 0 and (self.lower_left.y + self.length) > 0

    def get_lower_left(self) -> Point:
        return self._lower_left

    def set_lower_left(self, point):
        self._lower_left = point

    def get_width(self) -> float:
        return self._width

    def set_width(self, width):
        self._width = width

    def get_length(self) -> float:
        return self._length

    def set_length(self, length):
        self._length = length

    # Creating the class properties
    lower_left = property(get_lower_left, set_lower_left)
    width = property(get_width, set_width)
    length = property(get_length, set_length)

    def area(self) -> float:
        """
        :return: Returns the area of the rectangle.
        """
        return self.width * self.length

    def perimeter(self) -> float:
        """
        :return: Returns the perimeter of the rectangle.
        """
        return (self.length * 2) + (self.width * 2)

    def is_square(self) -> bool:
        """
        :return: Returns a bool representing if the rectangle is a square.
        """
        return self.length == self.width

    def distance_from_origin(self) -> float:
        """
        Returns the closes distance from the origin a rectangle is.
        :return: Returns a float representing the distance from the origin
                to the closest corner.
        """
        if not self.crosses_axis:
            origin = Point(0, 0)
            all_points = [self.lower_left, Point(self.lower_left.x + self.width, self.lower_left.y),
                          Point(self.lower_left.x, self.lower_left.y + self.length),
                          Point(self.lower_left.x + self.width, self.lower_left.y + self.length)]
            distances = []
            for point in all_points:
                distances.append(point.distance_from(origin))

            return min(distances)
        else:
            if self.x_axis_intersection():
                return abs(self.lower_left.x)
            elif self.y_axis_intersection():
                return abs(self.lower_left.y)

    def __str__(self) -> str:
        """
        :return: A string representation of the rectangle.
        """
        return f'({self.lower_left.x}, {self.lower_left.y}) Width: {self.width} Length: {self.length}'
