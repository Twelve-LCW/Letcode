class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        n=len(candidates)
        res=[]
        combine=[]
        def backtrack(sum,combine,s):
            if sum==target:
                res.append(combine[:])
                return
            elif sum>target:
                return
            for i in range(s,n):
                combine.append(candidates[i])
                backtrack(sum+candidates[i],combine,i)
                combine.pop()
        backtrack(0,combine,0)
        return res
        
