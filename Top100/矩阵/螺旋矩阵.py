from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res=[]
        left=0
        right=len(matrix[0])-1  
        top=0
        bottom=len(matrix)-1
        while left<=right and top<=bottom:
            for i in range(left,right+1):
                res.append(matrix[top][i])
            for i in range(top+1,bottom+1):
                res.append(matrix[i][right])
            if left<right and top<bottom:
                for i in range(right-1,left,-1):
                    res.append(matrix[bottom][i])
                for i in range(bottom,top,-1):
                    res.append(matrix[i][left])
            top+=1
            right-=1
            bottom-=1
            left+=1
        return res