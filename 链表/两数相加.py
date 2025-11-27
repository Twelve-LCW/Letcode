# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        pre=ListNode(0)
        cur=pre
        a,b=l1,l2
        tmp=0
        while a or b:
            num1=a.val if a else 0
            num2=b.val if b else 0
            sum=num1+num2+tmp
            tmp=0
            if sum>=10:
                tmp=1
                num=sum-10
            else:
                num=sum
            cur.next=ListNode(num)
            cur=cur.next
            if a is not None:
                a=a.next
            if b is not None:
                b=b.next
        if tmp==1:
            cur.next=ListNode(tmp)
        return pre.next