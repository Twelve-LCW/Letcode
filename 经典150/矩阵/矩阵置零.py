class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m,n=len(matrix),len(matrix[0])
        flag_x=[False]*m
        flag_y=[False]*n
        for i in range(m):
            for j in range(n):
                if matrix[i][j]==0:
                    flag_x[i]=True
                    flag_y[j]=True
        
        for i in range(m):
            for j in range(n):
                if flag_x[i] or flag_y[j]:
                    matrix[i][j]=0
            