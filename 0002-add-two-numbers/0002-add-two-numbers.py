# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        res_list = ListNode(0)
        tail = res_list
        carry = 0

        while l1 != None or l2 != None or carry != 0:
            digit1 = l1.val if l1 != None else 0
            digit2 = l2.val if l2 != None else 0

            sum = digit1 + digit2 + carry
            digit = sum % 10
            carry = sum // 10

            newNode = ListNode(digit)
            tail.next = newNode
            tail = tail.next
            
            l1 = l1.next if l1 != None else None
            l2 = l2.next if l2 != None else None

        result = res_list.next
        res_list.next = None
        return result

