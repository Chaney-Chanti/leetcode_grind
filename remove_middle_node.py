# # Definition for singly-linked list.
# # class ListNode:
# #     def __init__(self, val=0, next=None):
# #         self.val = val
# #         self.next = next

# # Original thought is to, find the length of the list (via a traversal) and then writing the logic to
# # remove the node. However this requires a double traversal which seems inefficient.

# # So now I need to think of a way to traverse a single time. I've seen strategies of a tortoise and hare
# # so maybe its something along the lines of if the hare ever becomes null moving at twice the speed, then
# # whatever the tortoise is at, denotes the middle node.

# # Ok I worked out the tortoise and the hare solution and it seems to work except that the tortoise is the middle, but in order to write the logic
# # to delete itself, I need the node before the tortoise to set it's next to the node after the tortoise... Seems complicated to keep track of 3 Nodes? 
# # also seems kinda hacky to write the logic of the lagging node.

# class Solution:
#     def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
#         tortoise = ListNode()
#         hare = ListNode()
#         lag = ListNode() # lags 1 node behind the tortoise
#         tortoise, hare, lag = head, head, head
#         if head.next == None:
#             return None

#         while hare:
#             if hare.next == None:
#                 break
#             if tortoise != head:
#                 lag = lag.next
#             tortoise = tortoise.next
#             hare = hare.next.next
    
#         # logic to remove the tortoise
#         lag.next = tortoise.next
#         return head

    # ========================================================================================================================================================
    # Seems like I had the right idea of using a fast and slow pointer, here's the clean canonical way

    class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Edge case: single node
        if not head or not head.next:
            return None

        slow = head
        fast = head
        prev = None # Ah, this feels like a much better way to track the prev instead of what I did.

        while fast and fast.next: # Ah, this is also a better way to do what I did. I'm so troll
            prev = slow
            slow = slow.next
            fast = fast.next.next

        # slow is the middle node
        prev.next = slow.next
        return head
