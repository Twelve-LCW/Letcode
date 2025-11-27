class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m=len(matrix)
        # n=len(matrix[0])
        for i in range(m//2):
            for j in range((m+1)//2):
                temp=matrix[i][j]
                matrix[i][j]=matrix[m-1-j][i]
                matrix[m-1-j][i]=matrix[m-1-i][m-1-j]
                matrix[m-1-i][m-1-j]=matrix[j][m-1-i]
                matrix[j][m-1-i]=temp
