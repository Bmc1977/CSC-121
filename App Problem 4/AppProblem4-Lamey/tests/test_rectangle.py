import pytest as pytest

from rectangle import Rectangle
from point import Point

from math import sqrt, isclose

BASE_POINT = Point(0, 0)
POINTS = [
    BASE_POINT,
    Point(1, 2),
    Point(0, 1),
    Point(1, 0),
    Point(-1, 2),
    Point(-1, 0),
    Point(1, -2),
    Point(0, -1),
    Point(-1, -2),
    Point(0.5, 0.75),
    Point(-0.5, 0.75),
    Point(0.5, -0.75),
    Point(-0.5, -0.75)
]


@pytest.mark.parametrize('width, length, e_area',
                         [
                             (1, 1, 1),
                             (0.5, 0.5, 0.25),
                             (5, 5, 25),
                             (3, 4, 12),
                             (0.25, 0.75, 0.1875)
                         ])
def test_area(width, length, e_area):
    rect = Rectangle(BASE_POINT, width, length)
    assert rect.area() == e_area


@pytest.mark.parametrize('width, length, e_perimeter',
                         [
                             (1, 1, 4),
                             (0.5, 0.5, 2),
                             (5, 5, 20),
                             (3, 4, 14),
                             (0.25, 0.75, 2)
                         ])
def test_perimeter(width, length, e_perimeter):
    rect = Rectangle(BASE_POINT, width, length)
    assert rect.perimeter() == e_perimeter


@pytest.mark.parametrize('width, length, sq',
                         [
                             (1, 1, True),
                             (1.5, 1.5, True),
                             (3, 4, False),
                             (5, 5, True),
                             (0.5, 0.5, True),
                             (2.5, 3.5, False)
                         ])
def test_is_square(width, length, sq):
    rect = Rectangle(BASE_POINT, width, length)
    assert rect.is_square() == sq


@pytest.mark.parametrize('rectangle, e_distance',
                         [
                             (Rectangle(POINTS[0], 1, 1), 0),
                             (Rectangle(POINTS[1], 5, 5), sqrt(5)),
                             (Rectangle(POINTS[2], 2, 3), 1),
                             (Rectangle(POINTS[3], 4, 7), 1),
                             (Rectangle(POINTS[4], 0.5, 3), sqrt(4.25)),
                             (Rectangle(POINTS[5], 0.5, 3), 0.5),
                             (Rectangle(POINTS[6], 2.5, 3), 1),
                             (Rectangle(POINTS[7], 3, 1), 0),
                             (Rectangle(POINTS[8], 1, 1), 1),
                             (Rectangle(POINTS[9], 3, 9), sqrt(0.8125)),
                             (Rectangle(POINTS[10], 1, 7), 0.75),
                             (Rectangle(POINTS[11], 2.25, 0.75), 0.5),
                             (Rectangle(POINTS[12], 0.5, 0.75), 0)

                         ])
def test_distance_to_origin(rectangle, e_distance):
    rect = rectangle
    assert isclose(rect.distance_from_origin(), e_distance)
