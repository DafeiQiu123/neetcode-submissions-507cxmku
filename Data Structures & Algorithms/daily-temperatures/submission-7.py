class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # current = 0
        # result = []
        # for i in range(len(temperatures)):
        #     count = 0
        #     for j in range(i+1,len(temperatures)):
        #         if temperatures[j] > temperatures[i]:
        #             count = j - i
        #             break
        #     result.append(count)
        # return result
        s = []
        res = [0] * len(temperatures)
        s.append((temperatures[0],0))
        for i in range(1, len(temperatures)):
            while (s and temperatures[i] > s[-1][0]):
                p = s.pop()
                res[p[1]] = i - p[1]
            s.append((temperatures[i],i))
        while s:
            p = s.pop()
            res[p[1]] = 0
        return res

               
            
            