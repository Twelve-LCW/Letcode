# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        p0 = dummy = ListNode(next=head)
        for _ in range(left - 1):
            p0 = p0.next

        pre = None
        cur = p0.next
        for _ in range(right - left + 1):
            nxt = cur.next
            cur.next = pre  # 每次循环只修改一个 next，方便大家理解
            pre = cur
            cur = nxt

        # 见视频
        p0.next.next = cur
        p0.next = pre
        return dummy.next

from typing import Optional

# 定义链表节点类（方便代码独立运行）
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        # 虚拟头节点，处理left=1时的边界情况
        dummy = ListNode()
        dummy.next = head
        pre = dummy
        cur = head
        i = 1
        
        # 1. 移动到反转区间的前一个节点（pre）和反转起始节点（cur）
        while i < left:
            pre = pre.next
            cur = cur.next
            i += 1
        
        # 记录反转区间的前驱节点（固定不变）和反转起始节点（反转后会变成区间末尾）
        reverse_pre = pre
        reverse_start = cur
        
        # 2. 反转[left, right]区间内的节点
        next_node = None
        while i <= right:
            next_node = cur.next  # 保存下一个节点
            cur.next = pre        # 反转当前节点的指针
            pre = cur             # pre 后移
            cur = next_node       # cur 后移
            i += 1
        
        # 3. 处理反转区间的首尾衔接（关键修复）
        reverse_pre.next = pre       # 前驱节点指向反转后的区间头
        reverse_start.next = cur     # 原区间头（现区间尾）指向反转区间后的第一个节点
        
        return dummy.next
        