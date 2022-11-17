from typing import List


class BuildInFunc:
    def __init__(self, pick):
        self.pick = pick

    def guess(self, num: int) -> int:
        if num > self.pick:
            return -1
        if num < self.pick:
            return 1
        if num == self.pick:
            return 0


class Solution:
    GREATER_THAN_PICK = -1
    LESS_THAN_PICK = 1
    EQUAL_TO_PICK = 0

    def __init__(self, build_in_func: BuildInFunc):
        self.build_in_func = build_in_func

    def guessNumber(self, n: int) -> int:
        if n == 1:
            return 1

        i = 1  # lower index
        j = n  # high index
        while i < j:
            mid = (i + j) // 2

            guess_result = self.build_in_func.guess(mid)
            if guess_result == self.GREATER_THAN_PICK:
                j = mid if j != mid else mid - 1
            elif guess_result == self.LESS_THAN_PICK:
                i = mid if i != mid else mid + 1
            elif guess_result == self.EQUAL_TO_PICK:
                return mid

        assert i == j
        return i


def get_test_cases() -> List:  # [(input1, output1), (input2, output2), ...]
    return [
        ((10, 6), 6),
        ((1, 1), 1),
        ((2, 1), 1),
    ]


if __name__ == '__main__':
    test_cases = get_test_cases()

    for t_input, t_output in test_cases:
        n, pick = t_input

        built_in_func = BuildInFunc(pick=pick)

        sol = Solution(built_in_func)
        guess_result = sol.guessNumber(n=n)

        print(f'Is guess right? `{guess_result == t_output}`')
