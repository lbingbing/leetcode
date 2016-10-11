# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = []
        self.rightSideViewHelper(root,res,0)
        return res
        
    def rightSideViewHelper(self, root, res, level):
        if not root:
            return
        if level==len(res):
            res.append(root.val)
        self.rightSideViewHelper(root.right,res,level+1)
        self.rightSideViewHelper(root.left,res,level+1)
