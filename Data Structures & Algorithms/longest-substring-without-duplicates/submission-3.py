class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, r = 0, 0
        res = 0
        cur = set()
        while r < len(s):
            while s[r] in cur:
                cur.remove(s[l])
                l += 1
            cur.add(s[r])
            r += 1
            res = max(res, r - l)
        return res