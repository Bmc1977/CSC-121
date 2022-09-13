class Column:
    """
    Class to represent a column in a connect 4 game board.
    """
    def __init__(self, size):
        """
        :param size: Height of the game board.
        """
        self.cells = []
        self.size = size
        for i in range(size):
            self.cells.append('-')

    def get_size(self):
        """
        :return: Height of the column
        """
        return self.size

    def get_cells(self):
        """
        Returns the contents of the column.
        :return: List of contents of the column.
        """
        return self.cells

    def increase_size(self):
        """
        Increases the size of the column. Used for when a player drops a
        stone in a full column.
        """
        self.cells.append('-')
        self.size += 1

    def get_cell(self, pos):
        """
        Returns the contents of a specific cell in the column.
        :param pos: The desired location within the column.
        :return: The contents at the specified position.
        """
        return self.cells[pos]

    def __str__(self):
        """
        String representation of the column.
        :return: String representing the column.
        """
        returnable = ''
        for cell in self.cells:
            returnable = returnable + f' {cell}'
        return returnable

    def is_full(self):
        """
        This will be more of a utility function now that the board can grow.
        """
        if '-' in self.cells:
            return False

        return True

    def add_stone(self, stone):
        """
        Used in the 'dropping' of a stone. Places the stone in the 'lowest'
        unfilled cell within the column.
        :param stone: Stone that is being dropped.
        :return: The position in the column where the stone lands.
        """
        for i in range(len(self.cells)):
            if self.cells[(i + 1) * -1] == '-':
                self.cells[(i + 1) * -1] = stone.__str__()
                return (i + 1) * -1
