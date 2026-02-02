# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        a=head
        b=head
        while b and b.next: ## 确保快指针一次能走两步
            a=a.next
            b=b.next.next
            if a==b:   ## 两者相遇，说明链表存在环; 但相遇的地方不一定就是链表出现环的入口
                return True
        return False