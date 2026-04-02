class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pro = []
        post = []
        pro_product = 1
        post_product = 1
        j = len(nums) - 1
        for i in range(len(nums)):
            pro_product *= nums[i]
            post_product *= nums[j]
            pro.append(pro_product)
            post.append(post_product)
            j = j - 1
        res = []
        for i in range(len(nums)):
            if i == 0:
                res.append(post[len(nums)-2-i])
            elif i == len(nums) - 1:
                res.append(pro[i-1])
            else:
                res.append(pro[i-1]*post[len(nums)-2-i])
        return res
