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
        self.max_depth = 0
        if root:
            self.walk(root,1)
        return self.max_depth
        
    def walk(self,p,cur_depth):
        if cur_depth > self.max_depth:
            self.max_depth = cur_depth
        if p.left:
            self.walk(p.left,cur_depth+1)
        if p.right:
            self.walk(p.right,cur_depth+1)
