# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from math import inf


class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        res=inf
        pre=-inf
        def dfs(root):
            if root is None:
                return
            dfs(root.left)
            nonlocal res,pre
            res=min(res,root.val-pre)
            pre=root.val
            dfs(root.right)
        dfs(root)
        return res