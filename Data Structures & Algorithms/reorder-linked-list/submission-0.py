# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow=head
        fast=head
        #finding middle node
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        
        #reversing from middle to end
        curr=slow.next
        slow.next=None
        prev=None
        while curr:
            nxt=curr.next
            curr.next=prev
            prev=curr
            curr=nxt
        #merging prev and slow
        first=head
        second=prev
        while second:
            tmp1, tmp2= first.next, second.next
            first.next=second
            second.next=tmp1
            first=tmp1
            second=tmp2
        




