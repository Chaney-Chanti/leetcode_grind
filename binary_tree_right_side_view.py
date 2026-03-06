# This one should have been easy, but I had trouble trying to understand the code, specifically the for loop part... Had to use claude to help me again.
from collections import deque
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        output = []
        if not root:
            return output
        
        queue = deque([root])
        node = None
        while queue:
            # You need this for loop to group nodes by level....
            for _ in range(len(queue)):
                node = queue.popleft()       
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)             
            output.append(node.val)
        return output
