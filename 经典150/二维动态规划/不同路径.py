class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        
        # 起点是障碍物，直接返回0
        if obstacleGrid[0][0] == 1:
            return 0
        
        dp = [[0] * n for _ in range(m)]
        dp[0][0] = 1
        
        # 初始化第一列（遇到障碍直接break，后面都不可达）
        for i in range(1, m):
            if obstacleGrid[i][0] == 1:
                break
            dp[i][0] = 1
        
        # 初始化第一行（遇到障碍直接break，后面都不可达）
        for j in range(1, n):
            if obstacleGrid[0][j] == 1:
                break
            dp[0][j] = 1
        
        # 正常DP
        for i in range(1, m):
            for j in range(1, n):
                if obstacleGrid[i][j] == 1:
                    dp[i][j] = 0
                else:
                    dp[i][j] = dp[i-1][j] + dp[i][j-1]
        
        return dp[m-1][n-1]