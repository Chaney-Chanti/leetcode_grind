# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# It wasn't too bad, I just thought the solution didn't involve using an array/list
# to get around the singly linked list restriction of being able to parse a linked list
# backwards.

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if head == None or head.next == None:
            return

        node = head
        reorder = []
        # generate list mimicing ll
        while node != None:
            reorder.append(node)
            node = node.next

        i = 0
        j = len(reorder) - 1

        node = head
        while i < j:
            reorder[i].next = reorder[j]
            i += 1
            reorder[j].next = reorder[i]
            j -= 1

        reorder[i].next = None
    
