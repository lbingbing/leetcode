# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = []
        stack = []
        cur = (root,0) # [1]: childs visited
        while True:
            if cur[0]:
                if not cur[1]:
                    stack.append((cur[0],1))
                    stack.append((cur[0].right,0))
                    cur = (cur[0].left,0)
                else:
                    res.append(cur[0].val)
                    cur = (None,1)
            else:
                if stack:
                    cur = stack.pop()
                else:
                    break
        return res
