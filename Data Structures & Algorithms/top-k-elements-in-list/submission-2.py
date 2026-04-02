class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic = {}
        freq = [[] for _ in range(len(nums)+1)]
        for num in nums:
            dic[num] = 1 + dic.get(num,0)
        for number, count in dic.items():
            freq[count].append(number)
        j = 0
        result = []
        for i in range(len(freq)-1, 0, -1):
            if j >= k:
                break
            result.extend(freq[i])
            j += len(freq[i])
        return result