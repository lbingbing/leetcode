# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return bool(not root or self.isSymmetricHelper(root.left,root.right))
        
    def isSymmetricHelper(self, t1, t2):
        return bool((not t1 and not t2) or (t1 and t2 and t1.val==t2.val and self.isSymmetricHelper(t1.left,t2.right) and self.isSymmetricHelper(t1.right,t2.left)))
