# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        index={x:i for i,x in enumerate(inorder)}

        def dfs(pre_l, pre_r, in_l, in_r):
            # 左闭右开区间：pre_l == pre_r 表示区间内没有元素，返回空
            if pre_l == pre_r:
                return None
            # 根节点值是前序区间的第一个元素（pre_l 位置，因为左闭）
            root_val = preorder[pre_l]
            # 计算左子树大小：根节点在中序中的索引 - 中序左边界
            left_size = index[root_val] - in_l
            
            # 左子树的前序区间：[pre_l+1, pre_l+1+left_size)
            # 左闭右开，所以右边界是 左边界 + 左子树大小（刚好包含left_size个元素）
            left = dfs(pre_l+1, pre_l+1+left_size, in_l, in_l+left_size)
            
            # 右子树的前序区间：[pre_l+1+left_size, pre_r)
            # 中序区间：[in_l+left_size+1, in_r)（跳过根节点）
            right = dfs(pre_l+1+left_size, pre_r, in_l+left_size+1, in_r)
            
            return TreeNode(root_val, left, right)
        return dfs(0,len(preorder),0,len(inorder))

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        index={x:i for i,x in enumerate(inorder)}

        def dfs(pre_l, pre_r, in_l, in_r):
            # 左闭右闭：空区间条件是 pre_l > pre_r
            if pre_l > pre_r:
                return None
            root_val = preorder[pre_l]
            left_size = index[root_val] - in_l
            
            # 左子树前序区间：[pre_l+1, pre_l+left_size]（需要减1）
            left = dfs(pre_l+1, pre_l+left_size, in_l, in_l+left_size-1)
            
            # 右子树前序区间：[pre_l+left_size+1, pre_r]
            right = dfs(pre_l+left_size+1, pre_r, in_l+left_size+1, in_r)
    
            return TreeNode(root_val, left, right)  

        return dfs(0,len(preorder)-1,0,len(inorder)-1)