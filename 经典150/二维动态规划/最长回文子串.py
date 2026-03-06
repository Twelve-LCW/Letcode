class Solution:
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

class Solution:
    def longestPalindrome(self, s: str) -> str:
        n=len(s)
        ans_left=ans_right=0
        for i in range(n):
            l=r=i
            while l>=0 and r<n and s[l]==s[r]:
                l-=1
                r+=1
            if ans_right-ans_left<r-l-1:
                ans_left,ans_right=l+1,r
        
        for i in range(n):
            l,r=i,i+1
            while l>=0 and r<n and s[l]==s[r]:
                l-=1
                r+=1
            if r-l-1>ans_right-ans_left:
                ans_left,ans_right=l+1,r
        return s[ans_left:ans_right] 