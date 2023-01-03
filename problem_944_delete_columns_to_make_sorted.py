import math
from typing import List, Tuple


class BuildInFunc:
    pass


class Solution:
    INCREASE_ORDER = 'INCREASE_ORDER'
    DECREASE_ORDER = 'DECREASE_ORDER'

    def __init__(self, build_in_func: BuildInFunc):
        self.build_in_func = build_in_func

    def minDeletionSize(self, strs: List[str]) -> int:
        row_len = len(strs)
        col_len = len(strs[0])

        # see if each row sorted
        rows_last_acsii = [ord('a')] * row_len
        for col_idx in range(col_len):

            for row_idx, row in enumerate(strs):
                word_last_ascii = rows_last_acsii[row_idx]
                word_cur_ascii = ord(row[col_idx])

                if word_last_ascii is None:
                    continue

                if word_cur_ascii >= word_last_ascii:
                    rows_last_acsii[row_idx] = word_cur_ascii
                else:
                    rows_last_acsii[row_idx] = None

        if col_len >= 2:
            rows_need_delete_count = len([acsii for acsii in rows_last_acsii if acsii is None])
        else:
            rows_need_delete_count = row_len

        # see if each col sorted
        cols_last_acsii = [ord('a')] * col_len
        for row_idx, row in enumerate(strs):

            for col_idx in range(col_len):
                word_last_ascii = cols_last_acsii[col_idx]
                word_cur_ascii = ord(row[col_idx])

                if word_last_ascii is None:
                    continue

                if word_cur_ascii >= word_last_ascii:
                    cols_last_acsii[col_idx] = word_cur_ascii
                else:
                    cols_last_acsii[col_idx] = None

        if row_len >= 2:
            cols_need_delete_count = len([acsii for acsii in cols_last_acsii if acsii is None])
        else:
            cols_need_delete_count = col_len

        if rows_need_delete_count == cols_need_delete_count == 1:
            return 0

        return min(rows_need_delete_count, cols_need_delete_count)


def get_test_cases() -> List:  # [(input1, output1), (input2, output2), ...]
    return [
        (["cba", "daf", "ghi"], 1),
        (["a", "b"], 0),
        (["zyx", "wvu", "tsr"], 3)
    ]


if __name__ == '__main__':
    test_cases = get_test_cases()

    for t_input, t_output in test_cases:
        built_in_func = BuildInFunc()

        sol = Solution(built_in_func)
        result = sol.minDeletionSize(t_input)

        print(f'Is delete min expect ? `{result == t_output}`')
