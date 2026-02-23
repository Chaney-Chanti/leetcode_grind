# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# my first thought was to keep track of a set of 3 adjacent nodes and change the order while traversing it.
# my second thought, is to just make a new linked list?
# Ok looked at the solition. i conceptually knew what to do, but translating my thought into clean code is difficult.

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head

        while curr:
            next_node = curr.next   # save next
            curr.next = prev        # reverse pointer
            prev = curr             # move prev forward
            curr = next_node        # move curr forward

        return prev


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Base case: empty list or single node
        if not head or not head.next:
            return head

        # Reverse everything after head
        new_head = self.reverseList(head.next)

        # Fix the current node
        head.next.next = head
        head.next = None

        return new_head


