class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp=[-1]*(amount+1)
        dp[0]=0  # 基础情况：凑0元需要0个硬币
        for i in range(1,amount+1):
            minn=10000
            for coin in coins:
                if i>=coin and dp[i-coin]!=-1: #保证可达的情况下才更新
                    minn=min(minn,dp[i-coin])
            if minn!=10000:
                dp[i]=minn+1
            # 否则 dp[i] 保持 -1（不可达）
        return dp[amount]