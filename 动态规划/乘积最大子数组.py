class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n=len(nums)
        fmax=[0]*n
        fmin=[0]*n
        fmax[0]=fmin[0]=nums[0]
        for i in range(1,n):
            x=nums[i]
            fmax=max(fmax[i-1]*x,fmin[i-1]*x,x)
            fmin=max(fmax[i-1]*x,fmin[i-1]*x,x)
        return max(fmax)
    #         核心：同时维护最大值和最小值（DP）。
    # 一、为什么要两个值（关键）
    # 因为有 负数：
    # 负 × 负 → 正
    # 当前最小值，乘上负数，可能变成最大值
    # 👉 只维护最大值会出错
    # 二、DP 定义（一句话）
    # fmax：以当前位置结尾的最大乘积
    # fmin：以当前位置结尾的最小乘积
    def maxProduct(self, nums: List[int]) -> int:
        res=-inf
        fmax=fmin=1
        for x in nums:
            fmax,fmin=max(fmax*x,fmin*x,x),min(fmin*x,fmax*x,x)
            res=max(fmax,res)
        return res