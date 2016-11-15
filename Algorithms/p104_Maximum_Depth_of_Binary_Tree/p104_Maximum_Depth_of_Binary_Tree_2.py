# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        if not root.left and not root.right:
            return 1
        left_depth = 0
        right_depth = 0
        if root.left:
            left_depth = 1 + self.maxDepth(root.left)
        if root.right:
            right_depth = 1 + self.maxDepth(root.right)
        return left_depth if left_depth > right_depth else right_depth
