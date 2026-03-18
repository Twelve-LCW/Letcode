class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        s=nums[0]
        res=nums[0]
        for num in nums[1:]:
            s=max(s+num,num)
            res=max(res,s)
        return res