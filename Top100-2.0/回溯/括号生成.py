class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        path=[]
        res=[]
        def dfs(l,r):
            if len(path)==2*n:
                res.append(''.join(path))
                return
            if l<n:
                path.append('(')
                dfs(l+1,r)
                path.pop()
            if l>r:
                path.append(')')
                dfs(l,r+1)
                path.pop()
        dfs(0,0)
        return res