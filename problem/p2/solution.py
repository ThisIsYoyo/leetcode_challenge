class Solution:
    process_function_str = "twoSum"

    def twoSum(self, nums: list[int], target: int) -> list[int]:
        num_to_idx = {}
        for idx, num in enumerate(nums):
            rest = target - num
            if rest in num_to_idx:
                return [num_to_idx[rest], idx]

            num_to_idx[num] = idx
