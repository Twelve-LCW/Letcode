class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n=len(s)
        dp=[True]+[False]*n
        maxlen=max(map(len,wordDict))
        for i in range(1,n+1):
            for j in range(max(0,i-maxlen),i):
                if dp[j] and s[j:i] in wordDict:
                    dp[i]=True
        return dp[n]