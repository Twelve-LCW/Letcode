class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        n=len(nums)
        left_sum=1
        right_sum=[1]*(n+1)
        for i in range(n-1,-1,-1):
            right_sum[i]=right_sum[i+1]*nums[i]
        ans=[]
        for i in range(n):
            res=left_sum*right_sum[i+1]
            ans.append(res)
            left_sum=left_sum*nums[i]
        return ans
