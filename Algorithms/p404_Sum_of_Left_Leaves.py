# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        res = 0
        if root:
            if root.left:
                res += root.left.val if (not root.left.left and not root.left.right) else self.sumOfLeftLeaves(root.left)
            if root.right:
                res += self.sumOfLeftLeaves(root.right)
        return res
