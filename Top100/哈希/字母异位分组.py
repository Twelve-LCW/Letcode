from collections import defaultdict  
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mp=defaultdict(list)
        for st in strs:
            key=''.join(sorted(st))
            mp[key].append(st)
        return list(mp.values())
