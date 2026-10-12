# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.bst(root, float('-inf'), float('inf'))

    
    def bst(self, root, lower, upper):
        if not root:
            return True
        
        if root.val <= lower or root.val >= upper:
            return False
        
        left = self.bst(root.left, lower, root.val)
        right = self.bst(root.right, root.val, upper)
    

        return left and right

            