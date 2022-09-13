from column import Column
from stone import Stone
from result import Result

# Number of stones needed to win
WIN_NUM = 4
# Number for checking full range of win range
WIN_RANGE = (WIN_NUM * 2) - 1


class Grid:
    """
    Class that represents the game board of a connect 4 game. Board's
    functionality includes dropping stones, checking for win-condition(s),
    and increasing the board's size when a player drops a stone in a full
    column.
    """
    def __init__(self, height=7, length=6):
        """
        :param height: 'Up and down' height of the board.
        :param length: 'across' length of the board.
        """
        self.columns = []
        self.height = height
        self.length = length
        for i in range(length):
            self.columns.append(Column(height))

    def stone_at(self, x, y):
        """
        Gets the stone at specified location.
        :param x: column
        :param y: row
        :return: Stone at specified location.
        """
        return self.columns[x].get_cell(y)

    def checkNS(self, pos, color, y_loc):
        """
        Checks for winning number in the 'Up-Down' direction.
        :param pos: column number of the dropped stone
        :param color: color of the dropped stone
        :param y_loc: row number of the dropped stone
        :return: A boolean representing if the winning number was reached.
        """
        num_in_row = 0
        if y_loc <= (WIN_NUM - 1):
            for i in range(WIN_NUM):
                if self.stone_at(pos, y_loc + i) == color[0]:
                    num_in_row += 1
                    if num_in_row >= WIN_NUM:
                        return True
                else:
                    num_in_row = 0
        else:
            for i in range(WIN_RANGE):
                if self.stone_at(pos, (y_loc - (WIN_NUM - 1) + i)) == color[0]:
                    num_in_row += 1
                    if num_in_row >= WIN_NUM:
                        return True
                else:
                    num_in_row = 0

        return False

    def checkEW(self, pos, color, y_loc):
        """
        Checks for winning number in the 'across' direction.
        :param pos: column number of the dropped stone
        :param color: color of the dropped stone
        :param y_loc: row number of the dropped stone
        :return: A boolean representing if the winning number was reached.
        """
        num_in_row = 0
        if pos < (WIN_NUM - 1):
            for i in range(WIN_NUM):
                if (pos + i) < self.length:
                    if self.stone_at(pos + i, y_loc) == color[0]:
                        num_in_row += 1
                        if num_in_row >= WIN_NUM:
                            return True
                    else:
                        num_in_row = 0
        else:
            for i in range(WIN_RANGE):
                col_pos = pos - (WIN_NUM - 1)
                if ((col_pos + i) < self.length) and (self.stone_at(col_pos + i, y_loc) == color[0]):
                    num_in_row += 1
                    if num_in_row >= WIN_NUM:
                        return True
                else:
                    num_in_row = 0
        return False

    def checkSWNE(self, pos, color, y_loc):
        """
        Checks for winning number in the 'bottom-left to top-right'
        direction.
        :param pos: column number of the dropped stone
        :param color: color of the dropped stone
        :param y_loc: row number of the dropped stone
        :return: A boolean representing if the winning number was reached.
        """
        num_in_row = 0
        if (pos - (WIN_NUM - 1) < 0) and (y_loc - (WIN_NUM - 1) < 0):
            for i in range(WIN_NUM):
                if self.stone_at((pos + i), (y_loc + i)) == color[0]:
                    num_in_row += 1
                    if num_in_row >= WIN_NUM:
                        return True
        else:
            for i in range(WIN_RANGE):
                if (((pos - (WIN_NUM - 1)) + i) < self.length) and ((y_loc + (WIN_NUM - 1)) - i) < self.height:
                    if self.stone_at(((pos - (WIN_NUM - 1)) + i), ((y_loc + (WIN_NUM - 1)) - i)) == color[0]:
                        num_in_row += 1
                        if num_in_row >= WIN_NUM:
                            return True
                    else:
                        num_in_row = 0
        return False

    def checkNWSE(self, pos, color, y_loc):
        """
                Checks for winning number in the 'top-left to bottom-right'
                direction.
                :param pos: column number of the dropped stone
                :param color: color of the dropped stone
                :param y_loc: row number of the dropped stone
                :return: A boolean representing if the winning number was reached.
                """
        num_in_row = 0
        if (pos - (WIN_NUM - 1) < 0) and (y_loc + (WIN_NUM - 1) > self.height):
            for i in range(WIN_NUM):
                if self.stone_at((pos + i), (y_loc - i)) == color[0]:
                    num_in_row += 1
                    if num_in_row >= WIN_NUM:
                        return True
                else:
                    num_in_row = 0
        else:
            for i in range(WIN_RANGE):
                new_y_pos = (y_loc + (WIN_NUM - 1)) + i
                if (((pos - (WIN_NUM - 1)) + i) < self.length) and (0 < new_y_pos < self.height):
                    if self.stone_at(((pos - (WIN_NUM - 1)) + i), ((y_loc - (WIN_NUM - 1)) + i)) == color[0]:
                        num_in_row += 1
                        if num_in_row >= WIN_NUM:
                            return True
        return False

    def check_four(self, pos, color, y_loc):
        '''
        Checks if the player connected the winning length
        :param pos: column number of the dropped stone
        :param color: color of the dropped stone
        :param y_loc: row number of the dropped stone
        :return: A boolean representing if the winning number was reached.
        '''
        return (self.checkNS(pos, color, y_loc) or self.checkEW(pos, color, y_loc) or
                self.checkNWSE(pos, color, y_loc) or self.checkSWNE(pos, color, y_loc))

    def drop(self, player, pos):
        """
        Is by the driver program when a user takes their turn.
        :param player: The color of the player
        :param pos: The column the player dropped their stone in.
        :return: The result of the player's turn.
        """
        if pos > self.length:
            return Result.ILLEGAL
        if self.columns[pos - 1].is_full():
            for col in self.columns:
                col.increase_size()
            self.height += 1
        if player == "Red":
            y_loc = self.columns[pos - 1].add_stone(Stone('R'))
        else:
            y_loc = self.columns[pos - 1].add_stone(Stone('B'))

        if self.check_four(pos - 1, player, y_loc):
            return Result.WIN

        return Result.LEGAL

    def __str__(self):
        """
        :return: String representation of the game board.
        """
        returnable = ''
        for i in range(self.height):
            for col in self.columns:
                returnable += col.get_cell(i) + " "
            returnable += f'\n'
        return returnable
