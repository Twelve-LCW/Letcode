class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n=len(heights)
        left=[-1]*n
        st=[]
        for i,h in enumerate(heights):
            while st and heights[st[-1]]>=h:
                st.pop()
            if st:
                left[i]=st[-1]
            st.append(i)
        
        right=[n]*n
        st.clear()
        for i in range(n-1,-1,-1):
            h=heights[i]
            while st and heights[st[-1]]>=h:
                st.pop()
            if st:
                right[i]=st[-1]
            st.append(i)
        
        ans=0
        for h,l,r in zip(heights,left,right):
            ans=max(ans,h*(r-l-1))
        return ans


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        left = [-1] * n
        right = [n] * n
        st = []
        for i, h in enumerate(heights):
            while st and heights[st[-1]] >= h:
                right[st.pop()] = i
            if st:
                left[i] = st[-1]
            st.append(i)

        ans = 0
        for h, l, r in zip(heights, left, right):
            ans = max(ans, h * (r - l - 1))
        return ans


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        heights.append(-1)  # 最后大火收汁，用 -1 把栈清空
        st = [-1]  # 在栈中只有一个数的时候，栈顶的「下面那个数」是 -1，对应 left[i] = -1 的情况
        ans = 0
        for right, h in enumerate(heights):
            while len(st) > 1 and heights[st[-1]] >= h:
                i = st.pop()  # 矩形的高（的下标）
                left = st[-1]  # 栈顶下面那个数就是 left
                ans = max(ans, heights[i] * (right - left - 1))
            st.append(right)
        return ans