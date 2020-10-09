from collections import defaultdict


class Solution:
    def minNumberOfFrogs(self, croakOfFrogs: str) -> int:
        data = defaultdict(int)

        res = 0
        for letter in croakOfFrogs:
            if letter == 'c':
                data['c'] += 1
            elif letter == 'r':
                data['c'] -= 1
                data['r'] += 1
            elif letter == 'o':
                data['r'] -= 1
                data['o'] += 1
            elif letter == 'a':
                data['o'] -= 1
                data['a'] += 1
            elif letter == 'k':
                data['a'] -= 1
            else:
                return -1
            if min(data.values()) < 0:
                return -1
            res = max(res, sum(data.values()))
        if sum(data.values()) != 0:
            return -1
        return res


if __name__ == '__main__':
    s = Solution()
    rock = "crcoakroak"
    print(s.minNumberOfFrogs(rock))
