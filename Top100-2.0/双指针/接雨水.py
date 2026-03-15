class Solution:
    def trap(self, height: List[int]) -> int:
        n=len(height)
        left,right=0,n-1
        leftmax=rightmax=0
        res=0
        while left<right:
            leftmax=max(leftmax,height[left])
            rightmax=max(rightmax,height[right])
            if leftmax<=rightmax:
                res+=leftmax-height[left]
                left+=1
            else:
                res+=rightmax-height[right]
                right-=1
        return res