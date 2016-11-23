# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        if not root:
            return []
        res = []
        cur = []
        self.dfs(res,cur,root,sum)
        return res

    def dfs(self, res, cur, root, sum):
        cur.append(root.val)
        sum -= root.val
        if root.left:
            self.dfs(res,cur,root.left,sum)
        if root.right:
            self.dfs(res,cur,root.right,sum)
        if not root.left and not root.right and sum==0:
            res.append(cur[:])
        cur.pop()
