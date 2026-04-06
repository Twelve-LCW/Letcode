class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        mp={
            '2':'abc','3':'def','4':'ghi','5':'jkl','6':'mno','7':'pqrs','8':'tuv','9':'wxyz'
        }
        res=['']
        for d in digits:
            cur=[]
            for s in res:
                for c in mp[d]:
                    cur.append(s+c)
            res=cur
        return res

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        mp={
            '2':'abc','3':'def','4':'ghi','5':'jkl','6':'mno','7':'pqrs','8':'tuv','9':'wxyz'
        }
        res=[]
        n=len(digits)
        def dfs(i,s):
            if i==n:
                res.append(s)
                return
            for c in mp[digits[i]]:
                s+=c
                dfs(i+1,s)
                s=s[:-1]
        dfs(0,'')
        return res