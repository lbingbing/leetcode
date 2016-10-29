# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        res = [0]
        if root:
            self.sumNumbersHelper(res,root,0)
        return res[0]

    def sumNumbersHelper(self, res, root, n):
        n1 = n*10+root.val
        if not root.left and not root.right:
            res[0] += n1
        if root.left:
            self.sumNumbersHelper(res,root.left,n1)
        if root.right:
            self.sumNumbersHelper(res,root.right,n1)
