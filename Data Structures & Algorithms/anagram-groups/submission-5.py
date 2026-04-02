class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = []
        dic = {}
        for i, n in enumerate(strs):
            counter = [0] * 26
            for char in n:
                counter[ord(char) - ord('a')] += 1
            counter_key = tuple(counter) 
            if counter_key in dic:
                dic[counter_key].append(n)
            else:
                dic[counter_key] = [n]
        return list(dic.values())