from typing import List


class Solution:
    def __init__(self):
        self._cache = {}  # sorted_nums_tuple: permute_result

    def permute(self, nums: List[int]) -> List[List[int]]:
        sorted_nums = sorted(nums)
        if tuple(sorted_nums) in self._cache:
            return self._cache[tuple(sorted_nums)]

        all_permute = []
        if len(sorted_nums) == 1:
            all_permute.append(sorted_nums)
        else:
            for i, n in enumerate(sorted_nums):
                other_nums = sorted_nums[:i] + sorted_nums[i + 1:]
                all_permute.extend(
                    [[n] + p for p in self.permute(other_nums)]
                )

        self._cache.setdefault(tuple(sorted_nums), all_permute)
        return all_permute

