class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if not s:
            return True

        rest_s = s
        for char in t:
            if rest_s[0] == char:
                rest_s = rest_s[1:]

            if not rest_s:
                return True

        return not rest_s
