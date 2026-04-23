class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # bruteforce
        if len(heights) == 1:
            return heights[0]
        largest = 0
        for i in range(len(heights)):
            minh = heights[i]
            for j in range(i,len(heights)):
                minh = min(heights[j], minh)
                largest = max(largest, (j-i+1)*minh)
        return largest