"""
    5374 长度为 n 的开心字符串中字典序第 k 小的字符串
"""
import itertools


class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        idx = 0
        for st in itertools.product('abc', repeat=n):
            st = "".join(st)
            if self.check(st):
                idx += 1
            if idx == k:
                return st
        return ""

    def check(self, st: str):
        idx = 0
        while idx + 1 < len(st):
            if st[idx] == st[idx + 1]:
                return False
            idx += 1
        return True


if __name__ == '__main__':
    s = Solution()
    # print(s.check("b"))
    print(s.getHappyString(1, 3))
