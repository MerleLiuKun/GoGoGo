class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        idx_s, idx_t = 0, 0

        while idx_t < len(t) and idx_s < len(s):
            if s[idx_s] == t[idx_t]:
                idx_s = idx_s + 1

            idx_t += 1

        if idx_s == len(s):
            return True
        return False


if __name__ == '__main__':
    s = Solution()
    s.isSubsequence("axc", "ahbgdc")
