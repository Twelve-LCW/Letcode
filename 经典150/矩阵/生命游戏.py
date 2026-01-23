class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        neighbors = [(1,0), (1,-1), (0,-1), (-1,-1), (-1,0), (-1,1), (0,1), (1,1)]
        rows,cols=len(board),len(board[0])
        board_copy = [row[:] for row in board]

        for i in range(rows):
            for j in range(cols):
                s=0
                for neighbor in neighbors:
                    r=i+neighbor[0]
                    c=j+neighbor[1]

                    if (r<rows and r>=0) and (c<cols and c>=0) and board_copy[r][c]==1:
                        s+=1
                    
                #规则
                if s<2 or s>3:
                        board[i][j]=0
                elif s==3:
                     board[i][j]=1
        
class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m, n = len(board), len(board[0])
        
        # Directions for the 8 neighbors
        neighbors = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

        for r in range(m):
            for c in range(n):
                # Count live neighbors
                live_neighbors = 0
                for dr, dc in neighbors:
                    nr, nc = r + dr, c + dc
                    # We check if the absolute value is 1 or 2 (meaning it was originally alive)
                    if 0 <= nr < m and 0 <= nc < n and abs(board[nr][nc]) in [1, 2]:
                        live_neighbors += 1

                # Apply Game of Life rules
                if board[r][c] == 1:
                    if live_neighbors < 2 or live_neighbors > 3:
                        board[r][c] = 2  # Mark as "was alive, now dead"
                else:
                    if live_neighbors == 3:
                        board[r][c] = 3  # Mark as "was dead, now alive"

        # Final pass: update the board to the new states (0 or 1)
        for r in range(m):
            for c in range(n):
                if board[r][c] == 2:
                    board[r][c] = 0
                elif board[r][c] == 3:
                    board[r][c] = 1
class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        import numpy as np
        r, c = len(board), len(board[0])
        # 下面两行做 zero padding
        board_exp = np.array([[0 for _ in range(c + 2)] for _ in range(r + 2)])
        board_exp[1:1 + r, 1:1 + c] = np.array(board)
        # 设置卷积核
        kernel = np.array([[1, 1, 1], [1, 0, 1], [1, 1, 1]])
        # 开始卷积
        for i in range(1, r + 1):
            for j in range(1, c + 1):
                # 统计细胞周围 8 个位置的状态
                temp_sum = np.sum(kernel * board_exp[i - 1:i + 2, j - 1:j + 2])
                # 按照题目规则进行判断
                if board_exp[i, j] == 1:
                    if temp_sum < 2 or temp_sum > 3:
                        board[i - 1][j - 1] = 0
                else:
                    if temp_sum == 3:
                        board[i - 1][j - 1] = 1  