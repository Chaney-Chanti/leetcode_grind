# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# At first glance, I have no idea how to solve this problem
# I want to retranslate what (n-1-ith) node means. It basically means the first and last node are a pair, the second to last and the second node are also a pair, and so on and so forth. 
# The two immediate problems I see, are that I don't know how big the linked list is, or can move back and forth from the linkedlist during traversal. This is very much unlike an array. 
# Now I'm thinking, that knowing that the linked list always being even means something.

# Ok couldn't think of a solution, so took a look at the hints. The solution given was to reverse the second half of the linked list. That makes sense. I think I was trying to hard to try and solve it in a single pass through.
# The problem now, is how to reverse the second half of the linked list since I don't know the length. I'd probably have to do a tortoise and hare thing 

class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        slow_node = head
        fast_node = head.next

        # Figure out the middle of the list
        while fast_node and fast_node.next:
            slow_node = slow_node.next
            fast_node = fast_node.next.next

        # slow_node should be at the half mark. Now reverse the second half. This part probably builds off the reverse a linked list question
        curr = slow_node.next
        slow_node.next = None
        prev = None

        while curr:
            next_node = curr.next   # save next
            curr.next = prev        # reverse pointer
            prev = curr             # move prev forward
            curr = next_node        # move curr forward

        max_sum = 0
        node_1 = head
        node_2 = fast_node
        while node_1 and node_2:
            # print("first: ", node_1.val, "second:", node_2.val)
            # print("What is this: ",  node_1.val + node_2.val)
            max_sum = max(max_sum, node_1.val + node_2.val)
            node_1 = node_1.next
            node_2 = node_2.next

        return max_sum


# Canonical/Cleaner Solution

class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        # 1. Find middle
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # 2. Reverse second half
        prev = None
        curr = slow

        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt

        # 3. Compute twin sums
        max_sum = 0
        left = head
        right = prev

        while right:   # only need to traverse half
            max_sum = max(max_sum, left.val + right.val)
            left = left.next
            right = right.next

        return max_sum

