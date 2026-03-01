class Solution:
    def totalNQueens(self, n: int) -> int:
        queens=[0]*n
        cols=[False]*n
        dig1=[False]*(2*n-1)
        dig2=[False]*(2*n-1)
        res=0
        def dfs(r):
            if r==n:
                nonlocal res
                res+=1
                return
            for c,ok in enumerate(cols):
                if not ok and not dig1[r+c] and not dig2[r-c]:
                    queens[r]=c
                    cols[c]=dig1[r+c]=dig2[r-c]=True
                    dfs(r+1)
                    cols[c]=dig1[r+c]=dig2[r-c]=False
        dfs(0)
        return res