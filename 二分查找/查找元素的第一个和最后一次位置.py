class Solution:
    def lower_bound(self,nums,target):
        l,r=0,len(nums)-1
        while l<=r:
            mid=(l+r)//2
            if nums[mid]>=target:
                r=mid-1
            elif nums[mid]<target:
                l=mid+1
        return l
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        s=self.lower_bound(nums,target)
        if s==len(nums) or nums[s]!=target:
            return [-1,-1]
        end=self.lower_bound(nums,target+1)-1
        return [s,end]
        
        
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        n=len(nums)
        l,r=0,n-1
        res=[-1,-1]
        if not nums:
            return res
        while l<=r:
            mid=(l+r)//2
            if nums[mid]==target:
                res[1]=mid
                l=mid+1
            elif nums[mid]>target:
                r=mid-1
            else:
                l=mid+1
        l,r=0,n-1
        while l<=r:
            mid=(l+r)//2
            if nums[mid]==target:
                res[0]=mid
                r=mid-1
            elif nums[mid]>target:
                r=mid-1
            else:
                l=mid+1
        return res