class Solution:
    def partition(self, s: str) -> List[List[str]]:
        n=len(s)
        res=[]
        path=[]
        def backtrack(i):
            if i==n:
                res.append(path.copy())
                return
            for j in range(i,n):
                t=s[i:j+1]
                if t==t[::-1]:
                    path.append(t)
                    backtrack(j+1)
                    path.pop()
        backtrack(0)
        return res
    
    def partition(self, s: str) -> List[List[str]]:
        n=len(s)
        res=[]
        path=[]
        def backtrack(i,start):
            if i==n:
                res.append(path.copy())
                return
            if i<n-1:
                backtrack(i+1,start)
            t=s[start:i+1]
            if t==t[::-1]:
                path.append(t)
                backtrack(i+1,i+1)
                path.pop()

        backtrack(0,0)
        return res