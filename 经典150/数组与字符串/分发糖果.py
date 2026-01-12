class Solution:
    def candy(self, ratings: List[int]) -> int:
        n=len(ratings)
        left=[1]*n
        right=left.copy()
        for i in range(1,n):
            if ratings[i]>ratings[i-1]:
                left[i]=left[i-1]+1
        res=max(left[n-1],right[n-1])
        for i in range(n-2,-1,-1):
            if ratings[i]>ratings[i+1]:
                right[i]=right[i+1]+1
            res+=max(left[i],right[i])
        return res

class Solution:
    def candy(self, ratings: List[int]) -> int:
        ans = n = len(ratings)  # 先给每人分一个
        i = 0
        while i < n:
            start = i - 1 if i > 0 and ratings[i - 1] < ratings[i] else i

            # 找严格递增段
            while i + 1 < n and ratings[i] < ratings[i + 1]:
                i += 1
            top = i  # 峰顶

            # 找严格递减段
            while i + 1 < n and ratings[i] > ratings[i + 1]:
                i += 1

            inc = top - start  # start 到 top 严格递增
            dec = i - top      # top 到 i 严格递减
            ans += (inc * (inc - 1) + dec * (dec - 1)) // 2 + max(inc, dec)
            i += 1
        return ans