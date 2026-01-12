class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        pre_max = [0] * n  # pre_max[i] 表示从 height[0] 到 height[i] 的最大值
        pre_max[0] = height[0]
        for i in range(1, n):
            pre_max[i] = max(pre_max[i - 1], height[i])

        suf_max = [0] * n  # suf_max[i] 表示从 height[i] 到 height[n-1] 的最大值
        suf_max[-1] = height[-1]
        for i in range(n - 2, -1, -1):
            suf_max[i] = max(suf_max[i + 1], height[i])

        ans = 0
        for h, pre, suf in zip(height, pre_max, suf_max):
            ans += min(pre, suf) - h  # 累加每个水桶能接多少水
        return ans
class Solution:
    def trap(self, height: list[int]) -> int:
        n=len(height)
        left,right=0,n-1
        leftmax,rightmax=0,0
        res=0
        while left<right:
            leftmax=max(height[left],leftmax) #从左往右的最大值
            rightmax=max(height[right],rightmax) #从右往左的最大值
            if height[left]<height[right]: #如果左边的值现在更小，就填左边的
                res+=leftmax-height[left] #当前格子 可以接的水最多为lfetmax-height[left]，因为rightmax肯定比leftmax大
                left+=1
            else:
                res+=rightmax-height[right]
                right-=1
        return res

class Solution:
    def trap(self, height: List[int]) -> int:
        ans = 0
        st = []
        for i, h in enumerate(height):
            while st and height[st[-1]] <= h:
                bottom_h = height[st.pop()]
                if not st:  # 栈是空的
                    break
                left = st[-1]
                dh = min(height[left], h) - bottom_h  # 面积的高
                ans += dh * (i - left - 1)
            st.append(i)
        return ans