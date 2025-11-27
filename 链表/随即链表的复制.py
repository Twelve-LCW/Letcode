"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""
from collections import defaultdict


# class Node:
#     def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
#         self.val = int(x)
#         self.next = next
#         self.random = random

class Solution:
    def __init__(self):
        self.map = defaultdict(Node)  # 改为实例变量
    #哈希+回溯
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if(head==None):
            return None
        if(not self.map.get(head)):
            headnew=Node(head.val)
            self.map[head]=headnew
            headnew.random=self.copyRandomList(head.random)
            headnew.next=self.copyRandomList(head.next)
        
        return self.map.get(head)
    

    #哈希+两次遍历
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if(head is None):
            return None
        map = defaultdict(Node)
        cur=head
        while cur:
            map[cur]=Node(cur.val)
            cur=cur.next
        
        cur=head
        while cur:
            clone=map.get(cur)
            clone.next=map.get(cur.next)
            clone.random=map.get(cur.random)
            cur=cur.next
        
        return map.get(head)
    
    #模拟+拆分
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if head==None:
            return None
        #添加复制节点
        cur=head
        while cur:
            cur.next=Node(cur.val,cur.next)
            cur=cur.next.next
        #复制节点指向新的random节点
        cur=head
        while cur:
            if cur.random:
                cur.next.random=cur.random.next
            cur=cur.next.next
        
        #拆分链表
        cur=head.next
        while cur.next:
            cur.next=cur.next.next #指向复制节点
            cur=cur.next
        
        return head.next
        