from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals = sorted(intervals, key=lambda x: (x[0],x[1]))
        n=len(intervals)
        res=[]
        if n==0 or intervals is None: return res
        i=0
        while i<n:
            left=intervals[i][0]
            right=intervals[i][1]
            while (i<n-1 and right>=intervals[i+1][0]):
                i+=1
                right=max(intervals[i][1],right)
            res.append([left,right])
            i+=1
        return res


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals = sorted(intervals, key=lambda x: x[0])
        res=[intervals[0]]
        i=0
        for start,end in intervals[1:]:
            preStart,preEnd=res[-1]
            if preEnd>=start:
                res[-1][1]=max(preEnd,end)
            else:
                res.append([start,end])
        return res