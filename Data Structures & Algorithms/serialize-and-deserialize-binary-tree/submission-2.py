# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        arr = []
        def go(root):
            if root is None:
                arr.append('#')
                return
            arr.append(str(root.val))
            go(root.left)
            go(root.right)
        go(root)
            
        return " ".join(arr)
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        data = data.split()
        print(data)
        def go():
            if data[self.i] == "#":
                return None
            root = TreeNode(data[self.i])
            self.i += 1
            root.left = go()
            self.i += 1
            root.right = go()
            return root
        self.i = 0
        root = go()
        return root
            
