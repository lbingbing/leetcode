# Definition for a  binary tree node
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class BSTIterator(object):
    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.my_stack = []
        while root:
            self.my_stack.append(root)
            root = root.left

    def hasNext(self):
        """
        :rtype: bool
        """
        return bool(self.my_stack)

    def next(self):
        """
        :rtype: int
        """
        val = None
        if self.my_stack:
            p = self.my_stack.pop()
            val = p.val
            p = p.right
            while p:
                self.my_stack.append(p)
                p = p.left
        return val

# Your BSTIterator will be called like this:
# i, v = BSTIterator(root), []
# while i.hasNext(): v.append(i.next())
