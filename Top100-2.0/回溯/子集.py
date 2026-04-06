class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res=[[]]
        for x in nums:
            res.extend([subset+[x] for subset in res])
        return res