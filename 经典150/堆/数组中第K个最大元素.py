class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        min_v,max_v=min(nums),max(nums)
        count=[0]*(max_v-min_v+1)
        for num in nums:
            count[num-min_v]+=1
        
        for i in range(len(count)-1,-1,-1):
            k-=count[i]
            if k<=0:
                return min_v+i
        