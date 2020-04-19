"""
    5372 逐步求和得到正数的最小值
"""
from typing import List


class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        min_r = 0
        r = 0
        for n in nums:
            r += n
            if r < min_r:
                min_r = r

        if min_r > 0:
            return 1
        else:
            return -min_r + 1


if __name__ == '__main__':
    s = Solution()

    num = [1, 2]
    print(s.minStartValue(num))
