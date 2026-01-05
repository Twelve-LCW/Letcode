# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    # def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
    #     if not head or k<=1:
    #         return head
        
    #     cnt=0
    #     cur=head
    #     while cur and cnt<k:
    #         cur=cur.next
    #         cnt+=1
    #     if cnt==k:
    #         reserved_head=self.reserve(head,k)

    #         head.next=self.reverseKGroup(cur,k)
    #         return reserved_head
        
    #     return head
        
    

    # def reserve(self,head,k):
    #     pre=None
    #     cur=head
    #     while k>0:
    #         tmp=cur.next
    #         cur.next=pre
    #         pre=cur
    #         cur=tmp
    #         k-=1
    #     return pre
    

        def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
            if not head or k<=1:
                return head
            

            n,cur=0,head
            while cur:
                 n+=1
                 cur=cur.next

            pre_tail=dummy=ListNode(next=head)
            pre=None
            cur=head
            while n>=k:
                n-=k
                for _ in range(k):
                    tmp=cur.next
                    cur.next=pre
                    pre=cur
                    cur=tmp
                cur_tail=pre_tail.next
                cur_tail.next=cur
                pre_tail.next=pre
                pre_tail=cur_tail
            return dummy.next
                