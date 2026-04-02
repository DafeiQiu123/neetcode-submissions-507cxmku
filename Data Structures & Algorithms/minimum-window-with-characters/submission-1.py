class Solution:
    def minWindow(self, s: str, t: str) -> str:
        l = 0
        t_counter = {}
        s_counter = {}
        res, resLen = [-1, -1], float("infinity")
        for i in t:
            t_counter[i] = 1 + t_counter.get(i, 0)
        have, need = 0, len(t_counter)
        for r in range(len(s)):
            c = s[r]
            s_counter[c] = 1 + s_counter.get(c,0)
            if c in t_counter and t_counter[c] == s_counter[c]:
                have += 1
            while have == need:
                if (r - l + 1) < resLen:
                    res = [l, r]
                    resLen = r - l + 1
                s_counter[s[l]] -= 1
                if s[l] in t_counter and s_counter[s[l]] < t_counter[s[l]]:
                    have -= 1
                l += 1
        l, r = res
        return s[l: r + 1] if resLen != float("infinity") else ""