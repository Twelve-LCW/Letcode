class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res=[]
        path=['']*(n*2)
        def backtrack(left,right):
            if right==n:
                res.append(''.join(path))
                return
            if left<n:
                path[left+right]='('
                backtrack(left+1,right)
            if left>right:
                path[left+right]=')'
                backtrack(left,right+1)
        backtrack(0,0)
        return res

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        path = []  # 记录左括号的下标

        # 目前填了 i 个括号
        # balance = 这 i 个括号中的左括号个数 - 右括号个数
        def dfs(i: int, balance: int) -> None:
            if len(path) == n:
                s = [')'] * (n * 2)
                for j in path:
                    s[j] = '('
                ans.append(''.join(s))
                return
            # 枚举填 right=0,1,2,...,balance 个右括号
            for right in range(balance + 1):
                # 先填 right 个右括号，然后填 1 个左括号，记录左括号的下标 i+right
                path.append(i + right)
                dfs(i + right + 1, balance - right + 1)
                path.pop()  # 恢复现场

        dfs(0, 0)
        return ans