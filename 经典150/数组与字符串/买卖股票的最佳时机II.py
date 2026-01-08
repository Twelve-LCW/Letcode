class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res=0
        n=len(prices)
        for i in range(1,n):
            if prices[i]>prices[i-1]:
                res+=prices[i]-prices[i-1]
        return res

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        f = [[0] * 2 for _ in range(n + 1)]
        f[0][1] = -inf
        for i, p in enumerate(prices):
            f[i + 1][0] = max(f[i][0], f[i][1] + p)
            f[i + 1][1] = max(f[i][1], f[i][0] - p)
        return f[n][0]
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        f0, f1 = 0, -inf
        for p in prices:
            f0, f1 = max(f0, f1 + p), max(f1, f0 - p)
        return f0