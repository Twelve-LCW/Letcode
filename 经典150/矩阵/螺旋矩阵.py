class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        left=top=0
        right=len(matrix[0])-1
        bottom=len(matrix)-1
        res=[]
        while left<=right and top<=bottom:
            for i in range(left,right+1):
                res.append(matrix[top][i])
            for i in range(top+1,bottom+1):
                res.append(matrix[i][right])
            if left<right and top<bottom:
                for i in range(right-1,left-1,-1):
                    res.append(matrix[bottom][i])
                for i in range(bottom-1,top,-1):
                    res.append(matrix[i][left])
            left+=1
            right-=1
            top+=1
            bottom-=1
        return res
DIRS = (0, 1), (1, 0), (0, -1), (-1, 0)  # 右下左上

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m, n = len(matrix), len(matrix[0])
        ans = []
        i = j = di = 0
        for _ in range(m * n):  # 一共走 mn 步
            ans.append(matrix[i][j])
            matrix[i][j] = None  # 标记，表示已经访问过（已经加入答案）
            x, y = i + DIRS[di][0], j + DIRS[di][1]  # 下一步的位置
            # 如果 (x, y) 出界或者已经访问过
            if x < 0 or x >= m or y < 0 or y >= n or matrix[x][y] is None:
                di = (di + 1) % 4  # 右转 90°
            i += DIRS[di][0]
            j += DIRS[di][1]  # 走一步
        return ans