class Solution:
    def canJump(self, nums: List[int]) -> bool:
        goal=0
        n=len(nums)
        for i in range(n):
            if i>goal:
                return False
            goal=max(i+nums[i],goal)
            if goal>=n-1:
                return True
        return False
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        goal = len(nums)-1 
        for i in range(len(nums)-2,-1,-1):
            if i+nums[i]>=goal:
                goal=i 
        return True if goal==0 else False