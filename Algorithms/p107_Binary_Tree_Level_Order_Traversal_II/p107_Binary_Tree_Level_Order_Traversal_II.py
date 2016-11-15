# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        res = []
        q = collections.deque([root])
        while q:
            res.append([])
            size = len(q)
            for i in range(0,size):
                res[-1].append(q[0].val)
                if q[0].left:
                    q.append(q[0].left)
                if q[0].right:
                    q.append(q[0].right)
                q.popleft()
        res.reverse()
        return res
