# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy=ListNode(next=head)
        second=dummy
        first=head
        while n>0:
            first=first.next
            n-=1
        while first:
            first=first.next
            second=second.next
        second.next=second.next.next
        return dummy.next


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(next=head)
        cur = head
        i = 0
        while cur:
            cur = cur.next
            i += 1
        second = dummy
        i -= n
        while i > 0:
            second = second.next
            i -= 1
        second.next = second.next.next
        return dummy.next
        