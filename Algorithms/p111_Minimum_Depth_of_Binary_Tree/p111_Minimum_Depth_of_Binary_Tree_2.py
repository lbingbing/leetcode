# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        depth = 0
        q = collections.deque()
        q.append(root)
        while q:
            depth += 1
            done = False
            size = len(q)
            for i in range(size):
                node = q.popleft()
                if not node.left and not node.right:
                    done = True
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            if done:
                break
        return depth
