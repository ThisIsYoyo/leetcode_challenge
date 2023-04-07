from typing import List, Tuple


class Solution:
    def __init__(self):
        self._grid = None

    def numEnclaves(self, grid: List[List[int]]) -> int:
        self._grid = grid
        row_len = len(grid)
        col_len = len(grid[0])

        # turn closed to boundary island to sea
        for row_i in [0, row_len - 1]:
            for col_j in range(col_len):
                if self._grid[row_i][col_j] == 0:
                    continue

                self._turn_to_sea_with_related_island((row_i, col_j))

        for col_j in [0, col_len - 1]:
            for row_i in range(row_len):
                if self._grid[row_i][col_j] == 0:
                    continue

                self._turn_to_sea_with_related_island((row_i, col_j))

        return sum(sum(row) for row in self._grid)

    def _turn_to_sea_with_related_island(self, coor: Tuple[int, int]):
        row_len = len(self._grid)
        col_len = len(self._grid[0])

        up__coor = coor[0] - 1, coor[1]
        down_coor = coor[0] + 1, coor[1]
        left_coor = coor[0], coor[1] - 1
        right_coor = coor[0], coor[1] + 1

        # turn to sea
        self._grid[coor[0]][coor[1]] = 0

        # check related
        for sur__coor in [up__coor, down_coor, left_coor, right_coor]:
            if not (0 <= sur__coor[0] < row_len and 0 <= sur__coor[1] < col_len):
                # check illegal coordinate
                continue

            if self._grid[sur__coor[0]][sur__coor[1]] == 0:
                # sea
                continue

            # island
            self._turn_to_sea_with_related_island(sur__coor)

