# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        output = []
        if not root:
            return output
        
        queue = deque([root])
        node = None
        max_level, curr_level = 1, 1
        max_sum = float('-inf')
        while queue:
            # You need this for loop to group nodes by level...
            curr_sum = 0
            for _ in range(len(queue)):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                curr_sum += node.val
            if curr_sum > max_sum: # i originally had this as >= which would not be the smallest level 
                max_level = curr_level
            max_sum = max(max_sum, curr_sum) # need to update max after
            curr_level += 1
        return max_level
        
