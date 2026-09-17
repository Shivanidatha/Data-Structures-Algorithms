# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists or len(lists)==0:
            return None
        def merge(node1,node2):
            dummy=ListNode()
            tail=dummy
            while node1 and node2:
                if node1.val <node2.val:
                    dummy.next=node1
                    node1=node1.next
                else:
                    dummy.next=node2
                    node2=node2.next
                dummy=dummy.next
            if node1:
                dummy.next=node1
            elif node2:
                dummy.next=node2
            return tail.next
        i=0
        while len(lists)>1 and i+1< len(lists):
            l1=lists[i] if lists[i] else None
            l2=lists[i+1] if lists[i+1] else None
            
            lists.append(merge(l1,l2))
            i+=2

        return lists[-1]