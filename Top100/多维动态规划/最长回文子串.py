class Solution:
    #动态规划方法
    def longestPalindrome(self, s: str) -> str:
        n=len(s)
        if n==0:
            return ""
        dp=[[False]*n for _ in range(n)] #dp[i][j]表示从i到j是否为回文子串
        res=s[0]
        maxlen=1 #最小的回文子串就一个字母，所以是1

        for i in range(n-1,-1,-1):#从左下角开始，往右上角，因为要保证j>=i
            for j in range(i,n):
                if i==j: #如果是从i到i,就是只有一个字母
                    dp[i][j]=True #是回文串，不会超过maxlen=1
                elif s[i]==s[j]: #如果两个字母相同
                    if j==i+1 or dp[i+1][j-1]: #可能是两个相邻的，或者是他们中间的是回文串
                        dp[i][j]=True
                        if j-i+1>maxlen: #更新最长回文串
                            maxlen=j-i+1
                            res=s[i:j+1]
        return res
    
    #中心扩展方法
    def longestPalindrome(self, s: str) -> str:
        n=len(s)
        ans_left=ans_right=0

        #奇数回文串
        for i in range(n):
            l=r=i
            while l>=0 and r<n and s[l]==s[r]:
                l-=1
                r+=1
            #结束后，判断新的回文串和原来的大小 s[l+1] 到 s[r-1]
            if r-l-1>ans_right-ans_left:
                ans_left,ans_right=l+1,r # 左闭右开区间
        
        #偶数回文串
        for i in range(n-1):
            l,r=i,i+1
            while l>=0 and r<n and s[l]==s[r]:
                l-=1
                r+=1
            #结束后，判断新的回文串和原来的大小 s[l+1] 到 s[r-1]
            if r-l-1>ans_right-ans_left:
                ans_left,ans_right=l+1,r # 左闭右开区间
        return s[ans_left:ans_right]
    
    #中心扩展法升级版本
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        ans_left = ans_right = 0

        for i in range(2 * n - 1):
            l, r = i // 2, (i + 1) // 2
            while l >= 0 and r < n and s[l] == s[r]:
                l -= 1
                r += 1
            # 循环结束后，s[l+1] 到 s[r-1] 是回文串
            if r - l - 1 > ans_right - ans_left:
                ans_left, ans_right = l + 1, r  # 左闭右开区间

        return s[ans_left: ans_right]
