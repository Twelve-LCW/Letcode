# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        def dfs(root):
            if root is None:
                return 0
            return dfs(root.left)+dfs(root.right)+1
        return dfs(root)
    

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import Optional

class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        # 辅助函数：计算二叉树的左深度（只沿着左子节点遍历）
        # 对于完全二叉树，左深度可以快速判断子树是否为满二叉树
        def depth(node):
            # 如果节点为空，深度为0
            if not node:
                return 0
            # 只遍历左子树，因为完全二叉树的左子树一定是连续的
            return depth(node.left) + 1

        # 核心递归函数：计算以node为根的完全二叉树的节点数
        def dfs(node):
            # 递归终止条件：空节点的节点数为0
            if not node:
                return 0
            
            # 计算当前节点左子树的左深度
            left_depth = depth(node.left)
            # 计算当前节点右子树的左深度
            right_depth = depth(node.right)
            
            # 关键判断：如果左右子树的左深度相等
            # 说明左子树是满二叉树（完全二叉树特性）
            if left_depth == right_depth:
                # 满二叉树节点数公式：2^深度 - 1
                # 当前节点(1) + 左满子树节点数(2^left_depth - 1) + 递归计算右子树节点数
                return 1 + (2 ** left_depth - 1) + dfs(node.right)
            # 否则，右子树是满二叉树（深度比左子树小1）
            else:
                # 当前节点(1) + 右满子树节点数(2^right_depth - 1) + 递归计算左子树节点数
                return 1 + (2 ** right_depth - 1) + dfs(node.left)

        # 从根节点开始计算
        return dfs(root)
