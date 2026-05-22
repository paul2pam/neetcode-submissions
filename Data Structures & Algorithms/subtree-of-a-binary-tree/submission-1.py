# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def bfs(Root, subRoot):
            if Root is None and subRoot is None:
                return True
            if Root is None or subRoot is None:
                return False
            if Root.val != subRoot.val:
                return False
            return bfs(Root.left, subRoot.left) and bfs(Root.right, subRoot.right)
                
        if root is None:
            return False
        
        if root.val == subRoot.val:
            if bfs(root, subRoot):
                return True
            

        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)