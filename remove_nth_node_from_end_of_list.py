# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# This problem is slightly different from removing the middle node. The tactic for removing a middle node is to use tortoise and hare to find the middle. Use one that parses twice as fast. But here, n may not be the middle and its from the end of the list....

# clarification question i can ask if if n is always less or equal to the size of the list.
# because if thats the case then of a list of 2, n can be at most 2. So Now I'm thinking along the lines
# of something like advancing a pointer n fast. 
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # Edge case: single node
        if not head or not head.next:
            return None

        slow = head
        fast = head
        prev = None

        # First advance the fast pointer n times
        # This is so we can keep the distance between them
        # at n length
        for i in range(n):
            fast = fast.next

        # Keep the distance between the two pointers at n length
        while fast: # note never is true if n is == to size of list.
            prev = slow
            slow = slow.next
            fast = fast.next

        # Need to adjust for the edge case of if n is the size of the list because prev never gets assigned
        if prev == None:
            head = slow.next
        else:
            # Once we reach the end of the list. Slow pointer should now be 
            # at the node that we want to remove. Lets reassign
            prev.next = slow.next

        return head
        
