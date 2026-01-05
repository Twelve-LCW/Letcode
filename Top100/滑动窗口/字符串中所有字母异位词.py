#定滑窗口
from typing import Counter, List


class Solution:
    def findAnagrams(self, s: str, p: str) -> list[int]:
        m,n=len(s),len(p)
        l=0
        r=l+n-1
        p_list=''.join(sorted(p))
        res=[]
        while r<m:
            cur_list=''.join(sorted(s[l:r+1]))
            if cur_list==p_list:
                res.append(l)
            l+=1
            r+=1
        return res

#动滑窗口
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        ans = []
        cnt = Counter(p)  # 统计 p 的每种字母的出现次数
        left = 0
        n=len(p)
        for right, c in enumerate(s):
            cnt[c] -= 1  # 右端点字母进入窗口
            while cnt[c] < 0:  # 字母 c 太多了
                cnt[s[left]] += 1  # 左端点字母离开窗口
                left += 1
            if right - left + 1 == n:  # s' 和 p 的每种字母的出现次数都相同
                ans.append(left)  # s' 左端点下标加入答案
        return ans