# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        # Upon initially reading, I feel confused by: Given the head of a linked list and a value x, 
        # partition it such that all nodes less than x come before nodes greater than or equal to x. 
        # Because based on the example 1,4,3,2,5,2 -> 1,2,2,4,3,5 there seems to be multiple answers to the input, like 
        # 1,2,2,4,5,3 seems like it follows the rule. 
        # Actually I trolled because it says that it needs to maintain the original relative order.

        parser = head
        lesser_head, lesser_tail, greater_head, greater_tail  = None, None, None, None
        while parser != None:
            # print("parser: ", parser.val)
            if parser.val < x: 
                if lesser_head == None:
                    lesser_head = parser
                    lesser_tail = parser
                else:
                    lesser_tail.next = parser
                    lesser_tail = lesser_tail.next
            elif parser.val >= x:
                if greater_head == None:
                    greater_head = parser
                    greater_tail = parser
                else:
                    greater_tail.next = parser
                    greater_tail = greater_tail.next
            parser = parser.next

        if greater_tail:
            greater_tail.next = None
        if not greater_head:
            return lesser_head
        elif not lesser_head:
            return greater_head
        else:
            lesser_tail.next = greater_head

        return lesser_head
        
# Canonical solution

class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        lesser_dummy = ListNode(0)
        greater_dummy = ListNode(0)
        lesser_tail = lesser_dummy
        greater_tail = greater_dummy

        parser = head
        while parser:
            if parser.val < x:
                lesser_tail.next = parser
                lesser_tail = lesser_tail.next
            else:
                greater_tail.next = parser
                greater_tail = greater_tail.next
            parser = parser.next

        greater_tail.next = None
        lesser_tail.next = greater_dummy.next
        return lesser_dummy.next
 
        
