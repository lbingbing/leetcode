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
        q = collections.deque()
        if root:
            q.append(root)
        while q:
            p = q.popleft()
            if p:
                l.append(str(p.val))
                q.append(p.left)
                q.append(p.right)
            else:
                l.append('#')
            if q:
                l.append(',')
        return ''.join(l)

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        q = collections.deque()
        head = TreeNode(None)
        cur = head
        left = False
        pos = 0
        while pos<len(data):
            if data[pos]!='#':
                end = pos
                while end<len(data) and data[end]!=',':
                    end += 1
                child = TreeNode(int(data[pos:end]))
                pos = end+1
                q.append(child)
                if left:
                    cur.left = child
                    left = False
                else:
                    cur.right = child
                    cur = q.popleft()
                    left = True
            else:
                pos += 2
                if left:
                    left = False
                else:
                    if q:
                        cur = q.popleft()
                    left = True
        return head.right

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
