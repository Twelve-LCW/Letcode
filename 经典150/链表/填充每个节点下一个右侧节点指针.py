"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
from itertools import pairwise


class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if root is None:
            return None
        q=[root]
        while q:
            #从左到右依次连接
            for x,y in pairwise(q):
                x.next=y
            tmp=q
            q=[]
            for node in tmp:
                if node.left: q.append(node.left)
                if node.right: q.append(node.right)
        return root


class Solution:
    def connect(self, root: 'Node') -> 'Node':
        cur=root
        while cur:
            nxt=dummy=Node()
            while cur:
                if cur.left:
                    nxt.next=cur.left
                    nxt=cur.left
                if cur.right:
                    nxt.next=cur.right
                    nxt=cur.right
                cur=cur.next
            cur=dummy.next
        return root
