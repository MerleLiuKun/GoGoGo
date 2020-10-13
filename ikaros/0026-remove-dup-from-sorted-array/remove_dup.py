"""

"""
from typing import List


class Solution:
    # 双指针 数据交换
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0

        p_idx = 0
        c_idx = 1

        while c_idx < len(nums):
            if nums[p_idx] != nums[c_idx]:
                nums[p_idx + 1] = nums[c_idx]
                p_idx += 1

            c_idx += 1
        return p_idx + 1

    def removeDuplicates2(self, nums: List[int]) -> int:
        if not nums:
            return 0
        count = 0
        length = len(nums)

        for i in range(1, length):
            # 如果当前值与前一步相同，则 count 前进一步保持与 i 的距离
            if nums[i] == nums[i - 1]:
                count += 1
            else:
                nums[i - count] = nums[i]

        return length - count


if __name__ == '__main__':
    s = Solution()
    print(s.removeDuplicates2([1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2]))
