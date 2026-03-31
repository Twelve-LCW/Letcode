# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res=[]
        def dfs(root,depth):
            if root is None:
                return
            if len(res)==depth:
                res.append(root.val)
            dfs(root.right,depth+1)
            dfs(root.left,depth+1)
        dfs(root,0)
        return res

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res=[]
        cur=[root]
        while cur:
            res.append(cur[-1].val)
            nxt=[]
            for node in cur:
                if node.left: nxt.append(node.left)
                if node.right: nxt.append(node.right)
            cur=nxt
        return res

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        q=deque([root])
        ans=[]
        while q:
            ans.append(q[0].val)
            n=len(q)
            for _ in range(n):
                node=q.popleft()
                if node.right:
                    q.append(node.right)        #先放右边
                if node.left:
                    q.append(node.left)
        return ans