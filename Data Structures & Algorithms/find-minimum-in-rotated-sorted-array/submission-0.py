def recur(nums, left, right):
    mid = (left + right)//2
    if left >= right:
        return nums[left]
    
    l = recur(nums,left,mid)
    r = recur(nums,mid+1,right)
    return min(l,r)
class Solution:
        
    def findMin(self, nums: List[int]) -> int:
        return recur(nums,0,len(nums)-1)