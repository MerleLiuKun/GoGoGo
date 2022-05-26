"""
    注意几个关键点
    1. 有序数组
    2. 有则输出下标，无则输出要插入的下标位置

    插入位置成立条件为
    nums[pos - 1] < target <= nums[pos]
    
    寻找有序数组中第一个大于等于target的目标

    使用 ans = len(nums) 可以排除边界条件。即 该目标值 大于所有的数。
"""
from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        
        ans = right + 1
        while left <= right:
            middle = left + (right - left) // 2
            if target <= nums[middle]:
                ans = middle
                right = middle - 1
            else:
                left = middle + 1
        
        return ans

if __name__ == '__main__':
    s = Solution()
    print(s.searchInsert([1,3,5,6], 2))
    print(s.searchInsert([1,3,5,6], 7))
    print(s.searchInsert([1,3,5,6], 5))
