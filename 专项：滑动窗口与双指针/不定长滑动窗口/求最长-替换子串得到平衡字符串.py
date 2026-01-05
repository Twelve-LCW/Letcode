from collections import Counter
from math import inf


class Solution:
    def balancedString(self, s: str) -> int:
        m=len(s)//4
        cnt=Counter(s)
        if len(cnt)==4 and min(cnt.values())==m:
            return 0
        res,left=inf,0
        for right,c in enumerate(s) :
            cnt[c]-=1
            while max(cnt.values())<=m: #cnt为窗口之外的值
                res=min(res,right-left+1)
                cnt[s[left]]+=1
                left+=1
        return res