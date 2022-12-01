from typing import List


class BuildInFunc:
    pass


class Solution:
    VOWELS = ['a', 'e', 'i', 'o', 'u']

    def __init__(self, build_in_func: BuildInFunc):
        self.build_in_func = build_in_func

    def halvesAreAlike(self, s: str) -> bool:
        lower_s = s.lower()

        half_len = len(lower_s) // 2
        front_part = lower_s[:half_len]
        behind_part = lower_s[half_len:]

        front_vowel_counts = 0
        behind_vowel_counts = 0
        for f, b in zip(front_part, behind_part):
            if f in self.VOWELS:
                front_vowel_counts += 1

            if b in self.VOWELS:
                behind_vowel_counts += 1

        return front_vowel_counts == behind_vowel_counts


def get_test_cases() -> List:  # [(input1, output1), (input2, output2), ...]
    return [
        ('book', True),
        ('textbook', False),
    ]


if __name__ == '__main__':
    test_cases = get_test_cases()

    for t_input, t_output in test_cases:
        built_in_func = BuildInFunc()

        sol = Solution(built_in_func)
        result = sol.halvesAreAlike(t_input)

        print(f'Is text alike expect ? `{result == t_output}`')
