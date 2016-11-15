# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        path = []
        found = [0]
        self.getNodePath(root,p,q,path,found)
        res = None
        for e in path:
            if e[1]==0:
                res = e[0]
            else:
                break
        return res
        
    def getNodePath(self, root, p, q, path, found):
        if root:
            path.append((root,found[0]))
            if root==p:
                found[0] += 1
            if root==q:
                found[0] += 1
            if found[0]<2:
                self.getNodePath(root.left,p,q,path,found)
            if found[0]<2:
                self.getNodePath(root.right,p,q,path,found)
            if found[0]<2:
                del path[-1]
