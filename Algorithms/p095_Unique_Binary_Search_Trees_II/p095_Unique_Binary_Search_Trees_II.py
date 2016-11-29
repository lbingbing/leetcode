# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        if n==0:
            return []
        table = [[] for i in range(n+1)]
        table[0].append(None)
        for i in range(1,n+1):
            for j in range(i):
                for t1 in table[j]:
                    for t2 in table[i-1-j]:
                        root = TreeNode(0)
                        idx = [0]
                        root.left = self.copyTree(t1,idx)
                        idx[0] += 1
                        root.val = idx[0]
                        root.right = self.copyTree(t2,idx)
                        table[i].append(root)
        return table[n]

    def copyTree(self, root, idx):
        if not root:
            return None
        root1 = TreeNode(0)
        root1.left = self.copyTree(root.left,idx)
        idx[0] += 1
        root1.val = idx[0]
        root1.right = self.copyTree(root.right,idx)
        return root1
