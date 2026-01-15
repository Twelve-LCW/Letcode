class Solution:
    def convert(self, s: str, numRows: int) -> str:
        n,r=len(s),numRows
        if r==1 or r>=n:
            return s
        t=2*r-2
        c=(n+t-1)//t*(r-1)
        mat=[['']*c for _ in range(r)]
        x,y=0,0
        for i,ch in enumerate(s):
            mat[x][y]=ch
            if i%t<r-1:
                x+=1
            else:
                x-=1
                y+=1
        return ''.join(ch for row in mat for ch in row if ch)

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        r=numRows
        t=2*r-2
        if r==1 or r>=len(s):
            return s
        mat=[[] for _ in range(r)]
        x=0
        for i,ch in enumerate(s):
            mat[x].append(ch)
            x+=1 if i%t<r-1 else -1
        return ''.join(ch for row in mat for ch in row)

# 0             0+t                    0+2t                     0+3t
# 1      t-1    1+t            0+2t-1  1+2t            0+3t-1   1+3t
# 2  t-2        2+t  0+2t-2            2+2t  0+3t-2             2+3t  
# 3             3+t                    3+2t                     3+3t
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        n, r = len(s), numRows
        if r == 1 or r >= n:
            return s
        t = r * 2 - 2
        ans = []
        for i in range(r):  # 枚举矩阵的行
            for j in range(0, n - i, t):  # 枚举每个周期的起始下标
                ans.append(s[j + i])  # 当前周期的第一个字符
                if 0 < i < r - 1 and j + t - i < n:
                    ans.append(s[j + t - i])  # 当前周期的第二个字符
        return ''.join(ans)
