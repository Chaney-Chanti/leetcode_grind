# # Definition for singly-linked list.
# # class ListNode:
# #     def __init__(self, val=0, next=None):
# #         self.val = val
# #         self.next = next
# class Solution:
#     def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
#         # Basically because the numbers are in reverse order, as I traverse it, I can keep track of 
#         # 10's place I'm evaluating. For example the first node is 0-9, then the 2nd node is 10-99,
#         # then the 3rd nwode is 100-999 and so on and so forth.
#         # sum1 = 0
#         # sum2 = 0
#         # i = l1
#         # j = l2
#         # pos = 0
#         # while i is not None or j is not None:
#         #     if i is not None:
#         #         if pos > 0:
#         #             val = i.val * (pos*10) 
#         #         else:
#         #             val = i.val
#         #         sum1 += val
#         #         i = i.next
#         #     if j is not None:
#         #         if pos > 0:
#         #             val = j.val * (pos*10)
#         #         else:
#         #             val = j.val
#         #         sum2 += val
#         #         j = j.next

#         # sum = sum1 + sum2
#         # digits = list(map(int, str(sum)))
#         # return digits
            

#         sum = 0
#         i = l1
#         j = l2
#         head = 
#         carry = 0
#         while i.next is not None and j.next is not None:
#             val = i.val + j.val
#             if carry == 1:
#                 val += 1
#                 carry = 0

#             if val >= 10:
#                 val = val - 10
#                 carry = 1

#             node = ListNode(val)
#             node.next = node
#             if i.next:
#                 i = i.next
#             if j.next:
#                 j = j.next
        
#         return output


# Clarifying questions to ask:
# How long can the linked list be?
# Do I have negative numbers? Or is it just positive numbers?
# There aren't any loops right?
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        curr = dummy
        carry = 0

        while l1 is not None or l2 is not None or carry:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0

            total = val1 + val2 + carry
            carry = total // 10 # calculate the carry
            digit = total % 10 # calculate the leftover number, reduce if over 10

            curr.next = ListNode(digit)
            curr = curr.next

            if l1: l1 = l1.next
            if l2: l2 = l2.next

        return dummy.next
