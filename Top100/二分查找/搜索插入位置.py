class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        n=len(nums)
        l=0,r=n-1
        mid=(r+l)//2
        while l<=r:
            mid=(r+l)//2
            if target>nums[mid]:
                l=mid+1
            else:
                r=mid-1
        return l