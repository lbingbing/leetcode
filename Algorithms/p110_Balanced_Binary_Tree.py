# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return self.isBalancedHelper(root)!=-1

    def isBalancedHelper(self, root):
        if not root:
            return 0
        height_l = self.isBalancedHelper(root.left)
        if height_l==-1:
            return -1
        height_r = self.isBalancedHelper(root.right)
        if height_r==-1:
            return -1
        large = max(height_l,height_r)
        small = min(height_l,height_r)
        return large+1 if large-small<=1 else -1
