class Solution:
    ROMAN = {
        1: "I",
        5: "V",
        10: "X",
        50: "L",
        100: "C",
        500: "D",
        1000: "M",
    }
    process_function_str = "intToRoman"

    def intToRoman(self, num: int) -> str:
        rest_num = num
        roman = ""

        for decimal in [1000, 100, 10, 1]:
            digit_num = rest_num // decimal

            if digit_num == 0:
                continue
            elif digit_num <= 3:
                roman += self.ROMAN[decimal] * digit_num
            elif digit_num == 4:
                roman += self.ROMAN[decimal] + self.ROMAN[5 * decimal]
            elif digit_num <= 8:
                roman += self.ROMAN[5 * decimal] + self.ROMAN[decimal] * (digit_num - 5)
            elif digit_num == 9:
                roman += self.ROMAN[decimal] + self.ROMAN[10 * decimal]

            rest_num = rest_num % decimal

        return roman






