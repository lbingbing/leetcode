# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = []
        self.preorderTraversalStep(root,res)
        return res
        
    def preorderTraversalStep(self, root, l):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root:
            l.append(root.val)
            self.preorderTraversalStep(root.left,l)
            self.preorderTraversalStep(root.right,l)
