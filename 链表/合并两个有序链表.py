# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        a,b=list1,list2
        head=ListNode(0)
        cur=head
        while a and b:
            if a.val<=b.val:
                cur.next=a
                a=a.next
            elif a.val>b.val:
                cur.next=b
                b=b.next
            cur=cur.next
        cur.next=a if a else b
        return head.next

