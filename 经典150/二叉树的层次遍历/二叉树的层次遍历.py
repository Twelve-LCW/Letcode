# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        def dfs(node, level):
            if not node:
                return
            # 如果这是当前层的第一个节点（即最右边的节点）
            if level == len(result):
                result.append(node.val)
            # 先访问右子树（保证右边节点先被处理）
            dfs(node.right, level + 1)
            # 再访问左子树
            dfs(node.left, level + 1)
        dfs(root, 0)
        return result
    

from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        
        queue = deque([root])
        result = []
        
        while queue:
            level_size = len(queue)
            # 遍历当前层的所有节点
            for i in range(level_size):
                node = queue.popleft()
                # 如果是当前层的最后一个节点，加入结果
                if i == level_size - 1:
                    result.append(node.val)
                
                # 将下一层的节点加入队列
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        
        return result