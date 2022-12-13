import math
from typing import List


class BuildInFunc:
    pass


class Solution:
    def __init__(self, build_in_func: BuildInFunc):
        self.build_in_func = build_in_func

    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        min_matrix = [[1] * n for _ in range(n - 1)]
        min_matrix.append(matrix[-1])  # last one row itself is min

        if n == 1:
            return matrix[0][0]

        for row_idx in range(n-2, -1, -1):  # last one row is done
            for col_idx in range(0, n):
                num_now = matrix[row_idx][col_idx]

                if col_idx == 0:
                    min_matrix[row_idx][col_idx] = min(
                        num_now + min_matrix[row_idx + 1][col_idx],
                        num_now + min_matrix[row_idx + 1][col_idx + 1]
                    )

                elif col_idx == n - 1:
                    min_matrix[row_idx][col_idx] = min(
                        num_now + min_matrix[row_idx + 1][col_idx - 1],
                        num_now + min_matrix[row_idx + 1][col_idx]
                    )

                else:
                    min_matrix[row_idx][col_idx] = min([
                        num_now + min_matrix[row_idx + 1][col_idx - 1],
                        num_now + min_matrix[row_idx + 1][col_idx],
                        num_now + min_matrix[row_idx + 1][col_idx + 1]
                    ])

        return min(min_matrix[0])


def get_test_cases() -> List:  # [(input1, output1), (input2, output2), ...]
    return [
        ([[2, 1, 3], [6, 5, 4], [7, 8, 9]], 13),
        ([[-19, 57], [-40, -5]], -59),
    ]


if __name__ == '__main__':
    test_cases = get_test_cases()

    for t_input, t_output in test_cases:
        built_in_func = BuildInFunc()

        sol = Solution(built_in_func)
        result = sol.minFallingPathSum(t_input)

        print(f'Is min expect ? `{result == t_output}`')
