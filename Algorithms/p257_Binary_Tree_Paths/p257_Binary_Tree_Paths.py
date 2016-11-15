# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {string[]}
    def binaryTreePaths(self, root):
        res = []
        cur_path = []
        if root:
            self.binaryTreePathsDFS(res,cur_path,root)
        return res

    def binaryTreePathsDFS(self, res, cur_path, root):
        cur_path.append(str(root.val))
        if not root.left and not root.right:
            res.append('->'.join(cur_path))
            return
        if root.left:
            self.binaryTreePathsDFS(res,cur_path,root.left)
            cur_path.pop()
        if root.right:
            self.binaryTreePathsDFS(res,cur_path,root.right)
            cur_path.pop()
