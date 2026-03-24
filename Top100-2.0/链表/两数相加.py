# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        a,b=l1,l2
        dummy=ListNode()
        cur=dummy
        carry=0
        while a or b:
            num1=a.val if a else 0
            num2=b.val if b else 0
            num=(carry+num1+num2)%10
            carry=(carry+num1+num2)//10
            cur.next=ListNode(val=num)
            cur=cur.next
            if a:a=a.next
            if b:b=b.next
        if carry>0:
            cur.next=ListNode(val=carry)
        return dummy.next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        cur=dummy=ListNode()
        carry=0
        while l1 or l2 or carry:
            if l1:
                carry+=l1.val
                l1=l1.next
            if l2:
                carry+=l2.val
                l2=l2.next
            cur.next=ListNode(carry%10)
            carry//=10
            cur=cur.next
        return dummy.next

        