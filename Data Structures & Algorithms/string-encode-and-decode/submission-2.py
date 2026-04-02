class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for st in strs:
            res += str(len(st))
            res += '#'
            res += st
        return res
    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i < len(s):
            j = s.find('#',i)
            length = int(s[i:j])
            res.append(s[j+1:j+length+1])
            i = j + length +1
        return res