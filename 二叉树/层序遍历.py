# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res=[]
        stack=deque([root])
        while stack:
            cur=[]
            for _ in range(len(stack)):
                node=stack.popleft()
                if node is not None:
                    cur.append(node.val)
                    stack.append(node.left)
                    stack.append(node.right)
            if cur:res.append(cur)
        return res
