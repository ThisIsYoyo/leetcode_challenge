import math
from typing import List, Tuple, Union


class BuildInFunc:
    pass


class Solution:
    def __init__(self, build_in_func: BuildInFunc):
        self.build_in_func = build_in_func

    def maxPoints(self, points: List[List[int]]) -> int:
        points_set = set([tuple(p) for p in points])

        linear_count_map = {}  # a, b, c(ax + by = c): count
        checked_points = set()
        for p in points_set:
            checked_points.add(p)

            for other_p in points_set - checked_points:
                a, b, c = self.solve_equation(p, other_p)
                linear_count_map.setdefault((a, b, round(c, 2)), 0)
                linear_count_map[(a, b, round(c, 2))] += 1

        return int(
            math.sqrt(
                2 * max([c for _, c in linear_count_map.items()])
            )
        ) + 1

    @staticmethod
    def solve_equation(
            p1: Tuple[int, int], p2: Tuple[int, int]
    ) -> Tuple[Union[int, float], int, Union[int, float]]:  # ax + by = c
        if p1[0] == p2[0]:
            a, b, c = 1, 0, p1[0]
        elif p1[1] == p2[1]:
            a, b, c = 0, 1, p1[1]
        else:
            a = (p2[1] - p1[1]) / (p1[0] - p2[0])
            b = 1
            c = a * p1[0] + p1[1]

        return a, b, c


def get_test_cases() -> List:  # [(input1, output1), (input2, output2), ...]
    return [
        # ([[1, 1], [2, 2], [3, 3]], 3),
        # ([[1, 1], [3, 2], [5, 3], [4, 1], [2, 3], [1, 4]], 4),
        ([
             [-184, -551], [-105, -467], [-90, -394], [-60, -248], [115, 359], [138, 429], [60, 336], [150, 774],
             [207, 639], [-150, -686], [-135, -613], [92, 289], [23, 79], [135, 701], [0, 9], [-230, -691],
             [-115, -341], [-161, -481], [230, 709], [-30, -102]
         ], 11)
    ]


if __name__ == '__main__':
    test_cases = get_test_cases()

    for t_input, t_output in test_cases:
        built_in_func = BuildInFunc()

        sol = Solution(built_in_func)
        result = sol.maxPoints(t_input)

        print(f'Is can complete expect ? `{result == t_output}`')
