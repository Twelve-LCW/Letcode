# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.stack=[]
        while root:
            self.stack.append(root)
            root=root.left
        

    def next(self) -> int:
        cur=self.stack.pop()
        node=cur.right
        while node:
            self.stack.append(node)
            node=node.left
        return cur.val
        

    def hasNext(self) -> bool:
        return len(self.stack)>0
        


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()

class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.queue = deque()
        self.inorder(root)
        
    def inorder(self, root: Optional[TreeNode]):
        if not root: return
        self.inorder(root.left)
        self.queue.append(root.val)
        self.inorder(root.right)

    def next(self) -> int:
        return self.queue.popleft()

    def hasNext(self) -> bool:
        return len(self.queue) > 0

