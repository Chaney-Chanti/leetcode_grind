# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# This is probably an extension of the previous question of searching for a target node. Seems pretty confusing, so figured I'd just memorize the solution

# class Solution:
#     def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
#         parent = None 
#         node = root
#         while node:
#             if node.val == key:
#                 break
#             parent = node
#             if node.val > key:
#                 node = node.left
#             elif node.val < key:
#                 node = node.right
            
#         if not node
#             return root

#         if node == parent.left:
#             direc = "left"
#         else:
#             direc = "right"

#         if direc == left and node.left == None and node.right == None:
#             parent.left = None
#         elif direc = right node.left == None and node.right == None:
#             parent.right = None
#         elif node.left != None or node.right != None:
#             parent = node
#         elif node.left and node.right:
#             # do somethin
                
#         return root

# Canonical Solution

class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        parent = None
        node = root
        
        while node:
            if node.val == key:
                break
            parent = node
            if node.val > key:
                node = node.left
            elif node.val < key:
                node = node.right
        
        if not node:
            return root

        # Find replacement
        if node.left and node.right:
            temp = node.right
            while temp.left:
                temp = temp.left
            temp.left = node.left
            replacement = node.right
        elif node.left:
            replacement = node.left
        elif node.right:
            replacement = node.right
        else:
            replacement = None
        
        # Apply replacement
        if not parent:
            return replacement
        if node == parent.left:
            parent.left = replacement
        else:
            parent.right = replacement
        
        return root
