from typing import List


class BuildInFunc:
    pass


class Solution:
    def __init__(self, build_in_func: BuildInFunc):
        self.build_in_func = build_in_func
        self.person_belong_to_map = []  # [person_id]: belong set
        self.last_dislike_history = []  # [person_id]: last dislike

    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        # init
        self.person_belong_to_map = [set()] * (n + 1)
        self.last_dislike_history = [0] * (n + 1)

        for dislike in dislikes:
            d1, d2 = dislike

            d1_belong_set = self.person_belong_to_map[d1]
            d2_belong_set = self.person_belong_to_map[d2]

            d1_last_dislike_history = self.last_dislike_history[d1]
            d2_last_dislike_history = self.last_dislike_history[d2]

            if not d1_belong_set and not d2_belong_set:
                self.person_belong_to_map[d1] = {d1}
                self.person_belong_to_map[d2] = {d2}
            elif not d1_belong_set and d2_belong_set:
                if d1 in d2_belong_set:
                    return False

                d2_dislike_set = self.person_belong_to_map[d2_last_dislike_history]
                d2_dislike_set.add(d1)
                self.person_belong_to_map[d1] = d2_dislike_set
            elif d1_belong_set and not d2_belong_set:
                if d2 in d1_belong_set:
                    return False

                d1_dislike_set = self.person_belong_to_map[d1_last_dislike_history]
                d1_dislike_set.add(d2)
                self.person_belong_to_map[d2] = d1_dislike_set
            else:  # d1_belong_set and d2_belong_set
                if d1_belong_set == d2_belong_set:
                    return False

                d1_dislike_set = self.person_belong_to_map[d1_last_dislike_history]
                d2_dislike_set = self.person_belong_to_map[d2_last_dislike_history]

                if d1_dislike_set != d2_belong_set:
                    if len(d1_dislike_set) > len(d2_belong_set):
                        d1_dislike_set.update(d2_belong_set)

                        for person in d2_belong_set:
                            self.person_belong_to_map[person] = d1_dislike_set

                    else:
                        d2_belong_set.update(d1_dislike_set)

                        for person in d1_dislike_set:
                            self.person_belong_to_map[person] = d2_belong_set

                if d2_dislike_set != d1_belong_set:
                    if len(d2_dislike_set) > len(d1_belong_set):
                        d2_dislike_set.update(d1_belong_set)

                        for person in d1_belong_set:
                            self.person_belong_to_map[person] = d2_dislike_set
                    else:
                        d1_belong_set.update(d2_dislike_set)

                        for person in d2_dislike_set:
                            self.person_belong_to_map[person] = d1_belong_set

            self.last_dislike_history[d1] = d2
            self.last_dislike_history[d2] = d1

        return True


def get_test_cases() -> List:  # [(input1, output1), (input2, output2), ...]
    return [
        # ((4, [[1, 2], [1, 3], [2, 4]]), True),
        ((3, [[1, 2], [1, 3], [2, 3]]), False),
        ((5, [[1, 2], [2, 3], [3, 4], [4, 5], [1, 5]]), False)
    ]


if __name__ == '__main__':
    test_cases = get_test_cases()

    for t_input, t_output in test_cases:
        built_in_func = BuildInFunc()
        n, dislikes = t_input

        sol = Solution(built_in_func)
        result = sol.possibleBipartition(n, dislikes)

        print(f'Is possible expect ? `{result == t_output}`')
