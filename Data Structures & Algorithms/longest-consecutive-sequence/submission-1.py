class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        def find_length(start, num_set):
            length = 0
            while start in num_set:
                start += 1
                length += 1
            return length
        num_set = set(nums)
        res = []
        for i in range(len(nums)):
            if (nums[i]-1) not in num_set:
                res.append(find_length(nums[i],num_set))
        if len(res) == 0:
            return 0
        return max(res)