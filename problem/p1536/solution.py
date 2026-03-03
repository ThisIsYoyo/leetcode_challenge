from typing import List


class Solution:
    process_function_str = "minSwaps"

    @staticmethod
    def _count_tailing_zeros(row: List[int]) -> int:
        count = 0
        for i in reversed(row):
            if i != 0:
                break
            count += 1
        return count

    def minSwaps(self, grid: List[List[int]]) -> int:
        n = len(grid)
        trailing_zeros = []  # row_idx: trailing_zero_count

        for row in grid:
            trailing_zeros.append(self._count_tailing_zeros(row))

        swaps = 0
        for i in range(n):
            require_zeros = n - i - 1
            j = i
            while j < n and trailing_zeros[j] < require_zeros:
                j += 1

            if j == n:
                return -1

            while j > i:
                trailing_zeros[j], trailing_zeros[j - 1] = trailing_zeros[j - 1], trailing_zeros[j]
                swaps += 1
                j = j - 1

        return swaps
