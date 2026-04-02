class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = set()
        for i in range(len(nums) - 2):
            l = i + 1
            r = len(nums) - 1
            target = -nums[i]
            while l < r:
                if nums[l] + nums[r] > target:
                    r -= 1
                elif nums[l] + nums[r] < target:
                    l += 1
                else:
                    res.add((nums[i], nums[l], nums[r]))
                    r -= 1
                    l += 1
        return [list(one) for one in res]
