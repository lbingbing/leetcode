# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        self.flattenDFS(root)

    def flattenDFS(self, root):
        if not root:
            return None
        l_tail = self.flattenDFS(root.left)
        r_tail = self.flattenDFS(root.right)
        if root.left:
            l_tail.right = root.right
            root.right = root.left
            root.left = None
        return r_tail if r_tail else l_tail if l_tail else root
