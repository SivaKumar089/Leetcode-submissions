# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]):
        
        self.max = float('-inf')
        self.height(root)
        return self.max

    def height(self, root):
        if not root:
            return 0

        left = max(0, self.height(root.left))
        right = max(0, self.height(root.right))
        self.max = max(self.max, left + right + root.val)

        return root.val + max(left, right)