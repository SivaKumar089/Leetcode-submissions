# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    def __init__(self):
        self.res = 0
        self.count = 1

    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.inorder(root, k)
        return self.res
    
    def inorder(self, root, k):
        if not root or self.count > k:
            return 

        self.inorder(root.left, k)
        if self.count == k:
            self.res = root.val
        self.count +=1
        self.inorder(root.right, k)