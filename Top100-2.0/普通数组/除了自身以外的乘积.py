class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n=len(nums)
        right_sum=[1]*n
        for i in range(n-2,-1,-1):
            right_sum[i]=right_sum[i+1]*nums[i+1]
        
        left_sum=1
        res=[]
        for i in range(n):
            res.append(left_sum*right_sum[i])
            left_sum=left_sum*nums[i]
        return res