# This doesn't seem that bad. I basically have to run the depth first search algorithm and keep track of the longest one? But then I also
# have to verify if it zig zags? Ok Doesn't seem that easy anymore...
# Well had to use claude to tutor me for this.. Man these DFS questions are tough....
class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        self.longest_zig_zag = 0
        def dfs(node, curr_zig_zag_len, dir):
            if not node:
                return
            self.longest_zig_zag = max(curr_zig_zag_len, self.longest_zig_zag)
            if dir == "none":
                dfs(node.left,  curr_zig_zag_len + 1, "left")
                dfs(node.right, curr_zig_zag_len + 1, "right")
            elif dir == "left":
                dfs(node.left, 1, "left")
                dfs(node.right, curr_zig_zag_len + 1, "right")
            elif dir == "right":
                dfs(node.left, curr_zig_zag_len + 1, "left")
                dfs(node.right, 1, "right")
        dfs(root, 0, "none")
        return self.longest_zig_zag
