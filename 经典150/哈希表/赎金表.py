from collections import defaultdict


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        cnt=defaultdict(int)
        for c in magazine:
            cnt[c]+=1
        for s in ransomNote:
            cnt[s]-=1
            if cnt[s]<0:
                return False
        return True

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        return Counter(ransomNote) <= Counter(magazine)