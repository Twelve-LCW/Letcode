# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from math import inf


class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res=-inf
        def dfs(node):
            if node is None:
                return 0
            l_val=dfs(node.left)
            r_val=dfs(node.right)

            nonlocal res
            res=max(res,l_val+r_val+node.val)

            return max(node.val+max(l_val,r_val),0)
        dfs(root)
        return res

