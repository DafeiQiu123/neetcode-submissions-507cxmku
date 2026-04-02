from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        c1 = dict(Counter(s))
        c2 = dict(Counter(t))
        if len(c1) != len(c2):
            return False
        for key,value in c1.items():
            if key not in c2.keys():
                return False
            if value != c2[key]:
                return False
        return True