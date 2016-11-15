# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        length = 0
        p = head
        while p:
            p = p.next
            length += 1
        return self.sortedListToBSTHelper(head,length)

    def sortedListToBSTHelper(self, head, length):
        if length==0:
            return None
        mid_index = (length-1)//2
        mid_p = head
        for i in range(mid_index):
            mid_p = mid_p.next
        root = TreeNode(mid_p.val)
        root.left = self.sortedListToBSTHelper(head,mid_index)
        root.right = self.sortedListToBSTHelper(mid_p.next,length-mid_index-1)
        return root
