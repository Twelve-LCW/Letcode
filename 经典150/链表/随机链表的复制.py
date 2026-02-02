"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if head==None:
            return None
        cur=head
        #按照next复制节点，接在原来节点后面
        while cur:
            cur.next=Node(cur.val,cur.next)
            cur=cur.next.next
        
        #把random接上
        cur=head
        while cur:
            if cur.random:
                cur.next.random=cur.random.next
            cur=cur.next.next
        
        #拆分链表
        cur=head.next
        while cur.next:
            cur.next=cur.next.next
            cur=cur.next
        return head.next
    

"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head: 
            return None
        old_to_new={}
        cur=head

        while cur:
            node = Node(x=cur.val)
            old_to_new[cur]= node
            cur=cur.next

        cur=head    
        while cur:
            copy=old_to_new[cur]
            copy.next=old_to_new[cur.next] if cur.next else None
            copy.random=old_to_new[cur.random] if cur.random else None
            cur=cur.next
        return old_to_new[head]