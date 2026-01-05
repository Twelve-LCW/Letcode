# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.res=[]
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root:
            #先遍历左节点
            self.inorderTraversal(root.left)
            #根节点
            self.res.append(root.val)
            #最后遍历右节点
            self.inorderTraversal(root.right)
        return self.res
    #染色法
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
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
        return res
    

    #传统方法
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
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
        return res