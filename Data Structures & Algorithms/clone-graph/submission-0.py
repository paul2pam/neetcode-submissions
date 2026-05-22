"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if node is None:
            return None
        m = {}

        def dfs(node):
            if node in m:
                return
            m[node] = Node(node.val) 
            for neighbor in node.neighbors:
                dfs(neighbor)
                m[node].neighbors.append(m[neighbor])

        dfs(node)

        return m[node]