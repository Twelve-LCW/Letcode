class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit=0
        min_price=prices[0]
        for price in prices:
            if price<min_price:
                min_price=price
            elif price>min_price:
                max_profit=max(max_profit,price-min_price)
        return max_profit

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ans = 0
        min_price = prices[0]
        for p in prices:
            ans = max(ans, p - min_price)
            min_price = min(min_price, p)
        return ans
