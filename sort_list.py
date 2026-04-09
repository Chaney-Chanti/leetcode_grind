# # Definition for singly-linked list.
# # class ListNode:
# #     def __init__(self, val=0, next=None):
# #         self.val = val
# #         self.next = next
# class Solution:
#     def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:

#         def merge(l1, l2):
#             dummy = ListNode(0)
#             current = dummy
            
#             while l1 and l2:
#                 if l1.val <= l2.val:
#                     current.next = l1
#                     l1 = l1.next
#                 else:
#                     current.next = l2
#                     l2 = l2.next
#                 current = current.next
            
#             # if one list still has nodes left...
#             current.next = l1 or l2
            
#             return dummy.next
                
#         if head == None or head.next == None:
#             return head

#         slow, fast = head, head
#         while fast != None and fast.next != None:
#             slow = slow.next
#             fast = fast.next.next

#         mid = slow
#         right = mid.next
#         mid.next = None
#         left = self.sortList(head)
#         right = self.sortList(right)

#         return merge(left, right)


class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        def merge(l1, l2):
            dummy = ListNode(0)
            current = dummy
            
            while l1 and l2:
                if l1.val <= l2.val:
                    current.next = l1
                    l1 = l1.next
                else:
                    current.next = l2
                    l2 = l2.next
                current = current.next
            
            current.next = l1 or l2
            return dummy.next
        
        if not head or not head.next:
            return head

        slow, fast = head, head.next  # fast starts at head.next!
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        mid = slow.next  # mid is one ahead of slow
        slow.next = None
        left = self.sortList(head)
        right = self.sortList(mid)

        return merge(left, right)
        
