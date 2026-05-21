# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def dfs(self, root: TreeNode, p: TreeNode, q: TreeNode):
        if not root:
            return False

        if root.val == p.val or root.val == q.val:
            return True
        
        l = r = False
        if root.left:
            l = self.dfs(root.left, p, q)
        if root.right:
            r = self.dfs(root.right, p, q)
        return l or r

    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:

        best = root

        d = deque()
        d.append(root)

        while (d):
            curr = d.popleft()
            if curr.val == p.val or curr.val == q.val:
                return curr

            l = self.dfs(curr.left, p, q)
            r = self.dfs(curr.right, p, q)
            print(curr.val, l, r)
            if l and r:
                return curr
            
            if curr.left and l:
                d.append(curr.left)
            if curr.right and r:
                d.append(curr.right)
            
        return best
        