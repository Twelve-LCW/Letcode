class Solution:
    def isValid(self, s: str) -> bool:
        if len(s)%2:
            return False
        mp={')':'(',']':'[','}':'{'}
        st=[]
        for c in s:
            if c not in mp:
                st.append(c) #c是左括号
            elif not st or st.pop()!=mp[c]: #c是右括号,但前一个不是匹配的左括号
                return False
        return not st