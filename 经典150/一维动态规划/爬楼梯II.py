class Solution:
    def climbStairs(self, n: int, costs: List[int]) -> int:
        dp=[0]*(n+1)
        dp[0]=0
        if n==0:
            return dp[0]
        dp[1]=costs[0]+1
        if n==1:
            return dp[1]
        dp[2]=costs[1]+min(dp[0]+4,dp[1]+1)
        if n==2:
            return dp[2]
        for i in range(3,n+1):
            dp[i]=costs[i-1]+min(dp[i-1]+1,dp[i-2]+4,dp[i-3]+9)
        return dp[-1]
