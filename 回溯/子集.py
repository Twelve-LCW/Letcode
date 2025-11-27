class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n=len(nums)
        res=[]
        combine=[]
        def backtrack(s):
            res.append(combine[:])
            for i in range(s,n):
                combine.append(nums[i])
                backtrack(i+1)
                combine.pop()
        backtrack(0)
        return res

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = [[]]
        for x in nums:
            res.extend([subset + [x] for subset in res])
        return res