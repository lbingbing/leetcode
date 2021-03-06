# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        head0 = ListNode(None)
        head0.next = head
        p = head0
        while p.next:
            if p.next.val==val:
                p.next = p.next.next
            else:
                p = p.next
        return head0.next
