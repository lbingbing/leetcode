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
        if not root:
            return 
        left_most = root
        while left_most.left:
            p = left_most
            while True:
                p.left.next = p.right
                if not p.next:
                    break
                p.right.next = p.next.left
                p = p.next
            left_most = left_most.left
