from typing import List


class BuildInFunc:
    pass


class Solution:
    def __init__(self, build_in_func: BuildInFunc):
        self.build_in_func = build_in_func
        self._cache = {}

    def climbStairs(self, n: int) -> int:
        if n in self._cache:
            return self._cache[n]

        if n <= 1:
            return 1

        self._cache.setdefault(n, self.climbStairs(n - 1) + self.climbStairs(n - 2))
        return self._cache[n]


def get_test_cases() -> List:  # [(input1, output1), (input2, output2), ...]
    return [
        (2, 2),
        (3, 3),
    ]


if __name__ == '__main__':
    test_cases = get_test_cases()

    for t_input, t_output in test_cases:
        built_in_func = BuildInFunc()

        sol = Solution(built_in_func)
        result = sol.climbStairs(t_input)

        print(f'Is combinations expect ? `{result == t_output}`')
