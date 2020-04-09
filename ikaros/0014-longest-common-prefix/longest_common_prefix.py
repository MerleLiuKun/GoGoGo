from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        base = strs[0]
        s = ""
        for idx, val in enumerate(base):
            for sub_str in strs[0:]:
                if idx >= len(sub_str):
                    return s
                elif sub_str[idx] != val:
                    return s

            s += val
        return s


if __name__ == "__main__":
    so = Solution()
    data = ["dog","racecar","car"]
    print(so.longestCommonPrefix(data))
