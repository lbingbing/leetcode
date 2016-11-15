# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        stack1 = []
        stack2 = []
        cur1 = root
        cur2 = root
        while True:
            if cur1 and cur2:
                if cur1.val!=cur2.val:
                    return False
                stack1.append(cur1.right)
                stack2.append(cur2.left)
                cur1 = cur1.left
                cur2 = cur2.right
            elif not cur1 and not cur2:
                if not stack1 and not stack2:
                    break
                if not stack1 or not stack2:
                    return False
                cur1 = stack1.pop()
                cur2 = stack2.pop()
            else:
                return False
        return True
