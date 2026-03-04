from typing import List


class Solution:
    process_function_str = "numSpecial"

    def numSpecial(self, mat: List[List[int]]) -> int:
        m = len(mat)
        n = len(mat[0])

        row_sum = [0] * m
        col_sum = [0] * n

        for i in range(m):
            for j in range(n):
                row_sum[i] += mat[i][j]
                col_sum[j] += mat[i][j]

        return sum(
            mat[i][j] == 1 and row_sum[i] == 1 and col_sum[j] == 1
            for i in range(m)
            for j in range(n)
        )
