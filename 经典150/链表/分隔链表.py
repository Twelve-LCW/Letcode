# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        cur=head
        l1=ListNode()
        l2=ListNode()
        cur1=l1
        cur2=l2
        while cur:
            if cur.val<x:
                cur1.next=cur
                cur1=cur1.next
            else:
                cur2.next=cur
                cur2=cur2.next
            cur=cur.next
        cur2.next=None
        cur1.next=l2.next
        return l1.next