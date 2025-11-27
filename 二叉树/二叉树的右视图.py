# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque


class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        q=deque([root])
        res=[]
        while q:
            res.append(q[0].val)
            for _ in range(len(q)):
                node=q.popleft()
                if node.right:
                    q.append(node.right)
                if node.left:
                    q.append(node.left)
        return res
    
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res=[]
        def dfs(node,depth):
            if not node:
                return
            if depth==len(res):
                res.append(node.val)
            dfs(node.right,depth+1)
            dfs(node.left,depth+1)
        dfs(root,0)
        return res
