# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        l = []
        stack1 = []
        while True:
            if root:
                l.append(str(root.val))
                stack1.append(root.right)
                root = root.left
            else:
                l.append('#')
                if stack1:
                    root = stack1.pop()
                else:
                    break
            l.append(',')
        return ''.join(l)

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        stack1 = []
        head = TreeNode(None)
        cur = head
        left = True
        pos = 0
        while pos<len(data):
            if data[pos]!='#':
                end = pos
                while end<len(data) and data[end]!=',':
                    end += 1
                child = TreeNode(int(data[pos:end]))
                pos = end+1
                if left:
                    stack1.append(cur)
                    cur.left = child
                    cur = cur.left
                else:
                    cur.right = child
                    cur = cur.right
                    left = True
            else:
                pos += 2
                if left:
                    left = False
                else:
                    if stack1:
                        cur = stack1.pop()
        return head.left

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
