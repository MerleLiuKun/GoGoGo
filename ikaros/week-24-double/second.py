"""

"""


class Solution:
    def findMinFibonacciNumbers(self, k: int) -> int:
        nums = []
        idx = 1
        while True:
            fib = self.fibonacci(idx)
            if fib > k:
                break
            if fib == k:
                return 1
            idx += 1
            nums.append(fib)

        c = 0
        while True:
            pass

    def fibonacci(self, k):
        if k == 1:
            return 0
        if k == 2:
            return 1
        return self.fibonacci(k - 1) + self.fibonacci(k - 2)


if __name__ == '__main__':
    s = Solution()
    s.findMinFibonacciNumbers(5)
