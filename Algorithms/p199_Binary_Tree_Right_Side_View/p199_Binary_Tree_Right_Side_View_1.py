# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = []
        if root:
            queue = collections.deque()
            queue.append(root)
            while queue:
                res.append(queue[0].val)
                size = len(queue)
                for i in range(0,size):
                    if queue[0].right:
                        queue.append(queue[0].right)
                    if queue[0].left:
                        queue.append(queue[0].left)
                    queue.popleft()
        return res
