# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head

        fast = head
        slow = dummy

        for i in range(n):
            fast = fast.next
        
        while fast:
            slow = slow.next
            fast = fast.next 
        
        #slow now points to the nth from the end 
        if slow.next.next is not None:
            slow.next = slow.next.next
        else:
            slow.next = None
        


        return dummy.next