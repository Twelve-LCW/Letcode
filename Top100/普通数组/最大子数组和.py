#前缀和
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n=len(nums)
        min_pre=0
        max_s=nums[0]
        pre=0
        if n==1:
            return nums[0]
        for i in range(n):
                pre+=nums[i]
                max_s=max(max_s,pre-min_pre)
                min_pre=min(min_pre,pre)
        return max_s
#贪心算法
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        sum=nums[0]
        res=nums[0]
        for i in range(1,len(nums)):
              sum=max(sum+nums[i],nums[i])
              res=max(sum,res)
        return res