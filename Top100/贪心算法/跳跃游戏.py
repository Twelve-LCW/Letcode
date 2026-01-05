class Solution:
    def canJump(self, nums: List[int]) -> bool:
        boder=nums[0]
        for i in range(len(nums)):
            if i>boder:
                return False
            boder=max(boder,i+nums[i])
        return True
#反着来
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        goal = len(nums)-1 
        for i in range(len(nums)-2,-1,-1):
            if i+nums[i]>=goal:
                goal=i 
        return True if goal==0 else False
        