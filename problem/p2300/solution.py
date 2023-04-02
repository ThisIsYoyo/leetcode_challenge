import bisect
import math
from typing import List


class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        sorted_potions = sorted(potions)
        max_potion = sorted_potions[-1]
        m = len(potions)

        pairs = []
        for spell in spells:
            min_potion = math.ceil(success / spell)
            if min_potion > max_potion:
                pairs.append(0)
                continue

            min_potion_insert_i = bisect.bisect_left(sorted_potions, min_potion)
            pairs.append(m - min_potion_insert_i)

        return pairs

