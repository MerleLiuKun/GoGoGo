from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m = len(nums1)
        n = len(nums2)

        idx, i, j = 0, 0, 0
        flag = False
        if (m + n) % 2 == 0:
            flag = True

        medium = (m + n) // 2
        # while True:
        #     pass

        return 1.9
