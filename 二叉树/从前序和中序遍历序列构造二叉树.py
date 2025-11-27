# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return None
        val = preorder[0]
        root = TreeNode(val)
        index = inorder.index(val)
        root.left=self.buildTree(preorder[1:index+1],inorder[0:index])
        root.right=self.buildTree(preorder[index+1:],inorder[index+1:])
        return root
    
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        index = {x: i for i, x in enumerate(inorder)}

        def dfs(pre_l: int, pre_r: int, in_l: int, in_r: int) -> Optional[TreeNode]:
            if pre_l == pre_r:  # 空节点
                return None
            left_size = index[preorder[pre_l]] - in_l  # 左子树的大小
            left = dfs(pre_l + 1, pre_l + 1 + left_size, in_l, in_l + left_size)
            right = dfs(pre_l + 1 + left_size, pre_r, in_l + 1 + left_size, in_r)
            return TreeNode(preorder[pre_l], left, right)

        return dfs(0, len(preorder), 0, len(inorder))  # 左闭右开区间