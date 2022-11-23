import math
import time
from typing import List, Tuple


class BuildInFunc:
    pass


class Solution:
    def __init__(self, build_in_func: BuildInFunc):
        self.build_in_func = build_in_func
        self._cache = {  # n: min_times
            1: 1,
            4: 1,
            9: 1,
            16: 1,
            25: 1,
            36: 1,
            49: 1,
            64: 1,
            81: 1,
            100: 1,
        }

    def numSquares(self, n: int) -> int:
        if n in self._cache:
            return self._cache[n]

        max_square_len = int(math.sqrt(n))

        min_times = math.inf
        for square_len in range(max_square_len, 0, -1):
            # init
            copy_n = n
            square = square_len ** 2
            times = 0

            # caculate
            while copy_n >= square:
                copy_n -= square
                times += 1

            if copy_n:
                times += self.numSquares(copy_n)

            if times < min_times:
                min_times = times

        self._cache[n] = min_times
        return min_times


def get_test_cases() -> List:  # [(input1, output1), (input2, output2), ...]
    return [
        # (12, 3),
        # (13, 2),
        (4635, 3),
    ]


if __name__ == '__main__':
    test_cases = get_test_cases()

    for t_input, t_output in test_cases:
        built_in_func = BuildInFunc()

        sol = Solution(built_in_func)

        _t = time.time()
        result = sol.numSquares(t_input)
        print(f'spend {time.time() - _t}s')

        print(f'Is num expect ? `{result == t_output}`')
