import math
from typing import List


class BuildInFunc:
    pass


class Solution:
    def __init__(self, build_in_func: BuildInFunc):
        self.build_in_func = build_in_func

    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(cost) > sum(gas):
            return -1

        total_dis = len(gas)
        cur_gas = 0
        lowest_gas, lowest_idx = math.inf, None
        for step in range(total_dis):
            if lowest_gas > cur_gas:
                lowest_gas = cur_gas
                lowest_idx = step

            # step -> step + 1
            cur_gas += gas[step] - cost[step]

        cur_gas = 0
        for step in range(total_dis):
            # lowest_idx + step -> lowest_idx + step + 1
            cur_step = (lowest_idx + step) % total_dis
            cur_gas += gas[cur_step] - cost[cur_step]
            if cur_gas < 0:
                return -1

        return lowest_idx


def get_test_cases() -> List:  # [(input1, output1), (input2, output2), ...]
    return [
        (([1, 2, 3, 4, 5], [3, 4, 5, 1, 2]), 3),
        (([2, 3, 4], [3, 4, 3]), -1),
    ]


if __name__ == '__main__':
    test_cases = get_test_cases()

    for t_input, t_output in test_cases:
        built_in_func = BuildInFunc()

        sol = Solution(built_in_func)
        result = sol.canCompleteCircuit(*t_input)

        print(f'Is can complete expect ? `{result == t_output}`')
