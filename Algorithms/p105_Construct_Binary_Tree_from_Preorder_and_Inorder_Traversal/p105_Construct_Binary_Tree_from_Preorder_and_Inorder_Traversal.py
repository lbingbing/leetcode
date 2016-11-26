# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        index = {}
        for i in range(len(inorder)):
            index[inorder[i]] = i
        return self.buildTreeHelper(preorder,0,len(preorder),inorder,0,len(inorder),index)

    def buildTreeHelper(self, preorder, l1, r1, inorder, l2, r2, index):
        if l1>=r1:
            return None
        i = index[preorder[l1]]
        root = TreeNode(inorder[i])
        root.left = self.buildTreeHelper(preorder,l1+1,l1+1+i-l2,inorder,l2,i,index)
        root.right = self.buildTreeHelper(preorder,l1+1+i-l2,r1,inorder,i+1,r2,index)
        return root
