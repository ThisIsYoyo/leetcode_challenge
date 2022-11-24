from typing import List, Tuple


class BuildInFunc:
    pass


class Solution:
    def __init__(self, build_in_func: BuildInFunc):
        self.build_in_func = build_in_func

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


def get_test_cases() -> List:  # [(input1, output1), (input2, output2), ...]
    return [
        (
            [
                ["5", "3", ".", ".", "7", ".", ".", ".", "."],
                ["6", ".", ".", "1", "9", "5", ".", ".", "."],
                [".", "9", "8", ".", ".", ".", ".", "6", "."],
                ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
                ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
                ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
                [".", "6", ".", ".", ".", ".", "2", "8", "."],
                [".", ".", ".", "4", "1", "9", ".", ".", "5"],
                [".", ".", ".", ".", "8", ".", ".", "7", "9"]
            ],
            True,
        ),
        (
            [
                ["8", "3", ".", ".", "7", ".", ".", ".", "."],
                ["6", ".", ".", "1", "9", "5", ".", ".", "."],
                [".", "9", "8", ".", ".", ".", ".", "6", "."],
                ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
                ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
                ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
                [".", "6", ".", ".", ".", ".", "2", "8", "."],
                [".", ".", ".", "4", "1", "9", ".", ".", "5"],
                [".", ".", ".", ".", "8", ".", ".", "7", "9"]
            ],
            False,
        ),
    ]


if __name__ == '__main__':
    test_cases = get_test_cases()

    for t_input, t_output in test_cases:
        built_in_func = BuildInFunc()

        sol = Solution(built_in_func)
        result = sol.isValidSudoku(t_input)

        print(f'Is board expect ? `{result == t_output}`')
