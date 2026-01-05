class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res=[]
        borad=[['.' for _ in range (n)]  for _ in range(n) ]
        col=[-1]*n
        dg1=[0]*(2*n)
        dg2=[0]*(2*n)

        def backtrack(x):
            if x==n:
                mid_lst=[]
                for row in borad:
                    mid_lst.append(''.join(row))
                res.append(mid_lst)
                return
            for y in range(n):
                if col[y]==-1 and dg1[y-x+n]==0 and dg2[x+y]==0:
                    borad[x][y]='Q'
                    col[y]=1
                    dg1[y-x+n]=1
                    dg2[x+y]=1

                    backtrack(x+1)

                    borad[x][y]='.'
                    col[y]=-1
                    dg1[y-x+n]=0
                    dg2[x+y]=0
        backtrack(0)
        return res
    
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        ans = []
        queens = [0] * n  # 皇后放在 (r,queens[r])
        col = [False] * n
        diag1 = [False] * (n * 2 - 1)
        diag2 = [False] * (n * 2 - 1)
        def dfs(r: int) -> None:
            if r == n:
                ans.append(['.' * c + 'Q' + '.' * (n - 1 - c) for c in queens])
                return
            # 在 (r,c) 放皇后
            for c, ok in enumerate(col):
                if not ok and not diag1[r + c] and not diag2[r - c]:  # 判断能否放皇后
                    queens[r] = c  # 直接覆盖，无需恢复现场
                    col[c] = diag1[r + c] = diag2[r - c] = True  # 皇后占用了 c 列和两条斜线
                    dfs(r + 1)
                    col[c] = diag1[r + c] = diag2[r - c] = False  # 恢复现场
        dfs(0)
        return ans