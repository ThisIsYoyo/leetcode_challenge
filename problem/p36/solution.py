from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # valid each row
        for row in board:
            if self.is_num_repeat(row):
                return False

        # valid each col
        for c_i in range(9):
            col = [r[c_i] for r in board]

            if self.is_num_repeat(col):
                return False

        # valid area
        for row_center in [1, 4, 7]:
            for col_center in [1, 4, 7]:

                area = []
                for row_i in [row_center - 1, row_center, row_center + 1]:
                    for col_i in [col_center - 1, col_center, col_center + 1]:
                        area.append(board[row_i][col_i])

                if self.is_num_repeat(area):
                    return False

        return True

    @staticmethod
    def is_num_repeat(sudoku_list):
        num_str_list = [num_str for num_str in sudoku_list if num_str != '.']
        if len(num_str_list) != len(set(num_str_list)):
            return True
        return False

