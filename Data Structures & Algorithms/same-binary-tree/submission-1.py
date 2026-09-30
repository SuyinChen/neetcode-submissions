# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # if both p and q are null return true
        if not p and not q:
            return True
        # if only one is null, return false
        elif not p or not q:
            return False
        #check values, if not equal return false
        elif p.val != q.val:
            return False
        #recursively compare the rest
        return self.isSameTree(p.right, q.right) and self.isSameTree(p.left, q.left)