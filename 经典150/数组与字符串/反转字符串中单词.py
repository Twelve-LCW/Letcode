class Solution:
    def reverseWords(self, s: str) -> str:
        lst=s.split()
        l,r=0,len(lst)-1
        while l<r:
            tmp=lst[l]
            lst[l]=lst[r]
            lst[r]=tmp
            l+=1
            r-=1
        return ' '.join(lst)