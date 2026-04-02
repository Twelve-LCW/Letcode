# Definition for a binary tree node.
from math import inf


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res=-inf
        def dfs(root):
            if root is None:
                return 0
            l_val=dfs(root.left)
            l_val=max(l_val,0)
            r_val=dfs(root.right)
            r_val=max(r_val,0)

            nonlocal res
            res=max(res,root.val+r_val+l_val)

            return root.val+max(r_val,l_val)
        dfs(root)
        return res