"""

"""
from typing import List


class Solution:
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


if __name__ == '__main__':
    s = Solution()
    print(s.removeDuplicates([1]))
