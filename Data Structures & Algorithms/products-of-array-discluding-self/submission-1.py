class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre = []
        post = []
        prepro = 1
        postpro = 1
        for i in range(len(nums)):
            pre.append(prepro)
            post.append(postpro)
            prepro *= nums[i]
            postpro *= nums[len(nums) - i - 1]
        res = []
        for i in range(len(nums)):
            res.append(post[len(nums) - i - 1]*pre[i])

        return res