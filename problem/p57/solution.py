from typing import List


class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        lower_intersect = None  # (idx, interval)
        higher_intersect = None  # (idx, interval)
        for idx, interval in enumerate(intervals):
            if not self.check_intersect(interval, newInterval):
                if higher_intersect:
                    break
                continue

            if lower_intersect is None:
                lower_intersect = (idx, interval)
                continue

            higher_intersect = (idx, interval)

        if not lower_intersect and not higher_intersect:
            return sorted(intervals + [newInterval])

        new_intervals_part1 = intervals[:lower_intersect[0]]
        new_intervals_part2 = []
        new_interval_start = min(lower_intersect[1][0], newInterval[0])
        if higher_intersect:
            new_interval_end = max(higher_intersect[1][1], newInterval[1])
            higher_idx = higher_intersect[0]
            if higher_idx + 1 < len(intervals):
                new_intervals_part2 = intervals[higher_idx + 1:]
        else:
            new_interval_end = max(lower_intersect[1][1], newInterval[1])
            lower_idx = lower_intersect[0]
            if lower_idx + 1 < len(intervals):
                new_intervals_part2 = intervals[lower_idx + 1:]

        return new_intervals_part1 + [[new_interval_start, new_interval_end]] + new_intervals_part2

    def check_intersect(self, interval1: List[int], interval2: List[int]) -> bool:
        start1, end1 = interval1
        start2, end2 = interval2
        if end1 < start2 or end2 < start1:
            return False

        return True

