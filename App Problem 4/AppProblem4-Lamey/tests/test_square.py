import pytest as pytest

from square import Square
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


@pytest.mark.parametrize('width, e_area',
                         [
                             (1, 1),
                             (0.5, 0.25),
                             (5, 25),
                             (3, 9),
                             (0.25, 0.0625)
                         ])
def test_area(width, e_area):
    sq = Square(BASE_POINT, width)
    assert sq.area() == e_area


@pytest.mark.parametrize('width, e_perimeter',
                         [
                             (1, 4),
                             (0.5, 2),
                             (5, 20),
                             (3, 12),
                             (0.25, 1)
                         ])
def test_perimeter(width, e_perimeter):
    sq = Square(BASE_POINT, width)
    assert sq.perimeter() == e_perimeter

    POINTS = [
        BASE_POINT,  #
        Point(1, 2),  #
        Point(0, 1),  #
        Point(1, 0),  #
        Point(-1, 2),  #
        Point(-1, 0),  #
        Point(1, -2),  # 2.5 (1, -2), (3.5, -2), (3.5, 0.5)
        Point(0, -1),  #
        Point(-1, -2),  #
        Point(0.5, 0.75),  #
        Point(-0.5, 0.75),  # 1,7 .25 +
        Point(0.5, -0.75),  #
        Point(-0.5, -0.75)
    ]


@pytest.mark.parametrize('square, e_distance',
                         [
                             (Square(POINTS[0], 1), 0),
                             (Square(POINTS[1], 5), sqrt(5)),
                             (Square(POINTS[2], 2), 1),
                             (Square(POINTS[3], 4), 1),
                             (Square(POINTS[4], 1), 2),
                             (Square(POINTS[5], 0.5), 0.5),
                             (Square(POINTS[6], 2.5), 1),
                             (Square(POINTS[7], 3), 0),
                             (Square(POINTS[8], 1), 1),
                             (Square(POINTS[9], 3), sqrt(0.8125)),
                             (Square(POINTS[10], 1), 0.75),
                             (Square(POINTS[11], 2.25), 0.5),
                             (Square(POINTS[12], 0.5), 0.25)
                         ])
def test_distance_to_origin(square, e_distance):
    sq = square
    assert isclose(sq.distance_from_origin(), e_distance)
