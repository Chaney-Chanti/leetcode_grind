# # Definition for singly-linked list.
# # class ListNode:
# #     def __init__(self, val=0, next=None):
# #         self.val = val
# #         self.next = next

# # example:
# # node -> node -> node -> node
# class Solution:
#     def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
#         if head.next == None:
#             return head
    
#         new_start, even_node = head.next, head.next
#         odd_node = head
#         while even_node or odd_node:
#             if odd_node.next.next:
#                 odd_node.next = odd_node.next.next
#                 odd_node = odd_node.next.next
#             if even_node.next.next:
#                 even_node.next = even_node.next.next
#                 even_node = even_node.next.next
#             else:
#                 even_node.next = None

#         odd_node.next = new_start
#         return head

# I basically had the solution, I just couldn't implement my idea properly
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        odd = head
        even = head.next
        even_head = even  # save start of even list

        while even and even.next: # Can just do even because its always ahead of odd. Which means if even next exists, then so does odd.next
            odd.next = even.next
            odd = odd.next

            even.next = odd.next
            even = even.next

        odd.next = even_head
        return head
