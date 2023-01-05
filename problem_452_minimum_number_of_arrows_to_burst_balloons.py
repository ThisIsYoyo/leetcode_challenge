from typing import List, Union


class BuildInFunc:
    pass


class Solution:
    def __init__(self, build_in_func: BuildInFunc):
        self.build_in_func = build_in_func

    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort()

        min_shots = len(points)
        cur_idx = 0
        while cur_idx < len(points):
            sub_dis = points[cur_idx]

            for aft_idx in range(cur_idx + 1, len(points)):
                new_intersect_dis = self.intersect_dis(sub_dis, points[aft_idx])
                if new_intersect_dis is None:
                    cur_idx = aft_idx
                    break

                sub_dis = new_intersect_dis
                min_shots -= 1
            else:
                break

        return min_shots

    @staticmethod
    def intersect_dis(point_pair_a: List[int], point_pair_b: List[int]) -> Union[List[int], None]:
        inter_l = max(point_pair_a[0], point_pair_b[0])
        inter_h = min(point_pair_a[1], point_pair_b[1])

        if inter_l <= inter_h:
            return [inter_l, inter_h]
        return None


def get_test_cases() -> List:  # [(input1, output1), (input2, output2), ...]
    return [
        ([[10, 16], [2, 8], [1, 6], [7, 12]], 2),
        ([[1, 2], [3, 4], [5, 6], [7, 8]], 4),
        ([[1, 2], [2, 3], [3, 4], [4, 5]], 2),
    ]


if __name__ == '__main__':
    test_cases = get_test_cases()

    for t_input, t_output in test_cases:
        built_in_func = BuildInFunc()

        sol = Solution(built_in_func)
        result = sol.findMinArrowShots(t_input)

        print(f'Is delete min expect ? `{result == t_output}`')
