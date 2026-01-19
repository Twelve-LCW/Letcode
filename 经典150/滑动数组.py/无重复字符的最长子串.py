class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        se=set()
        res=0
        n=len(s)
        l=r=0
        while r<n:
            while s[r] in se:
                se.remove(s[l])
                l+=1
            res=max(res,r-l+1)
            se.add(s[r])
            r+=1
        return res