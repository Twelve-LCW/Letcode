# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or head.next is None:
            return head
        dummy=ListNode(next=head)
        pre=dummy
        while pre.next:
            first=pre.next
            second=pre.next.next
            if not second:
                break
            first.next=second.next
            second.next=first
            pre.next=second
            pre=first
        return dummy.next