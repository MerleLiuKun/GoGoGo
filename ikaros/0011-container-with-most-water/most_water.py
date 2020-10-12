"""

"""
from typing import List


class Solution:
    # 暴力解法
    def maxArea(self, height: List[int]) -> int:
        i = 0
        r = 0

        while i < len(height):
            j = 0
            while j < len(height[i:]):
                c = min(height[i], height[i + j]) * j
                if c > r:
                    r = c
                j += 1
            i += 1

        return r

    # 双指针
    def maxArea2(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1

        max_area = 0

        while left < right:
            w = right - left
            # 移动小的一端
            if height[left] < height[right]:
                h = height[left]
                left += 1
            else:
                h = height[right]
                right -= 1

            area = h * w

            if area > max_area:
                max_area = area

        return max_area


if __name__ == '__main__':
    s = Solution()
    arr = [1, 8, 6, 2, 5, 4, 8, 3, 7]
    print(s.maxArea2(arr))
