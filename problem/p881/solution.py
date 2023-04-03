import bisect
from typing import List


class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        sorted_people = sorted(people)

        boat_count = 0
        not_on_boat_people = sorted_people
        while not_on_boat_people:
            s_person = not_on_boat_people.pop(0)
            pair_person_next_i = bisect.bisect_right(not_on_boat_people, limit - s_person)
            if pair_person_next_i:
                not_on_boat_people.pop(pair_person_next_i - 1)
            boat_count += 1

        return boat_count



