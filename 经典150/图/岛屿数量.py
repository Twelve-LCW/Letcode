class Solution:
    
    def numIslands(self, grid: List[List[str]]) -> int:
        m=len(grid)
        n=len(grid[0])
        def dfs(i,j):
            if i>=m or i<0 or j<0 or j>=n or grid[i][j]!='1':
                return
            grid[i][j]='2'
            dfs(i+1,j)
            dfs(i-1,j)
            dfs(i,j+1)
            dfs(i,j-1)
        
        res=0
        for i in range(m):
            for j in range(n):
                if grid[i][j]=='1':
                    res+=1
                    dfs(i,j)
        return res