class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m,n=len(word1),len(word2)
        dp=[[0]*(n+1) for _ in range(m+1)]
        dp[0]=list(range(n+1))
        for i,x in enumerate(word1):
            dp[i+1][0]=i+1
            for j,y in enumerate(word2):
                if x==y:
                    dp[i+1][j+1]=dp[i][j]
                else:
                    dp[i+1][j+1]=min(dp[i+1][j],dp[i][j+1],dp[i][j])+1
        return dp[m][n]