# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        index = {}
        for i in range(len(inorder)):
            index[inorder[i]] = i
        return self.buildTreeHelper(inorder,0,len(inorder),postorder,0,len(postorder),index)

    def buildTreeHelper(self, inorder, l1, r1, postorder, l2, r2, index):
        if l1>=r1:
            return None
        i = index[postorder[r2-1]]
        root = TreeNode(inorder[i])
        root.left = self.buildTreeHelper(inorder,l1,i,postorder,l2,l2+i-l1,index)
        root.right = self.buildTreeHelper(inorder,i+1,r1,postorder,l2+i-l1,r2-1,index)
        return root
