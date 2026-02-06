# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return head
        cur = head
        n = 0
        while cur:
            n += 1
            if cur.next is None:
                second_tail = cur
            cur = cur.next
        k = k % n
        if k == 0:
            return head
        k = n - k
        cur = head
        while k > 1:
            cur = cur.next
            k -= 1
        first_tail = cur
        new_head = first_tail.next
        first_tail.next = None
        second_tail.next = head
        return new_head