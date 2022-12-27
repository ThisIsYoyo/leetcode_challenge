from typing import List


class BuildInFunc:
    pass


class Solution:
    def __init__(self, build_in_func: BuildInFunc):
        self.build_in_func = build_in_func

    def maximumBags(self, capacity: List[int], rocks: List[int], additionalRocks: int) -> int:
        total_bag_num = len(capacity)

        max_bags = 0
        additional_rest_rocks = additionalRocks
        remain_capacity = [capacity[i] - rocks[i] for i in range(total_bag_num)]
        for remain_c in sorted(remain_capacity):
            if additional_rest_rocks >= remain_c:
                additional_rest_rocks -= remain_c
                max_bags += 1
            else:
                break

        return max_bags


def get_test_cases() -> List:  # [(input1, output1), (input2, output2), ...]
    return [
        (([2, 3, 4, 5], [1, 2, 4, 4], 2), 3),
        (([10, 2, 2], [2, 2, 0], 100), 3),
    ]


if __name__ == '__main__':
    test_cases = get_test_cases()

    for t_input, t_output in test_cases:
        built_in_func = BuildInFunc()
        capacity, rocks, addi_rocks = t_input

        sol = Solution(built_in_func)
        result = sol.maximumBags(capacity, rocks, addi_rocks)

        print(f'Is max bags expect ? `{result == t_output}`')
