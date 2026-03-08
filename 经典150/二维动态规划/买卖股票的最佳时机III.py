from math import inf


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        b1,s1,b2,s2=-inf,0,-inf,0
        for p in prices:
            b1=max(b1,0-p)
            s1=max(s1,b1+p)
            b2=max(b2,s1-p)
            s2=max(s2,b2+p)
        return s2