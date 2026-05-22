# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        if not root:
            return []

        d = deque()
        d.append(root)
        level = deque()
        level.append(0)

        prev_level = 0
        l = []
        tr = []
        while d:
            curr = d.popleft()

            curr_level = level.popleft()
            if (curr_level > prev_level):
                tr.append(l)
                l = []
                prev_level = curr_level
            l.append(curr.val)

            
            if curr.left:
                d.append(curr.left)
                level.append(curr_level + 1)
            if curr.right:
                d.append(curr.right)
                level.append(curr_level + 1)
        tr.append(l)
            
        return tr