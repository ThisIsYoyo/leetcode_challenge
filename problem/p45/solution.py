from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return 0

        jump_times = 0
        next_could_reach_max_idx = nums[0] if nums[0] < n else n - 1
        checked_reach_pointer_idx = 0

        while next_could_reach_max_idx < n - 1:
            max_reach_idx = 0
            for need_check_idx in range(checked_reach_pointer_idx + 1, next_could_reach_max_idx + 1):
                check_idx_max_reach_idx = need_check_idx + nums[need_check_idx]
                max_reach_idx = max(check_idx_max_reach_idx, max_reach_idx)
                max_reach_idx = max_reach_idx if max_reach_idx < n else n - 1
            jump_times += 1

            checked_reach_pointer_idx = next_could_reach_max_idx
            next_could_reach_max_idx = max_reach_idx

        return jump_times + 1

