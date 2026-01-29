class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals=sorted(intervals,key=lambda x:x[0])
        res=[intervals[0]]
        for start,end in intervals[1:]:
            preStart,preEnd=res[-1]
            if preEnd>=start:
                res[-1][1]=max(end,preEnd)
            else:
                res.append([start,end])
        return res