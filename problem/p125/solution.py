class Solution:
    process_function_str = "isPalindrome"

    def isPalindrome(self, s: str) -> bool:
        pure_lower = ""
        for char in s:
            if "a" <= char <= "z" or "A" <= char <= "Z" or "0" <= char <= "9":
                pure_lower = pure_lower + char.lower()

        if len(pure_lower) <= 1:
            return True

        half_len = len(pure_lower) // 2 + len(pure_lower) % 2
        return pure_lower[:half_len]  == pure_lower[::-1][:half_len]
