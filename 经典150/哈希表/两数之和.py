class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mp={}
        for i,num in enumerate(nums):
            if target-num in mp:
                return [mp.get(target-num),i]
            mp[num]=i
        return []