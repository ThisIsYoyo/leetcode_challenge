class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s

        row_list = ['' for _ in range(numRows)]

        cycle = 2 * numRows - 2
        for l_idx, l in enumerate(s):
            rem = l_idx % cycle

            if rem < numRows:
                row_list[rem] +=l
            else:
                row_idx = cycle - rem
                row_list[row_idx] += l

        result = ''
        for row in row_list:
            result += row

        return result

