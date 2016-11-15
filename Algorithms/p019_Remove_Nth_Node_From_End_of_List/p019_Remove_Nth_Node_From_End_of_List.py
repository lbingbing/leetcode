# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        h = ListNode(None)
        h.next = head
        p1 = h
        p2 = head
        while n>1:
            p2 = p2.next
            n -= 1
        while p2.next:
            p1 = p1.next
            p2 = p2.next
        p1.next = p1.next.next
        return h.next
