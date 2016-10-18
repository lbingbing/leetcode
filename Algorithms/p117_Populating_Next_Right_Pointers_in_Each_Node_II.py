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
        left_most1 = root
        while True:
            while left_most1 and not left_most1.left and not left_most1.right:
                left_most1 = left_most1.next
            if not left_most1:
                break
            left_most2 = left_most1.left if left_most1.left else left_most1.right
            p1 = left_most1
            p2 = left_most2
            if p2==p1.left and p1.right:
                p2.next = p1.right
                p2 = p2.next
            while True:
                p1 = p1.next
                if not p1:
                    break
                if p1.left:
                    p2.next = p1.left
                    p2 = p2.next
                if p1.right:
                    p2.next = p1.right
                    p2 = p2.next
            left_most1 = left_most2
