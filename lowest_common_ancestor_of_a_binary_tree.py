# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Ok from what I've learned from the past DFS problems is that I need three things
# 1. A base case
# 2. updating the state that i wish to track/return
# 3. recursivley calling dfs

# What do I need to keep track of, what state is maintaned?
    # I think I need a list of all of the nodes ancestors
# I need to return the LCA node
# Aiyah... needed claude to help me all the way DFS problems suck for me and are difficult to grasp the recursive aspect.
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def dfs(node):
            if not node:
                return None
            if node == p or node == q:
                return node
            left = dfs(node.left)
            right = dfs(node.right)
            if left and right:
                return node
            return left or right
        return dfs(root)
