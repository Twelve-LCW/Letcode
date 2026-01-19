from math import inf


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        s=0
        res=inf
        l=0
        n=len(nums)
        for r in range(n):
            s+=nums[r]
            while s>=target:
                res=min(res,r-l+1)
                s-=nums[l]
                l+=1
        return res if res!=inf else 0
    