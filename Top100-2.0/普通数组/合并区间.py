class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals=sorted(intervals,key=lambda x:x[0])
        res=[intervals[0]]
        for start,end in intervals[1:]:
            pre_s,pre_e=res[-1]
            if pre_e>=start:
                res[-1]=[pre_s,max(end,pre_e)]
            else:
                res.append([start,end])
        return res