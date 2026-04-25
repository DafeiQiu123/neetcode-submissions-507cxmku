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
        res = [0] * len(temperatures)
        pairs = [] #index, temp
        pairs.append((0,temperatures[0]))
        for i in range(1,len(temperatures)):
            while pairs and temperatures[i] > pairs[-1][1]:
                p = pairs.pop()
                res[p[0]] = i - p[0]
            pairs.append((i,temperatures[i]))
        while pairs:
            p = pairs.pop()
            res[p[0]] = 0
        return res            