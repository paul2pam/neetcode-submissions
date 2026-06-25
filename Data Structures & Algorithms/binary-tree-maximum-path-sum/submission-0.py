# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        dp = {}
        res = -float("INF")

        def helper(root):
            if root is None:
                return 0
            if root in dp: 
                return dp[root]
            
            l = helper(root.left)
            r = helper(root.right)

            dp[root] = max(root.val + l, root.val + r, root.val)
            return dp[root]

        s = []
        s.append(root)

        while s:
            l = helper(s[0].left)
            r = helper(s[0].right)
            print(s[0].val, l, r)
            res = max(s[0].val + l + r, s[0].val + l, s[0].val + r, s[0].val, res)
        
            if s[0].left:
                s.append(s[0].left)
            if s[0].right:
                s.append(s[0].right)

            s = s[1:]

        return res
        