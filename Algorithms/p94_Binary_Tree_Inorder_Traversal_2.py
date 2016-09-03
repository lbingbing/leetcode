# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = []
        stack = []
        while True:
            if root:
                stack.append(root)
                root = root.left
            else:
                if stack:
                    res.append(stack[-1].val)
                    root = stack[-1].right
                    stack.pop()
                else:
                    break
        return res
