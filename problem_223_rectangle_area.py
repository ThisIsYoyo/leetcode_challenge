from typing import List


class BuildInFunc:
    pass


class Solution:
    def __init__(self, build_in_func: BuildInFunc):
        self.build_in_func = build_in_func

    def computeArea(self, ax1: int, ay1: int, ax2: int, ay2: int, bx1: int, by1: int, bx2: int, by2: int) -> int:
        area_a = abs(ax1 - ax2) * abs(ay1 - ay2)
        area_b = abs(bx1 - bx2) * abs(by1 - by2)

        x_inter_len = self.inter_len(ax1, ax2, bx1, bx2)
        y_inter_len = self.inter_len(ay1, ay2, by1, by2)
        area_inter = x_inter_len * y_inter_len

        return area_a + area_b - area_inter

    @staticmethod
    def inter_len(a1: int, a2: int, b1: int, b2: int):
        a_min, a_max = min(a1, a2), max(a1, a2)
        b_min, b_max = min(b1, b2), max(b1, b2)

        inter_len = -1  # first time only touch
        for a in range(a_min, a_max + 1):
            if b_min <= a <= b_max:
                inter_len += 1

        return inter_len if inter_len >= 0 else 0


def get_test_cases() -> List:  # [(input1, output1), (input2, output2), ...]
    return [
        ((-3, 0, 3, 4, 0, -1, 9, 2), 45),
        ((-2, -2, 2, 2, -2, -2, 2, 2), 16),
    ]


if __name__ == '__main__':
    test_cases = get_test_cases()

    for t_input, t_output in test_cases:
        built_in_func = BuildInFunc()

        sol = Solution(built_in_func)
        area_result = sol.computeArea(*t_input)

        print(f'Is area right? `{area_result == t_output}`')
