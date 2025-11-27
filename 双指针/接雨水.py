class Solution:
    def trap(self, height: list[int]) -> int:
        left,right=0,len(height)-1
        res=0
        leftmax,rightmax=0,0
        while left<right:
            leftmax=max(height[left],leftmax)
            rightmax=max(height[right],rightmax)
            if height[left]<height[right]:
                res+=leftmax-height[left]
                left+=1
            else:
                res+=rightmax-height[right]
                right-=1
        return res

            
        
