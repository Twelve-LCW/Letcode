class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        if not triangle:
            return 0
        
        m = len(triangle)
        # 创建和三角形一样结构的 dp 数组
        dp = [[0] * (i + 1) for i in range(m)]
        dp[0][0] = triangle[0][0]
        
        for i in range(1, m):
            for j in range(i + 1):  # 第i行只有i+1个元素
                if j == 0:
                    # 最左边，只能来自正上方
                    dp[i][j] = dp[i-1][j] + triangle[i][j]
                elif j == i:
                    # 最右边，只能来自左上方
                    dp[i][j] = dp[i-1][j-1] + triangle[i][j]
                else:
                    # 中间，取两个方向最小值
                    dp[i][j] = min(dp[i-1][j], dp[i-1][j-1]) + triangle[i][j]
        
        # 最后一行最小值就是答案
        return min(dp[-1])