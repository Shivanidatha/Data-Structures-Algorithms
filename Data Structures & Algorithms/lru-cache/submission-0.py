class Node:
    def __init__(self, key, val):
        self.key,self.val= key,val
        self.prev,self.next= None, None


class LRUCache:


    def __init__(self, capacity: int):
        self.hm={}
        self.capacity=capacity
        self.left=self.right=Node(0,0)
        self.left.next=self.right
        self.right.prev=self.left

    def remove(self, node):
        node.prev.next=node.next
        node.next.prev=node.prev
    
    def insert(self, node):
        node.next=self.right
        node.prev=self.right.prev
        self.right.prev.next=node
        self.right.prev=node

    def get(self, key: int) -> int:
        if key in self.hm:
            self.remove(self.hm[key])
            self.insert(self.hm[key])
            return self.hm[key].val
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.hm:
            self.remove(self.hm[key])
        self.hm[key]=Node(key,value)
        self.insert(self.hm[key])
        if len(self.hm)>self.capacity:
            lru=self.left.next
            self.remove(lru)
            self.hm.pop(lru.key)
            
