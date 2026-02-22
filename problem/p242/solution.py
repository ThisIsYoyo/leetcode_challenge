from typing import List


class Solution:
    process_function_str = "isAnagram"

    def isAnagram(self, s: str, t: str) -> bool:
        letter_to_appear = {}
        for letter_s in s:
            letter_to_appear.setdefault(letter_s, 0)
            letter_to_appear[letter_s] += 1

        for letter_t in t:
            appear = letter_to_appear.get(letter_t, 0)
            if appear == 0:
                return False

            if appear == 1:
                del letter_to_appear[letter_t]
            else:
                letter_to_appear[letter_t] -= 1

        if letter_to_appear == {}:
            return True
        else:
            return False
