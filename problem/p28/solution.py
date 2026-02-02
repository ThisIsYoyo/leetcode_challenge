class Solution:
    process_function_str = "strStr"

    def strStr(self, haystack: str, needle: str) -> int:
        haystack_len = len(haystack)
        needle_len = len(needle)
        for idx, char in enumerate(haystack):
            if haystack_len - idx < needle_len:
                return -1

            if char != needle[0]:
                continue

            if haystack[idx: idx + needle_len] == needle:
                return idx
        return -1
