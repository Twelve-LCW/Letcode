from collections import Counter


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        cnt=Counter(s1)
        n=len(s1)
        left=0
        for right,c in enumerate(s2):
            cnt[c]-=1
            while cnt[c]<0:
                cnt[s2[left]]+=1
                left+=1
            if right-left+1==n:
                return True
        return False