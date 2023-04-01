from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        start = 0
        end = len(nums) - 1

        while start < end:
            mid = (start + end) // 2

            if nums[mid] > target:
                end = mid
            elif nums[mid] < target:
                start = mid if start != mid else mid + 1
            else:
                return mid

        assert start == end
        return (nums[start] == target and start) or -1
