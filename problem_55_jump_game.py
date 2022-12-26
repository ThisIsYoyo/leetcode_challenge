from typing import List


class BuildInFunc:
    pass


class Solution:
    def __init__(self, build_in_func: BuildInFunc):
        self.build_in_func = build_in_func

    def canJump(self, nums: List[int]) -> bool:
        last_idx = len(nums) - 1

        cur_idx = 0
        cur_can_jump = nums[0]
        while cur_can_jump > 0:
            if cur_idx + cur_can_jump >= last_idx:
                return True

            cur_can_jump_nums = []
            for cur_can_jump_idx in range(1, cur_can_jump + 1):
                cur_can_jump_nums.append(nums[cur_idx + cur_can_jump_idx] + cur_can_jump_idx)

            cur_max_can_jump = max(cur_can_jump_nums)
            next_idx = cur_idx + cur_can_jump
            next_can_jump = cur_max_can_jump - cur_can_jump

            cur_idx = next_idx
            cur_can_jump = next_can_jump

        return False


def get_test_cases() -> List:  # [(input1, output1), (input2, output2), ...]
    return [
        # ([2, 3, 1, 1, 4], True),
        # ([3, 2, 1, 0, 4], False),
        ([1, 1, 1, 0], True)
    ]


if __name__ == '__main__':
    test_cases = get_test_cases()

    for t_input, t_output in test_cases:
        built_in_func = BuildInFunc()

        sol = Solution(built_in_func)
        result = sol.canJump(t_input)

        print(f'Is capability expect ? `{result == t_output}`')
