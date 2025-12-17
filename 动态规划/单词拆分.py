class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n=len(s)
        dp=[False]*(n+1)
        dp[0]=True
        for i in range(1,n+1):
            for j in range(i):
                if dp[j] and s[j:i] in wordDict:
                    dp[i]=True
                    break #找到一种就可以了 退出
        return dp[n]

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n=len(s)
        dp=[True]+[False]*n
        maxlen=max(map(len,wordDict))
        for i in range(1,n+1):
            for j in range(max(0,i-maxlen),i):
                if dp[j] and s[j:i] in wordDict:
                    dp[i]=True
                    break #找到一种就可以了 退出
        return dp[n]