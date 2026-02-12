# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # 递归终止条件（核心边界）
        # 1. 当前节点为空（遍历到叶子节点的子节点，无意义）
        # 2. 当前节点就是p或q（找到目标节点，直接返回）
        if root is None or root is p or root is q:
            return root
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        # 情况1：左子树和右子树都找到了目标节点（p和q分别在左右子树）
        # 说明当前root就是最近公共祖先
        if left and right:
            return root
        # 情况2：只有左子树找到目标节点（p和q都在左子树）
        if left:
            return left
        # 情况3：只有右子树找到目标节点（p和q都在右子树）
        if right:
            return right

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        stack = [root]
        parent = {root: None}
        while p not in parent or q not in parent:
            node = stack.pop()
            if node.left:
                parent[node.left] = node
                stack.append(node.left)
            if node.right:
                parent[node.right] = node
                stack.append(node.right)
        ancestors = set()
        while p:
            ancestors.add(p)
            p = parent[p]
        while q not in ancestors:
            q = parent[q]
        return q