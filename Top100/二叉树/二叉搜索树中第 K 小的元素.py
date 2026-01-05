# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        stack=[(0,root)]
        res=[]
        while stack:
            color,node=stack.pop()
            if node is None:
                continue
            if color==0:
                stack.append((0,node.right))
                stack.append((1,node))
                stack.append((0,node.left))
            else:
                res.append(node.val)
        return res[k-1]
    
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        res=[]
        def dfs(root):
            if root:
                dfs(root.left)
                res.append(root.val)
                dfs(root.right)
        dfs(root)
        return res[k-1]
    

    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        stack=[]
        res=[]
        cur=root
        while cur or stack:
            while cur:
                stack.append(cur)
                cur=cur.left
            cur=stack.pop()
            res.append(cur.val)

            cur=cur.right
        return res[k-1]
    

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        ans = 0
        def dfs(node: Optional[TreeNode]) -> None:
            nonlocal k, ans
            if node is None or k == 0:
                return
            dfs(node.left)  # 左
            k -= 1
            if k == 0:
                ans = node.val  # 根
            dfs(node.right)  # 右
        dfs(root)
        return ans


class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        def dfs(node: Optional[TreeNode]) -> int:
            if node is None:
                return -1  # 题目保证节点值非负，用 -1 表示没有找到
            left_res = dfs(node.left)
            if left_res != -1:  # 答案在左子树中
                return left_res
            nonlocal k
            k -= 1
            if k == 0:  # 答案就是当前节点
                return node.val
            return dfs(node.right)  # 右子树会返回答案或者 -1
        return dfs(root)
