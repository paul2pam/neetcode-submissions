# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        stack = []
        stack.append(root)
        res = []

        while(len(stack) > 0):
            curr_len = len(stack)
            for i in range(curr_len):
                if stack[i].left:
                    stack.append(stack[i].left)
                if stack[i].right:
                    stack.append(stack[i].right)
            res.append(stack[curr_len - 1].val)
            stack = stack[curr_len:]
        
        return res
