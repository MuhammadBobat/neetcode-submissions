# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        current1 = list1
        current2 = list2

        dummy = ListNode()
        current = dummy

        while current1 and current2:
            if current1.val < current2.val:
                current.next = ListNode(current1.val)
                current = current.next
                current1 = current1.next
            else:
                current.next = ListNode(current2.val)
                current = current.next
                current2 = current2.next

        while current1:
            current.next = ListNode(current1.val)
            current = current.next
            current1 = current1.next
        
        while current2:
            current.next = ListNode(current2.val)
            current = current.next
            current2 = current2.next
        
        return dummy.next