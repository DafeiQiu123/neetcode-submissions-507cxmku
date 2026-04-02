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
            res = max(res, r - l + 1)
            r += 1
        return res