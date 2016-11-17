# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def insertionSortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return None
        head0 = ListNode(None)
        head0.next = head
        p1 = head.next
        head.next = None
        while p1:
            p = head0
            while p.next and p.next.val<p1.val:
                p = p.next
            p2 = p1.next
            p1.next = p.next
            p.next = p1
            p1 = p2
        return head0.next
