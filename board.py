from cell import Cell
from random import randint


class Board:
    def __init__(self, columns, rows):

        self.rows = rows
        self.columns = columns
        self.cycle = 0

        self._grid = [[Cell() for col in range(self.columns)] for row in range(self.rows)]

        self.generate_board()

    def draw_board(self):

        string = 'Cycle number {}\n'.format(self.cycle)

        for rows in self._grid:
            for cell in rows:
                string += cell.get_print_character()
            string += "\n"

        print(string)

    def generate_board(self):

        for row in self._grid:
            for cell in row:
                if randint(0, 2) == 1:
                    cell.set_alive()

    def check_neighbour(self, column, row):

        search_min = -1
        search_max = 2

        neighbour_list = []

        for col in range(search_min, search_max):
            for cell in range(search_min, search_max):
                cell_col = col + column
                cell_row = cell + row

                if cell_row < 0 or cell_row >= self.rows:
                    continue

                if cell_col < 0 or cell_col >= self.columns:
                    continue

                if cell_col == column and cell_row == row:
                    continue

                neighbour_list.append(self._grid[cell_row][cell_col])

        return neighbour_list

    def evolve(self):

        to_live = []
        to_kill = []

        self.cycle += 1

        for row in range(len(self._grid)):
            for col in range(len(self._grid[row])):

                neighbours = self.check_neighbour(column=col, row=row)

                alive_neighbour = 0

                for neighbour in neighbours:
                    if neighbour.is_alive():
                        alive_neighbour += 1

                if self._grid[row][col].is_alive():
                    if alive_neighbour not in [2, 3]:
                        to_kill.append(self._grid[row][col])
                else:
                    if alive_neighbour == 3:
                        to_live.append(self._grid[row][col])

        for cell in to_live:
            cell.set_alive()

        for cell in to_kill:
            cell.set_dead()
