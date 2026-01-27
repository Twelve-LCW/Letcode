class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        mp={}
        if len(nums) == len(set(nums)):
            return False
        for i,num in enumerate(nums):
            if num in mp:
                if i-mp[num]<=k:
                    return True
            mp[num]=i
        return False