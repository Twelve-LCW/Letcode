class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res=[]
        n=len(candidates)
        def dfs(start,path:list,total):
            if total==target:
                res.append(path[:])
                return
            for i in range(start,n):
                if total+candidates[i]>target:
                    break
                path.append(candidates[i])
                dfs(i,path,total+candidates[i])
                path.pop()
        dfs(0,[],0)
        return res