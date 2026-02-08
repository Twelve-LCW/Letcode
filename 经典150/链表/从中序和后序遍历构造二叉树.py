# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        index={x:i for i,x in enumerate(inorder)}

        def dfs(pos_l,pos_r,in_l,in_r):
            if pos_l>pos_r:
                return None
            
            root_val=postorder[pos_r]
            left_size=index[root_val]-in_l

            left=dfs(pos_l,pos_l+left_size-1,in_l,in_l+left_size-1)
            right=dfs(pos_l+left_size,pos_r-1,in_l+left_size+1,in_r)

            return TreeNode(root_val,left,right)
        
        return dfs(0,len(postorder)-1,0,len(inorder)-1)