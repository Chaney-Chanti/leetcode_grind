# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow, fast = head, head

        # Yes handle these edge case
        if head == None or not head.next:
            return None

        while fast and fast.next: # need both because the 
            slow = slow.next
            fast = fast.next.next
            # This algorithm doesn't guarantee that
            # The slow fast pointer always ends on the 
            # node that starts the cycle
            if slow == fast: # detected a cycle? Now what
                break
        else: return None
        slow = head

        # The mathematical explaination is that because the fast pointer is moving twice as fast, 
        while slow != fast:
            slow = slow.next
            fast = fast.next

        return slow
