# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        dummy=ListNode(0)
        dummy.next=head
        pre=dummy
        while pre.next:
            first=pre.next
            second=pre.next.next
            if not second:
                break
            first.next=second.next
            pre.next=second
            second.next=first
            pre=pre.next.next
        return dummy.next
