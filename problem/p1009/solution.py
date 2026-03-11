class Solution:
    process_function_str = "bitwiseComplement"

    def bitwiseComplement(self, n: int) -> int:
        # count 2^n
        rest_n = n
        log2_n = 0
        while rest_n > 1:
            rest_n = rest_n // 2
            log2_n += 1

        bin = ""
        rest_n = n
        for power in range(log2_n, -1, -1):
            decimal = 2 ** power
            if rest_n >= decimal:
                bin += "1"
                rest_n -= decimal
            else:
                if bin: bin += "0"
        if not bin: bin = "0"

        comple_bin = ""
        for i in bin:
            if i == "1":
                comple_bin += "0"
            else:
                comple_bin += "1"

        comple_n = 0
        for idx, b in enumerate(reversed(comple_bin)):
            if b == "1":
                comple_n += 2 ** idx

        return comple_n
