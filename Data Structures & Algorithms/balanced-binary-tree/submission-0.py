# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        dp = {}
        
        def len(node):
            if node in dp:
                return dp[node]
            if node is None:
                return 0
            dp[node] = 1 + max(len(node.right), len(node.left))
            return dp[node]

        def helper(node):
            if node is None:
                return True
            if abs(len(node.right) - len(node.left)) > 1:
                return False
            return helper(node.left) and helper(node.right)

        return helper(root)