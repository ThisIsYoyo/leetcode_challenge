class Solution:
    process_function_str = "reverseWords"

    def reverseWords(self, s: str) -> str:
        reversed_maybe_words = reversed(s.split(" "))
        reversed_words = [word for word in reversed_maybe_words if word]
        return " ".join(reversed_words)
