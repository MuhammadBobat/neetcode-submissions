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
        current = head
        dummy = Node(0)
        new = dummy
        nodes = {}
        
        while current:
            new.next = Node(current.val)
            new = new.next
            #Stores relationship between originals and copies
            nodes[current] = new

            current = current.next
            
           
        current = head
        while current:
            if current.next is None:
                nodes[current].next = None
            else:
                nodes[current].next = nodes[current.next]
            if current.random is None:
                nodes[current].random = None
            else:
                nodes[current].random = nodes[current.random]
        
            current = current.next
    
        return dummy.next
