# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        index={x:i for i,x in enumerate(inorder)}

        def dfs(pre_l,pre_r,in_l,in_r):
            if pre_l>pre_r:
                return None
            root_val=preorder[pre_l]
            left_size=index[root_val]-in_l

            left=dfs(pre_l+1,pre_l+left_size,in_l,in_l+left_size-1)
            right=dfs(pre_l+left_size+1,pre_r,in_l+left_size+1,in_r)

            return TreeNode(val=root_val,left=left,right=right)
        return dfs(0,len(preorder)-1,0,len(inorder)-1)