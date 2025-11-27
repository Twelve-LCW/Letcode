class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m,n=len(board),len(board[0])
        def backtrack(i,j,k):
            if board[i][j]!=word[k]:
                return False
            if k==len(word)-1:
                return True
            board[i][j]=''
            for x,y in (i,j-1),(i,j+1),(i-1,j),(i+1,j):
                if 0<=x<m and 0<=y<n and backtrack(x,y,k+1):
                    return True
            board[i][j]=word[k]
            return False
        return any(backtrack(i,j,0) for i in range(m) for j in range(n))