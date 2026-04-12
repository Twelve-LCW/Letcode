class Solution:
    def isValid(self, s: str) -> bool:
        if len(s)%2:
            return False
        mp={')':'(',']':'[','}':'{'}
        st=[]
        for c in s:
            if c not in mp:
                st.append(c)
            elif not st or st.pop()!=mp[c]:
                return False
        return not st
    
