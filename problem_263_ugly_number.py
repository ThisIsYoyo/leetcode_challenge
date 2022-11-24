from typing import List


class BuildInFunc:
    pass


class Solution:
    def __init__(self, build_in_func: BuildInFunc):
        self.build_in_func = build_in_func

    def isUgly(self, n: int) -> bool:
        if n <= 0:
            return False

        iter_n = n
        while True:
            if iter_n <= 1:
                return True

            last_dig = iter_n % 10
            if last_dig % 2 == 0:
                iter_n = iter_n // 2
                continue

            if last_dig == 5:
                iter_n = iter_n // 5
                continue

            if iter_n % 3 == 0:
                iter_n = iter_n // 3
                continue

            return False


def get_test_cases() -> List:  # [(input1, output1), (input2, output2), ...]
    return [
        (6, True),
        (1, True),
        (14, False),
        (-2147483648, False),
    ]


if __name__ == '__main__':
    test_cases = get_test_cases()

    for t_input, t_output in test_cases:
        built_in_func = BuildInFunc()

        sol = Solution(built_in_func)
        is_ugly = sol.isUgly(t_input)

        print(f'Is num expect ? `{is_ugly == t_output}`')
