class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res=[]
        candidates.sort()
        n=len(candidates)
        def dfs(start,path:list,total):
            if total==target:
                res.append(path.copy())
                return
            for i in range(start,n):
                if total+candidates[i]>target:
                    break
                path.append(candidates[i])
                dfs(i,path,total+candidates[i]) #可以重复使用，所以从现在这个数字开始
                path.pop()
        dfs(0,[],0)
        return res