from typing import List

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        sums = [n * n for n in nums]

        return self.quick_sort(sums, 0, len((nums)) - 1)

    

    def quick_sort(self, arr, left, right):
        if left >= right:
            return
        
        pidx = self.partition(arr, left, right)
        self.quick_sort(arr, left, pidx - 1)
        self.quick_sort(arr, pidx + 1, right)
        return arr
    

    def partition(self, arr, left, right):
        pivot = left
        idx = pivot + 1
        i = idx
        while i <= right:
            if arr[i] < arr[pivot]:
                arr[i], arr[pivot] = arr[pivot], arr[i]
                idx += 1
            i += 1
        arr[pivot], arr[idx - 1] = arr[idx - 1], arr[pivot]

        return idx - 1


if __name__ == '__main__':
    s = Solution()
    print(s.sortedSquares([-4,-1,0,3,10]))
