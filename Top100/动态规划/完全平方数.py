class Solution:
    def numSquares(self, n: int) -> int:
        dp=[0]*(n+1)
        for i in range(1,n+1):
            minn=10000
            j=1
            while j*j<=i:
                minn=min(minn,dp[i-j*j])
                j+=1
            dp[i]=minn+1
        return dp[n]

n = 10000
f = [0] + [inf] * n
#完全背包
for i in range(1, isqrt(n)+1): #i是第i个完全平方数
    for j in range(i*i, n+1): #j是元素和
        f[j] = min(f[j], f[j-i*i]+1)

class Solution:
    
    def numSquares(self, n: int) -> int:

        return f[n]
        