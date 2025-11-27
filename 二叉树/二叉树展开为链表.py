# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque


class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root:
            return
        stack=deque()
        stack.append(root)
        res=[]
        while stack:
            node=stack.pop()
            res.append(node.val)
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
        root.left=None
        root.right=None
        cur=root
        for i in range(1,len(res)):
            cur.right=TreeNode(res[i])
            cur=cur.right

class Solution:
    def flatten(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None:
            return None
        left_tail = self.flatten(root.left)
        right_tail = self.flatten(root.right)
        if left_tail:
            left_tail.right = root.right  # 左子树链表 -> 右子树链表
            root.right = root.left  # 当前节点 -> 左右子树合并后的链表
            root.left = None
        return right_tail or left_tail or root
class Solution:
    head = None

    def flatten(self, root: Optional[TreeNode]) -> None:
        if root is None:
            return
        self.flatten(root.right)
        self.flatten(root.left)
        root.left = None
        root.right = self.head  # 头插法，相当于链表的 root.next = head
        self.head = root  # 现在链表头节点是 root





