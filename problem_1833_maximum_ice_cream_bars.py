from typing import List


class BuildInFunc:
    pass


class Solution:
    def __init__(self, build_in_func: BuildInFunc):
        self.build_in_func = build_in_func

    def maxIceCream(self, costs: List[int], coins: int) -> int:
        sorted_costs = sorted(costs)

        bought_ice_creams = 0
        rest_coins = coins
        for c in sorted_costs:
            if rest_coins >= c:
                rest_coins -= c
                bought_ice_creams += 1
            else:
                break

        return bought_ice_creams


def get_test_cases() -> List:  # [(input1, output1), (input2, output2), ...]
    return [
        (([1, 3, 2, 4, 1], 7), 4),
        (([10, 6, 8, 7, 7, 8], 5), 0),
        (([1, 6, 3, 1, 2, 5], 20), 6),
    ]


if __name__ == '__main__':
    test_cases = get_test_cases()

    for t_input, t_output in test_cases:
        built_in_func = BuildInFunc()

        sol = Solution(built_in_func)
        result = sol.maxIceCream(*t_input)

        print(f'Is delete min expect ? `{result == t_output}`')
