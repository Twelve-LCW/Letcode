class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        n=len(nums)
        left_sum=1
        right_sum=[1]*(n+1)
        sum=1
        for i in range(n-1,0,-1):
            sum=sum*nums[i]
            right_sum[i]=sum
        ans=[]
        for i in range(n):
            res=left_sum*right_sum[i+1]
            ans.append(res)
            left_sum=left_sum*nums[i]
        return ans