# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy=ListNode(next=head)
        first=head
        i=0
        while first:
            i+=1
            first=first.next
        i-=n
        second=dummy
        while i>0:
            i-=1
            second=second.next
        second.next=second.next.next
        return dummy.next