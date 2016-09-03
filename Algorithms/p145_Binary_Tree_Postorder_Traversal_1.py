# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = []
        self.postorderTraversalStep(root,res)
        return res
        
    def postorderTraversalStep(self, root, l):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root:
            self.postorderTraversalStep(root.left,l)
            self.postorderTraversalStep(root.right,l)
            l.append(root.val)
