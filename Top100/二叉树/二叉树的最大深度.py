# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    #自底向上
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        l_depth=self.maxDepth(root.left)
        r_depth=self.maxDepth(root.right)
        return max(l_depth,r_depth)+1


    #自顶向下
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        self.ans=0
        def dfs(node,depth):
            if node is None:
                return
            depth+=1
            self.ans=max(self.ans,depth)
            dfs(node.left,depth)
            dfs(node.right,depth)
        dfs(root,0)
        return self.ans
        