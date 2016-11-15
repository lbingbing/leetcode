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
        q = collections.deque([(root.left,root.right)])
        while q:
            node = q.popleft()
            if not node[0] and not node[1]:
                continue
            if not node[0] or not node[1]:
                return False
            if node[0].val!=node[1].val:
                return False
            q.append((node[0].left,node[1].right))
            q.append((node[0].right,node[1].left))
        return True
