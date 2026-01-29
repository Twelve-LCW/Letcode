from typing import List


class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key=lambda x:x[0])
        res=[points[0]]
        for start,end in points:
            preStart,preEnd=res[-1]
            if preEnd>=start:
                res[-1][0]=max(start,preStart)
                res[-1][1]=min(preEnd,end)
            else:
                res.append([start,end])
        return len(res)

class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points = sorted(points,key=lambda x:x[1])
        if not points:
            return 0
        position = points[0][1]
        ans = 1
        for point in points:
            if point[0] > position:
                position = point[1]
                ans+=1
        return ans