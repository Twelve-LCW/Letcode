from collections import Counter


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        cnt=Counter(nums)
        for num,value in cnt.items():
            if value==1:
                return num
    
    def singleNumber(self, nums: List[int]) -> int:
        res = 0
        for x in nums:
            res ^= x
        return res
        