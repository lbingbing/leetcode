# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        return self.kthSmallestStep(root,[k])
        
    def kthSmallestStep(self, node, k_l):
        if node:
            val = self.kthSmallestStep(node.left,k_l)
            if k_l[0]==0:
                return val
            k_l[0] -= 1
            if k_l[0]==0:
                return node.val
            return self.kthSmallestStep(node.right,k_l)
        else:
            return -1 # dummy return value
