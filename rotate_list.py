# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # The first initial thought, is to do a single rotation, then just repeat that k times. But that 
        # could potentially be very slow, and maybe theres a quick way to do it.

        # Also thought maybe I can create a list thats properly ordered, then create a linked list from it
        # But that doesn't utilize two pointers, so surely this is wrong

        # observation, maybe it has something to do with the relationship between k and the distance between each node. Like on a list of 1-5, the difference between 1 and 5 is always 4. 
        # another thought that stemmed from the above observation is that I just need to re route three nodes. The new start, end, and new middle node

         # The new start of the chain is k nodes from the end of the list. Proabably another tortoise and hare question?
        if k == 0 or not head: return head

        # Get the length and tail node
        length = 1
        tail = head
        while tail.next:
            tail = tail.next
            length += 1

        # If k is a multiple of length, no rotation needed
        k = k % length
        if k == 0: return head

        slow, fast = head, head

        # Get fast to be k nodes ahead of slow
        for _ in range(k):
            fast = fast.next

        # Find where the new start and end are
        while fast.next != None:
            slow = slow.next
            fast = fast.next

        # The node that comes after slow becomes the new head
        new_head = slow.next
        # Fast goes before the head
        fast.next = head
        # Slow becomes the new end
        slow.next = None
