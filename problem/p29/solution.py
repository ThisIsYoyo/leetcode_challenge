class Solution:
    INT_MIN = - 2 ** 31
    INT_MAX = 2 ** 31 - 1

    def divide(self, dividend: int, divisor: int) -> int:
        # decide sign
        positive_sign = True
        if (dividend >= 0 and divisor > 0) or (dividend <= 0 and divisor < 0):
            pass
        else:
            positive_sign = False

        # calcute quotient without sign
        abs_dividend = abs(dividend)
        abs_divisor = abs(divisor)
        divisor_multi_map = {
            1: abs_divisor,
        }

        abs_q = 0
        rest_abs_dividend = abs_dividend
        while rest_abs_dividend >= abs_divisor:
            cu_q = 0
            for multi_div in sorted(list(divisor_multi_map.keys())):
                if rest_abs_dividend >= divisor_multi_map[multi_div]:
                    cu_q = multi_div
                else:
                    break

            rest_abs_dividend -= divisor_multi_map[cu_q]
            abs_q += cu_q
            divisor_multi_map.setdefault(abs_q, abs_dividend - rest_abs_dividend)

        # check inside int range and add sign
        if positive_sign:
            q = abs_q if abs_q <= self.INT_MAX else self.INT_MAX
        else:
            q = 0 - abs_q if (0 - abs_q) >= self.INT_MIN else self.INT_MIN

        return q

