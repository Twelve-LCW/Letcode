class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        st0=strs[0]
        for j,c in enumerate(st0):
            for s in strs[1:]:
                if j==len(s) or s[j]!=c:
                    return st0[:j]
        return st0

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""

        strs.sort()

        first_str = strs[0]
        last_str = strs[-1]

        for i,char in enumerate(first_str):
            if char != last_str[i]:
                return first_str[:i]

        return first_str
        