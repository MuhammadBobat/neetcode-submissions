# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # Sever link between 2 half lists
        current = slow.next
        slow.next = None

        #slow points at the middle
        prev = None
        while current:
            tmp = current.next
            current.next = prev
            prev = current
            current = tmp
        
        second = prev
        first = head
        while first and second:
            tmp1, tmp2 = first.next, second.next
            first.next = second
            second.next = tmp1
            first = tmp1
            second = tmp2
        