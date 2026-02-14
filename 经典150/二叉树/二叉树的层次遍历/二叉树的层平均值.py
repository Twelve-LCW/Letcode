# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque


class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        deq=deque([root])
        res=[]
        while deq:
            level_size=len(deq)
            sum=0
            for _ in range(level_size):
                node=deq.popleft()
                sum+=node.val

                if node.left:
                    deq.append(node.left)
                if node.right:
                    deq.append(node.right)
            res.append(sum/level_size)
        return res