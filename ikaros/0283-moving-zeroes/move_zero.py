"""

"""
from typing import List


class Solution:
    # 临时指针交换
    def moveZeroes(self, nums: List[int]) -> List[int]:
        i = j = 0
        while i < len(nums):
            if nums[i] != 0:
                nums[j] = nums[i]
                if i != j:
                    nums[i] = 0
                j += 1
            i += 1

        return nums


if __name__ == '__main__':
    s = Solution()
    arr = [0, 1, 0, 3, 12]
    print(s.moveZeroes(arr))
