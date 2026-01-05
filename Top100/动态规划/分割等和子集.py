class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        s=sum(nums)
        if s%2:
            return False
        s//=2
        n=len(nums)
        f=[[False]*(s+1) for _ in range(n+1)] #表示到位置i，和j的子序列是否存在
        f[0][0]=True #初始状态设置为True
        for i,x in enumerate(nums):
            for j in range(s+1):
                f[i+1][j]=j>=x and f[i][j-x] or f[i][j]
        return f[n][s]
    
    def canPartition(self, nums: List[int]) -> bool:
        s=sum(nums)
        if s%2:
            return False
        s//=2
        f=[True]+[False]*s
        s2=0
        for i,x in enumerate(nums):
            s2=min(s2+x,s)
            for j in range(s2,x-1,-1):
                f[j]=f[j] or f[j-x]
            if f[s]:
                return True
        return False