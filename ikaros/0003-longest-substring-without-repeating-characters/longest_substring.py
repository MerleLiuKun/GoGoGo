class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        max_length = 0
        cur_length = 0

        r = []

        for val in s:
            if val not in r:
                cur_length += 1
                max_length = max(max_length, cur_length)
                r.append(val)
            else:
                pidx = r.index(val)
                r = r[pidx + 1 :]
                r.append(val)
                cur_length = len(r)
        return max_length

    def method2(self, s: str) -> int:
        if not s:
            return 0

        start, max_length = 0, 0

        v_map = {}

        for idx, val in enumerate(s):
            if val in v_map:
                start = max(v_map[val] + 1, start)
            v_map[val] = idx
            max_length = max(max_length, idx - start + 1)

        return max_length

    def method3(self, s: str) -> int:
        res, start, cache = 0, 0, {}
        for idx, c in enumerate(s):
            if c in cache and cache[c] >= start:
                start = cache[c] + 1
            else:
                cur = idx - start + 1
                res = max(res, cur)

            cache[c] = idx
        return res



if __name__ == "__main__":
    sr = "pwwkew"
    so = Solution()
    print(so.method2(sr))
