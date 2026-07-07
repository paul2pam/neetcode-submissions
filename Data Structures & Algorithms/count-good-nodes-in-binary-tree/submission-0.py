# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        parent = {}

        def add_parents(node):
            if node.left:
                parent[node.left] = node
                add_parents(node.left)
            if node.right:
                parent[node.right] = node
                add_parents(node.right)
        
        add_parents(root)
        parent[root] = None

        def is_good(node):
            max_val = node.val
            while parent[node] != None:
                node = parent[node]
                if node.val > max_val:
                    return False
            return True
        
        def bfs(node):
            if node is None:
                return 0
            if is_good(node):
                return 1 + bfs(node.right) + bfs(node.left)
            else:
                return bfs(node.right) + bfs(node.left)

        return bfs(root)


        
        