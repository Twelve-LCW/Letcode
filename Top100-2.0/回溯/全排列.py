class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res=[]
        n=len(nums)
        choose=[False]*n
        path=[0]*n
        def dfs(i):
            if i==n:
                res.append(path.copy())
                return
            for j,on in enumerate(choose):
                if not on:
                    path[i]=nums[j]
                    choose[j]=True
                    dfs(i+1)
                    choose[j]=False
        dfs(0)
        return res