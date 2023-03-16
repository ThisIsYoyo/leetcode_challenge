import math
from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        min_coin = [math.inf] * (amount + 1)  # amount i need at least min_coin[i]
        min_coin[0] = 0

        sort_unique_coins = sorted(list(set(coins)))

        for i_amount in range(1, amount + 1):
            for coin in sort_unique_coins:
                if i_amount >= coin:
                    min_coin[i_amount] = min(min_coin[i_amount - coin] + 1, min_coin[i_amount])

        return min_coin[amount] if min_coin[amount] != math.inf else -1

