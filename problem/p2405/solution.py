class Solution:
    def partitionString(self, s: str) -> int:
        appeared_string_set = set()

        partit = 0
        for sub in s:
            if sub in appeared_string_set:
                appeared_string_set.clear()
                partit += 1
            appeared_string_set.add(sub)

        return partit + bool(appeared_string_set)

