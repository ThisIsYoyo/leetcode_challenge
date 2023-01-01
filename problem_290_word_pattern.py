from typing import List


class BuildInFunc:
    pass


class Solution:
    def __init__(self, build_in_func: BuildInFunc):
        self.build_in_func = build_in_func

    def wordPattern(self, pattern: str, s: str) -> bool:
        s_split_list = s.split()

        if len(pattern) != len(s_split_list):
            return False

        pattern_map = {}  # letter: string
        for p, ss in zip(pattern, s_split_list):
            map_string = pattern_map.get(p)

            if not map_string:
                # if string already map in other pattern, not allow to remember it
                if ss in pattern_map.values():
                    return False

                # first appear string, remember it
                pattern_map[p] = ss
            else:
                if map_string != ss:
                    return False

        return True


def get_test_cases() -> List:  # [(input1, output1), (input2, output2), ...]
    return [
        (('abba', 'dog cat cat dog'), True),
        (('abba', 'dog cat cat fish'), False),
        (('aaaa', 'dog cat cat dog'), False)
    ]


if __name__ == '__main__':
    test_cases = get_test_cases()

    for t_input, t_output in test_cases:
        built_in_func = BuildInFunc()

        sol = Solution(built_in_func)
        result = sol.wordPattern(*t_input)

        print(f'Is order expect ? `{result == t_output}`')
