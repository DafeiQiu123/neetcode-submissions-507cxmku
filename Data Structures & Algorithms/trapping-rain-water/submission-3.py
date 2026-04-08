class Solution:
    def trap(self, height: List[int]) -> int:
        premax = [0] * len(height)
        postmax = [0] * len(height)
        pre, post = 0, 0
        for i in range(len(height)):
            j = len(height) - 1 - i
            premax[i] = pre
            postmax[j] = post
            if height[i] > pre:
                pre = height[i]
            if height[j] > post:
                post = height[j]
        result = 0
        for k in range(len(height)):
            water = min(premax[k],postmax[k]) - height[k]
            if water > 0:
                result += water
        return result