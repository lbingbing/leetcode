# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        res = []
        q = collections.deque([root])
        forward = True
        while q:
            res.append([])
            size = len(q)
            for i in range(size):
                if forward:
                    p = q.popleft()
                    if p.left:
                        q.append(p.left)
                    if p.right:
                        q.append(p.right)
                else:
                    p = q.pop()
                    if p.right:
                        q.appendleft(p.right)
                    if p.left:
                        q.appendleft(p.left)
                res[-1].append(p.val)
            forward = not forward
        return res
