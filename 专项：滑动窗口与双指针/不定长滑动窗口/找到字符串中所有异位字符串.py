from collections import Counter


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        res=[]
        n=len(p)
        cnt=Counter(p)
        left=0
        for right,c in enumerate(s):
            cnt[c]-=1 #右端字母进入
            while cnt[c]<0:
                cnt[s[left]]+=1
                left+=1
            if right-left+1==n:
                res.append(left)
        return res
