# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        res = 0
        dp = {}

        def dfs(node):
            if node is None:
                return 0
            if node in dp:
                return dp[node]
            dp[node] = 1 + max(dfs(node.left), dfs(node.right))
            return dp[node]

        def diameter(node):
            nonlocal res
            if node is None:
                return
            res = max(res, dfs(node.right) + dfs(node.left))
            diameter(node.left)
            diameter(node.right)
        
        diameter(root)
        return res