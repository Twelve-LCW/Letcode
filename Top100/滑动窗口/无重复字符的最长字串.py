class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # string=list(s)
        smap=set()
        res=0
        n=len(s)
        l,r=0,0
        while r<n:
            while s[r] in smap:
                smap.remove(s[l])
                l+=1
            res=max(res,r-l+1)
            smap.add(s[r])
            r+=1
        return res