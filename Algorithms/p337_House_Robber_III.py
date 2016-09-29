# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def rob(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        res = self.robHelper(root)
        return max(res)
    
    def robHelper(self, root):
        """
        :rtype: tuple
            [0]: max when root not robbed
            [1]: max when root robbed
        """
        if root:
            left =  self.robHelper(root.left) if root.left else (0,0)
            right = self.robHelper(root.right) if root.right else (0,0)
            return (max(left[0],left[1])+max(right[0],right[1]),root.val+left[0]+right[0])
        else:
            return (0,0)
