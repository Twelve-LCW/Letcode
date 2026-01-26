class Solution:
    def isHappy(self, n: int) -> bool:
        def get_next(n):
            s=0
            while n>0:
                num=n%10
                s+=num*num
                n=n//10
            return s
        
        seen=set()
        while n!=1 and n not in seen:
            seen.add(n)
            n=get_next(n)
        return n==1

class Solution:
    def isHappy(self, n: int) -> bool:
        def get_next(n):
            s=0
            while n>0:
                num=n%10
                s+=num*num
                n=n//10
            return s
        slow,fast=n,get_next(n)
        while slow!=fast:
            slow=get_next(slow)
            fast=get_next(fast)
            fast=get_next(fast)
        return slow==1


