from collections import defaultdict
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        cnt = defaultdict(int)
        cnt[0] = 1  # s[0]=0 单独统计
        ans = s = 0
        for x in nums:
            s += x
            ans += cnt[s - k] #前缀和
            cnt[s] += 1
        return ans