from typing import List


class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        reversed_fruits = fruits[::-1]

        largest_amount_basket = 0
        now_amount_basket = 0
        last_same_fruit = []  # e.g. 1, 1, 1 for 3 kind 1 fruits
        fruit_basket_type_set = set()  # no more than 2 kind
        for fruit in reversed_fruits:
            if fruit not in fruit_basket_type_set and len(fruit_basket_type_set) < 2:
                fruit_basket_type_set.add(fruit)
                now_amount_basket += 1
            elif fruit not in fruit_basket_type_set and len(fruit_basket_type_set) == 2:
                largest_amount_basket = (
                    now_amount_basket
                    if now_amount_basket > largest_amount_basket
                    else largest_amount_basket
                )

                fruit_basket_type_set = {last_same_fruit[0], fruit}
                now_amount_basket = 1 + len(last_same_fruit)
            elif fruit in fruit_basket_type_set:
                now_amount_basket += 1

            if fruit not in last_same_fruit:
                last_same_fruit.clear()
            last_same_fruit.append(fruit)

        # last time amount not compared
        if now_amount_basket > largest_amount_basket:
            largest_amount_basket = now_amount_basket

        return largest_amount_basket


