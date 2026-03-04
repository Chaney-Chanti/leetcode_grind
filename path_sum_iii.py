# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# This felt impossible, had to utilize chatgbt in a hinty format.
# Basically make a hashmap, and keep track of all the node's values. Then as im traversing a path, keep track of the running sum. Then subtract that running sum from the targetSum. Whatever that comes out too, find how many times that occurs in the hashmap, and add to the counter.
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        # prefix_sum -> number of times it appears on the current path
        prefix = defaultdict(int)
        prefix[0] = 1  # allows paths that start at the root

        def dfs(node, curr_sum):
            if not node:
                return 0

            # Update running sum
            curr_sum += node.val

            # Count paths ending at this node
            count = prefix[curr_sum - targetSum]

            # Record this running sum
            prefix[curr_sum] += 1

            # Recurse
            count += dfs(node.left, curr_sum)
            count += dfs(node.right, curr_sum)

            # Backtrack (remove this node's contribution)
            prefix[curr_sum] -= 1

            return count

        return dfs(root, 0)
