import math
from typing import List, Tuple


class BuildInFunc:
    pass


class Solution:
    def __init__(self, build_in_func: BuildInFunc):
        self.build_in_func = build_in_func

    def minimumRounds(self, tasks: List[int]) -> int:
        tasks_count_map = {}  # diff: count

        for t in tasks:
            tasks_count_map.setdefault(t, 0)
            tasks_count_map[t] += 1

        min_rounds = 0
        for diff, count in tasks_count_map.items():
            if count == 1:
                return -1

            min_rounds += self.min_diff_rounds(count)

        return min_rounds

    def min_diff_rounds(self, count) -> int:
        if count % 3:
            return count // 3 + 1
        return count // 3


def get_test_cases() -> List:  # [(input1, output1), (input2, output2), ...]
    return [
        ([2, 2, 3, 3, 2, 4, 4, 4, 4, 4], 4),
        ([2, 3, 3], -1),
    ]


if __name__ == '__main__':
    test_cases = get_test_cases()

    for t_input, t_output in test_cases:
        built_in_func = BuildInFunc()

        sol = Solution(built_in_func)
        result = sol.minimumRounds(t_input)

        print(f'Is delete min expect ? `{result == t_output}`')
