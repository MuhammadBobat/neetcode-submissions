# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        head = dummy
        carry = 0
        
        while l1 and l2:
            value = l1.val + l2.val + carry
            if value >= 10:
                mod = value % 10
                head.next = ListNode(val=mod)
                carry = value // 10
            else:
                head.next = ListNode(val=value)
                carry = 0
            
            head = head.next

            l1 = l1.next
            l2 = l2.next
        
        while l1:
            value = l1.val + carry
            if value >= 10:
                mod = value % 10
                head.next = ListNode(val=mod)
                carry = value // 10
            else:
                head.next = ListNode(val=value)
                carry = 0

            head = head.next
            l1 = l1.next

        while l2:
            value = l2.val + carry
            if value >= 10:
                mod = value % 10
                head.next = ListNode(val=mod)
                carry = value // 10
            else:
                head.next = ListNode(val=value)
                carry = 0

            head = head.next
            l2 = l2.next
        
        if carry:
            head.next = ListNode(val=carry)
            head = head.next
            head = head.next
        
        return dummy.next