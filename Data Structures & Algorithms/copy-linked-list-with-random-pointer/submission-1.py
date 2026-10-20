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
        dummy = Node(x=0)
        new = dummy
        pairs = {}

        current = head
        while current:
            new.next = Node(x=int(current.val))
            pairs[current] = new.next
            new = new.next
            current = current.next
        
        current = head
        while current:
            node = pairs[current]
            if current.random is None:
                node.random = None
            else:
                node.random = pairs[current.random]

            current = current.next

        return dummy.next

        