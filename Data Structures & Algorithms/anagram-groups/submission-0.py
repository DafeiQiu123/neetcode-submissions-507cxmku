class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        c_map = {} # counter array -> string
        for st in strs:
            l = [0] * 26
            for char in st:
                l[ord(char) - ord('a')] += 1
            key = tuple(l)
            if key in c_map.keys():
                c_map[key].append(st)
            else:
                c_map[key] = [st]
        return list(c_map.values())
                
            
