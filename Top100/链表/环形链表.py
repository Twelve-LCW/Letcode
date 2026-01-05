# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        a=head
        b=head
        while b and b.next:
            a=a.next
            b=b.next.next
            if a==b:
                return True
        return False
    

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head is None or head.next is None or head.next.next is None:
            return False
        a=head
        b=head.next
        while a is not None and b is not None:
            if a==b:
                return True
            if a is None or b is None:
                return False
            if a.next is None or b.next is None:
                return False
            a=a.next
            b=b.next.next
        return False