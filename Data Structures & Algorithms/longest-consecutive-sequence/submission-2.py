class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        all_nums = set(nums)
        head = []
        for i in nums:
            if i - 1 not in all_nums:
                head.append(i)
        res = 0
        for j in head:
            count = 1
            while j + 1 in all_nums:
                count += 1
                j += 1
            if count > res:
                res = count
        return res