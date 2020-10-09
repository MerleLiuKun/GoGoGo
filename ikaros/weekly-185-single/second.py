from typing import List
from collections import defaultdict


class Solution:
    def displayTable(self, orders: List[List[str]]) -> List[List[str]]:
        foods = set()
        table_foods = {}

        for _, tb, food in orders:
            foods.add(food)
            table_foods.setdefault(tb, defaultdict(int))[food] += 1

        foods = ['Table'] + sorted(foods)
        res = [foods]
        for tb in sorted(table_foods.keys(), key=lambda a: int(a)):
            menu = table_foods[tb]
            items = []
            for food in foods:
                if food == 'Table':
                    items.append(tb)
                else:
                    items.append(str(menu[food]))

            res.append(items)
        return res


if __name__ == '__main__':
    s = Solution()
    print(s.displayTable([["James","12","Fried Chicken"],["Ratesh","12","Fried Chicken"],["Amadeus","12","Fried Chicken"],["Adam","1","Canadian Waffles"],["Brianna","1","Canadian Waffles"]]))
