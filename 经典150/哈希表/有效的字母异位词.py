from collections import defaultdict


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        cnt=defaultdict(int)
        for c in s:
            cnt[c]+=1
        for c in t:
            cnt[c]-=1
            if cnt[c]<0:
                return False
        return True

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        for i in set(s):
            if s.count(i) != t.count(i):
                return False
        return True

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return Counter(s)==Counter(t)