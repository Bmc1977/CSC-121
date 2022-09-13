class Stone:
    """
    Class to represent a "stone" in a connect 4 game.
    """
    def __init__(self, color):
        """
        :param color: Color of the stone.
        """
        self.color = color

    def __str__(self):
        """
        String representation of the stone for the game board.
        :return: The first letter of the stone's color
        """
        return self.color[0]
