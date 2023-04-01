from typing import List


class Solution:
    def __init__(self):
        self._cache = {}  # sorted_nums_tuple: unique_permute_result

    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        sorted_nums = sorted(nums)
        if tuple(sorted_nums) in self._cache:
            return self._cache[tuple(sorted_nums)]

        all_unique_permute = []
        if len(sorted_nums) == 1:
            all_unique_permute.append(sorted_nums)
        else:
            be_head_set = set()
            for i, n in enumerate(sorted_nums):
                if n in be_head_set:
                    continue
                be_head_set.add(n)

                other_nums = sorted_nums[:i] + sorted_nums[i + 1:]
                all_unique_permute.extend(
                    [[n] + p for p in self.permuteUnique(other_nums)]
                )

        self._cache.setdefault(tuple(sorted_nums), all_unique_permute)
        return all_unique_permute

