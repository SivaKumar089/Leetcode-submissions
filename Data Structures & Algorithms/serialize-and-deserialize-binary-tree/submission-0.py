# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        if not root:
            return ""

        queue = deque([root])
        res = []
        while queue:
            node = queue.popleft()

            if not node:
                res.append('#')
                continue
            
            res.append(str(node.val))
            queue.append(node.left)
            queue.append(node.right)
        return ','.join(res)
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:

        if data == "":
            return None
        
        values = data.split(',')
        root = TreeNode(int(values[0]))
        queue = deque([root])

        i = 1

        while queue:

            node = queue.popleft()

            if values[i] != '#':
                node.left = TreeNode(int(values[i]))
                queue.append(node.left)
            i +=1
            if values[i] != '#':
                node.right = TreeNode(int(values[i]))
                queue.append(node.right)
            i +=1
        return root

