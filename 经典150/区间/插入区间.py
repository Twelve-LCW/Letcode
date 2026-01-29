class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res=[]
        intervals.append(newInterval)
        intervals.sort(key=lambda x:x[0])
        res=[intervals[0]]
        for start,end in intervals[1:]:
            preStart,preEnd=res[-1]
            if preEnd>=start:
                res[-1][1]=max(preEnd,end)
            else:
                res.append([start,end])
        return res
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        i = 0
        n = len(intervals)
        
        # 1. 添加所有在 newInterval 左侧且不重叠的区间
        while i < n and intervals[i][1] < newInterval[0]:
            res.append(intervals[i])
            i += 1
        
        # 2. 合并所有与 newInterval 重叠的区间
        while i < n and intervals[i][0] <= newInterval[1]:
            newInterval[0] = min(intervals[i][0], newInterval[0])
            newInterval[1] = max(intervals[i][1], newInterval[1])
            i += 1
        res.append(newInterval)  # 添加合并后的新区间
        
        # 3. 添加所有在 newInterval 右侧且不重叠的区间
        while i < n:
            res.append(intervals[i])
            i += 1
        
        return res