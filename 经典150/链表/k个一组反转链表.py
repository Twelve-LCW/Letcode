# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy=ListNode(next=head)
        if not head or k<=1:
            return head
        n=0
        cur=head

        while cur:
            n+=1
            cur=cur.next
        pre=None
        cur=head
        pre_tail=dummy
        while n>=k:
            n-=k
            for _ in range(k):
                nc=cur.next
                cur.next=pre
                pre=cur
                cur=nc
            cur_tail=pre_tail.next
            cur_tail.next=cur
            pre_tail.next=pre
            pre_tail=cur_tail
        return dummy.next
        
