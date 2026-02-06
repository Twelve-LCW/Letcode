# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        return self.isSameTree(root.left,root.right)
        
    def isSameTree(self,l,r):
        if l is None or r is None:
            return l is r
        return l.val==r.val and self.isSameTree(l.left,r.right) and self.isSameTree(l.right,r.left)