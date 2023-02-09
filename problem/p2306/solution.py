from typing import List


class Solution:
    def distinctNames(self, ideas: List[str]) -> int:
        first_letter_classify = {}  # first letter: rest letter set
        for idea in ideas:
            first_letter_classify.setdefault(idea[0], set())
            first_letter_classify[idea[0]].add(idea[1:])

        checked_first_letter_set = set()
        count = 0
        for first_letter, rest_letter_set in first_letter_classify.items():
            for other_first_letter, other_rest_letter_set in first_letter_classify.items():
                if other_first_letter == first_letter or other_first_letter in checked_first_letter_set:
                    continue

                same_rest_letter_set = rest_letter_set.intersection(other_rest_letter_set)
                count += (
                        len(rest_letter_set - same_rest_letter_set) *
                        len(other_rest_letter_set - same_rest_letter_set) * 2
                )

            checked_first_letter_set.add(first_letter)

        return count

