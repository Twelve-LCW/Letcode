#暴力法
from collections import defaultdict


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        n=len(nums)
        res=0
        for i in range(n):
            target=0
            for j in range(i,0,-1):
                target+=nums[j]
                if target==k:
                    res+=1
        return res

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res,s=0,0
        cnt=defaultdict(int)
        for num in nums:
            cnt[s]+=1
            s+=num
            res+=cnt[s-k]
        return res
    
