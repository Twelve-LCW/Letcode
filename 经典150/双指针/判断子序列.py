class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if not s:
            return True
        m=len(s)
        i=0
        for c in t:
            if s[i]==c:
                i+=1
                if i==m:
                    return True
        return False
    
    def isSubsequence(self, s: str, t: str) -> bool:
        m,n=len(s),len(t)
        i,j=0,0
        if m==0:
            return True
        while j<n:
            if s[i]==t[j]:
                i+=1
                if i==m:
                    return True
            j+=1
        return False