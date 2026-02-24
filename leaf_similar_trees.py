# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# This doesn't seem to bad. A leaf is just defined as having no children, so if I
# can maintain two lists and comapre them at the end for equality, them I'm good.
# problem is how to create a list using a recursive solution.
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        def dfs(node, leaves):
            if not node:
                return

            if not node.left and not node.right:
                leaves.append(node.val)
                return

            dfs(node.left, leaves)
            dfs(node.right, leaves)

        leaves1 = []
        leaves2 = []

        # leaves gets passed by object-reference. Which means that through all the recursive calls. The same leaves(x) list is modified rather than having copies made.
        dfs(root1, leaves1)
        dfs(root2, leaves2)

        return leaves1 == leaves2
      
