# # Definition for a binary tree node.
# # class TreeNode:
# #     def __init__(self, val=0, left=None, right=None):
# #         self.val = val
# #         self.left = left
# #         self.right = right

# # This problem seems actually ok to solve. So yea, use depth first search, and keep track of the max during traversal. If the node I'm visiting is greater than the max then it's a good node. No need to keep track of all the nodes because if
# # the max is n, then surely every node passed is smaller than that max.
# class Solution:
#     def goodNodes(self, root: TreeNode) -> int:
#         def dfs(node, max_seen, count):
#             if not node:
#                 return

#             if not node.left and not node.right:
#                 leaves.append(node.val)
#                 return
            
#             if node.val > max_seen:
#                 count += 1

#             dfs(node.left)
#             dfs(node.right)

#         max_seen, count = 0, 0
#         dfs(root, max_seen, count)
#         return count 

# ==============================================================================================================
# Canonical/Cleaner solution
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(node, max_seen):
            if not node:
                return 0

            # Check if this node is "good"
            good = 1 if node.val >= max_seen else 0

            # Update max for THIS path only
            new_max = max(max_seen, node.val)

            # Count from left and right subtrees
            return (
                good
                + dfs(node.left, new_max)
                + dfs(node.right, new_max)
            )

        return dfs(root, root.val)
