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
        stack = []
        while True:
            if root:
                stack.append(root)
                root = root.left
            else:
                k -= 1
                if k==0:
                    res = stack[-1].val
                    break
                root = stack[-1].right
                stack.pop()
        return res
