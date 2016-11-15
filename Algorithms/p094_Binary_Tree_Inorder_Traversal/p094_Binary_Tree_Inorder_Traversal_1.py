# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        l = []
        if root:
            self.inorderTraversalStep(root,l)
        return l
        
    def inorderTraversalStep(self, root, l):
        if root:
            self.inorderTraversalStep(root.left,l)
            l.append(root.val)
            self.inorderTraversalStep(root.right,l)
