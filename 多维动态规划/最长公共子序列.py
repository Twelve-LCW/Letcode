class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n,m=len(text1),len(text2)
        dp=[[0]*(m+1) for _ in range(n+1)] #和下面的循环关联，如果外层是text1（n），那么就是n行m列
        for i,x in enumerate(text1):
            for j,y in enumerate(text2):
                if x==y:#如果两个字母相同，则+1
                    dp[i+1][j+1]=dp[i][j]+1 
                else:
                    dp[i+1][j+1]=max(dp[i+1][j],dp[i][j+1])
        return dp[n][m]
    
    #只要两行，当前行和上一行
    def longestCommonSubsequence(self, s: str, t: str) -> int:
        n, m = len(s), len(t)
        f = [[0] * (m + 1) for _ in range(2)]
        for i, x in enumerate(s):
            for j, y in enumerate(t):
                f[(i + 1) % 2][j + 1] = f[i % 2][j] + 1 if x == y else \
                                        max(f[i % 2][j + 1], f[(i + 1) % 2][j])
        return f[n % 2][m]
    
    def longestCommonSubsequence(self, s: str, t: str) -> int:
        f = [0] * (len(t) + 1)
        for x in s:
            pre = 0  # f[0] 对应的是左上角的数据
            for j, y in enumerate(t):
                tmp = f[j + 1] #下一轮j（到j+2）的左上角的数据
                f[j + 1] = pre + 1 if x == y else max(f[j + 1], f[j]) #f[j]已经更新了，是当前行的左边的数据，f[j+1]还没更新，还是上一行的数据
                pre = tmp
        return f[-1]