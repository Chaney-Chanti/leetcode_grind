# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        queue = deque([root])
        depth = 0

        while queue:
            level_size = len(queue)   # number of nodes at this level

            for _ in range(level_size):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            depth += 1   # finished one full level

        return depth

################## Recursive Solution #####################

# Definition for a binary tree node.
class TreeNode(object):
    def init(self, val=0, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right
    class Solution(object):
        def maxDepth(self, root):
            def dfs(node):
                if not node:
                    return 0
                left_depth = dfs(node.left)
                right_depth = dfs(node.right)
                return max(left_depth, right_depth) + 1
