from typing import List


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        anagrams_idx_list = []
        len_p = len(p)

        p_letter_classify_dict = {}  # letter: times
        for l in p:
            p_letter_classify_dict.setdefault(l, 0)
            p_letter_classify_dict[l] += 1

        this_letter_classify_dict = {}  # letter: times
        for start_idx in range(len(s)):
            this_s = s[start_idx: start_idx + len_p]
            if len(this_s) < len_p:
                return anagrams_idx_list

            if not this_letter_classify_dict:
                for l in this_s:
                    this_letter_classify_dict.setdefault(l, 0)
                    this_letter_classify_dict[l] += 1
            else:
                last_start_l = s[start_idx - 1]
                this_end_l = this_s[-1]

                if this_letter_classify_dict[last_start_l] == 1:
                    del this_letter_classify_dict[last_start_l]
                else:
                    this_letter_classify_dict[last_start_l] -= 1

                this_letter_classify_dict.setdefault(this_end_l, 0)
                this_letter_classify_dict[this_end_l] += 1

            if this_letter_classify_dict == p_letter_classify_dict:
                anagrams_idx_list.append(start_idx)

        return anagrams_idx_list

