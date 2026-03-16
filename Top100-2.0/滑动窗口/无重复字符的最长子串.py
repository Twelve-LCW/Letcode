from collections import defaultdict


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        cnt=defaultdict(int)
        res=0
        left=0
        for right,c in enumerate(s):
            cnt[c]+=1
            while cnt[c]>1:
                cnt[s[left]]-=1
                left+=1
            res=max(res,right-left+1)
        return res