# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        s = head
        f = head
        # 第一步：快指针走两步，慢指针走一步，直到相遇 / 快指针到链表尾
        while f and f.next:  # 必须加边界判断，防止无环时报错
            s = s.next
            f = f.next.next
            # 相遇了，说明有环
            if s == f:
                break
        # 特殊情况：无环（f走到了末尾）
        if not f or not f.next:
            return None
        
        # 第二步：找环的入口节点
        cur = head
        while s != cur:
            cur = cur.next
            s = s.next
        return s