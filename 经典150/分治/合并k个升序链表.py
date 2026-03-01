# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None
        def mergeDivde(left,right):
            if left>=right:
                return lists[left]
            mid=(left+right)//2
            left=mergeDivde(left,mid)
            right=mergeDivde(mid+1,right)
            return self.mergeTwoLists(left,right)
        return mergeDivde(0,len(lists)-1)

            

    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy=ListNode()
        cur=dummy
        while list1 and list2:
            if list1.val<=list2.val:
                cur.next=list1
                list1=list1.next
            else:
                cur.next=list2
                list2=list2.next
            cur=cur.next
        cur.next=list1 if list1 else list2
        return dummy.next