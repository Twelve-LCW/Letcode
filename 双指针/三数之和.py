class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        n=len(nums)
        res=[]
        if n<3:
            return res
        for i in range(n):
            if nums[i]>0:
                return res
            if (i>=1 and nums[i]==nums[i-1]):
                continue
            left=i+1
            right=n-1
            while(left<right):
                snum=nums[i]+nums[left]+nums[right]
                if snum==0:
                    res.append([nums[i],nums[left],nums[right]])
                    while(left<right and nums[left]==nums[left+1]):
                        left+=1
                    while(left<right and nums[right]==nums[right-1]):
                        right-=1
                    left+=1
                    right-=1
                elif snum>0:
                    right-=1
                elif snum<0:
                    left+=1
        return res