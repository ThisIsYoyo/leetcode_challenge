import math
from typing import List, Tuple


class BuildInFunc:
    pass


class Solution:
    def __init__(self, build_in_func: BuildInFunc):
        self.build_in_func = build_in_func

    def detectCapitalUse(self, word: str) -> bool:
        first_letter = word[0]

        if len(word) == 1:
            return True

        is_upper_after_first = None
        for l in word[1:]:
            if is_upper_after_first is not None:
                if (is_upper_after_first and l.islower()) or (not is_upper_after_first and l.isupper()):
                    return False
            else:
                if first_letter.isupper() and l.isupper():
                    is_upper_after_first = True
                elif l.islower():
                    is_upper_after_first = False
                else:
                    return False

        return True


def get_test_cases() -> List:  # [(input1, output1), (input2, output2), ...]
    return [
        ('USA', True),
        ('FlaG', False),
    ]


if __name__ == '__main__':
    test_cases = get_test_cases()

    for t_input, t_output in test_cases:
        built_in_func = BuildInFunc()

        sol = Solution(built_in_func)
        result = sol.detectCapitalUse(t_input)

        print(f'Is delete min expect ? `{result == t_output}`')
