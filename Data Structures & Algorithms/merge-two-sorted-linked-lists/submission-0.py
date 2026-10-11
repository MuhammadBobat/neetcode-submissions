# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        numbers = []
        current1 = list1
        current2 = list2

        while current1 and current2:
            if current1.val < current2.val:
                numbers.append(current1.val)
                current1 = current1.next
            else:
                numbers.append(current2.val)
                current2 = current2.next

        while current1:
            numbers.append(current1.val)
            current1 = current1.next
        
        while current2:
            numbers.append(current2.val)
            current2 = current2.next

        head = None
        current = None

        for num in numbers:
            new_node = ListNode(num)
            
            if head is None:
                head = new_node
            else:
                current.next = new_node

            current = new_node
        
        return head