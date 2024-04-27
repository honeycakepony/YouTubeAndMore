# started 27-04-2024
# https://youtu.be/A80YzvNwqXA?si=QyzntaCJTeO0d4PS
# Understanding: # todo
from typing import List
from itertools import product


class Solution:
    SHAPE = 9
    GRID = 3
    EMPTY = '.'
    DIGITS = set([str(num) for num in range(1, SHAPE + 1)])

    def solve_soduko(self, board: List[List[int]]) -> None:
        """No return value, modification have to take happen in-place"""
        self.search(board)

    def is_valid_state(self, board: List[List[int]]) -> bool:
        # validate all rows
        for row in self.get_rows(board):
            if not set(row) == self.DIGITS:
                return False

        # validate all columns
        for col in self.get_columns(board):
            if not set(col) == self.DIGITS:
                return False

        # validate all grids
        for grid in self.get_grids(board):
            if not set(grid) == self.DIGITS:
                return False

        return True

    def get_candidates(self, board: List[List[int]], row, col):
        used_digits = set()
        used_digits.update(self.get_kth_row(board, row))
        used_digits.update(self.get_kth_col(board, col))
        used_digits.update(self.get_grid_at_row_col(board, row, col))
        used_digits -= set([self.EMPTY])
        candidates = self.DIGITS - used_digits
        return candidates

    # todo: continue from 29:10