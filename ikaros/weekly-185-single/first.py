class Solution:
    def reformat(self, s: str) -> str:
        nums = []
        chars = []

        for letter in s:
            if 'a' <= letter <= 'z':
                chars.append(letter)
            else:
                nums.append(letter)

        if abs(len(chars) - len(nums)) > 1:
            return ""

        if len(chars) > len(nums):
            first, second = chars, nums
        else:
            first, second = nums, chars

        idx = 0
        r = ""
        while True:
            if idx >= len(first):
                break
            r += first[idx]

            if idx < len(second):
                r += second[idx]

            idx += 1

        return r


if __name__ == '__main__':
    s = Solution()

    print(s.reformat("ab123"))
