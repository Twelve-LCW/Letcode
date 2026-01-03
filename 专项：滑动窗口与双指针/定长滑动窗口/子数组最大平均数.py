class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        s=left=0
        res=-10000
        for i,num in enumerate(nums):
            s+=num

            left=i-k+1

            if left<0:
                continue

            res=max(res,s/k)
            s-=nums[left]
        return res
    
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        s=sum(nums[:k])
        res=s
        for i in range(k,len(nums)):
            s+=nums[i]-nums[i-k]
            res=max(res,s)
        return res/k