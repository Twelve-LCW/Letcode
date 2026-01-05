class Solution:
    def rob(self, nums: List[int]) -> int:
        f0,f1=0,0
        for x in nums:
            f0,f1=f1,max(f0+x,f1)
        return f1