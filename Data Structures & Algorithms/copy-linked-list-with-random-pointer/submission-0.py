"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        hm={None: None}
        cur=head
        while cur:
            copy=Node(cur.val)
            hm[cur]=copy
            cur=cur.next
        curr=head
        while curr:
            copy=hm[curr]
            copy.next=hm[curr.next]
            copy.random=hm[curr.random]
            curr=curr.next
        return hm[head]


