# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from math import inf


class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        ans=-inf
        def dfs(node):
            if node is None:
                return 0
            l_val=dfs(node.left)
            l_val=max(l_val,0) #分支最大值为负数，则丢弃考虑分支
            r_val=dfs(node.right)
            r_val=max(r_val,0)
            nonlocal ans
            
            #递归过程进行更新
            ans=max(ans,l_val+r_val+node.val)
            return node.val+max(l_val,r_val)
        dfs(root)
        return ans