class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        n,m=len(word1),len(word2)
        f=[[0]*(m+1) for _ in range(n+1)]
        f[0]=list(range(m+1))
        for i,x in enumerate(word1):
            f[i+1][0]=i+1
            for j,y in enumerate(word2):
                if x==y:
                    f[i+1][j+1]=f[i][j]
                else:
                    f[i+1][j+1]=min(f[i+1][j],f[i][j+1],f[i][j])+1
        return f[n][m]
    
    def minDistance(self, word1: str, word2: str) -> int:
        f=list(range(len(word2)+1))
        for x in word1:
            pre=f[0]
            f[0]+=1
            for j,y in enumerate(word2):
                tmp=f[j+1] 
                #pre代表左上角的值dp[i][j]
                #f[j]代表左边的值dp[i+1][j]
                #f[j+1]代表上边的值dp[i][j+1]
                f[j+1]=pre if x==y else min(pre,f[j],f[j+1])+1 
                pre=tmp
        return f[-1]    
        

    