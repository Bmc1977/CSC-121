from rectangle import Rectangle


class Square(Rectangle):
    """
    Represents a square in 2-dimensional Cartesian space.
    """

    def __init__(self, lower_left, width):
        """
        Creates a new square with a given lower-left point and a width.
        :param lower_left: Lower-left point.
        :param width: Width of the square
        """
        super().__init__(lower_left, width, width)

    def is_square(self) -> bool:
        """
        Returns a bool representing if the square is a square.
        :return: True if square.
        """
        return True
