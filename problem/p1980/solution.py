from typing import List


class Solution:
    process_function_str = "findDifferentBinaryString"

    def findDifferentBinaryString(self, nums: List[str]) -> str:
        nums_set = set(nums)
        n = len(nums[0])

        for decimal in range(2 ** n):
            binary = self._decimal_to_binary(decimal, max_dig=n)
            if binary not in nums_set:
                return binary

    @staticmethod
    def _decimal_to_binary(decimal: int, max_dig: int) -> str:
        binary = ""
        rest_decimal = decimal
        for dig in range(max_dig - 1, -1, -1):
            dig_decimal = 2 ** dig
            if rest_decimal >= dig_decimal:
                rest_decimal -= dig_decimal
                binary += "1"
            else:
                binary += "0"

        return binary
