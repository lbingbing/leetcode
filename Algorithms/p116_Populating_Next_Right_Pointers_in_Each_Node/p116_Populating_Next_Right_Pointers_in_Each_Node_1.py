# Definition for binary tree with next pointer.
# class TreeLinkNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None

class Solution:
    # @param root, a tree link node
    # @return nothing
    def connect(self, root):
        if not root or (not root.left and not root.right):
            return
        self.connect(root.left)
        self.connect(root.right)
        p = root.left
        q = root.right
        while p and q:
            p.next = q
            p = p.right
            q = q.left
