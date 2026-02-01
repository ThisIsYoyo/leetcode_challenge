import math


class Solution:
    process_function_str = "canCompleteCircuit"

    def canCompleteCircuit(self, gas: list[int], cost: list[int]) -> int:
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
