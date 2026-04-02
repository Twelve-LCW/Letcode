# Definition for a binary tree node.
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if root is None:
            return root
        res=[]
        stack=deque([root])
        while stack:
            node=stack.pop()
            res.append(node.val)
            if node.right: stack.append(node.right)
            if node.left: stack.append(node.left)
        root.left=None
        root.right=None
        cur=root
        for i in range(1,len(res)):
            cur.right=TreeNode(val=res[i])
            cur=cur.right
        return root

class Solution:
    head = None

    def flatten(self, root: Optional[TreeNode]) -> None:
        if root is None:
            return
        self.flatten(root.right)
        self.flatten(root.left)
        root.left=None
        root.right=self.head # 头插法，相当于链表的 root.next = head
        self.head=root # 头插法，相当于链表的 root.next = head