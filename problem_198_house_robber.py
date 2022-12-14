from typing import List


class BuildInFunc:
    pass


class Solution:
    def __init__(self, build_in_func: BuildInFunc):
        self.build_in_func = build_in_func
        self._cache = {}

    def rob(self, nums: List[int]) -> int:
        cache_search_key = tuple(nums)

        if tuple(cache_search_key) in self._cache:
            return self._cache[tuple(cache_search_key)]

        if len(nums) < 3:
            max_rob = max(nums)
        elif len(nums) == 3:
            max_rob = max(nums[0] + nums[2], nums[1])
        else:
            max_rob = max(
                nums[0] + self.rob(nums[2:]),
                nums[1] + self.rob(nums[3:])
            )

        self._cache.setdefault(cache_search_key, max_rob)
        return max_rob


def get_test_cases() -> List:  # [(input1, output1), (input2, output2), ...]
    return [
        ([1, 2, 3, 1], 4),
        ([2, 7, 9, 3, 1], 12),
    ]


if __name__ == '__main__':
    test_cases = get_test_cases()

    for t_input, t_output in test_cases:
        built_in_func = BuildInFunc()

        sol = Solution(built_in_func)
        result = sol.rob(t_input)

        print(f'Is max expect ? `{result == t_output}`')
