class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row_has=[[False]*9 for _ in range(9)]
        col_has=[[False]*9 for _ in range(9)]
        box_has=[[[False]*9 for _ in range(3)] for _ in range(3)]
        for i,row in enumerate(board):
            for j,b in enumerate(row):
                if b=='.':
                    continue
                x=int(b)-1
                if row_has[i][x] or col_has[j][x] or box_has[i//3][j//3][x]: #遇到已经出现过的数据
                        return False
                row_has[i][x] = col_has[j][x] = box_has[i//3][j//3][x] = True
        return True