# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        lt = ListNode(None)
        gt_eq = ListNode(None)
        p1 = lt
        p2 = gt_eq
        while head:
            if head.val<x:
                p1.next = head
                p1 = head
            else:
                p2.next = head
                p2 = head
            head = head.next
        p1.next = gt_eq.next
        p2.next = None
        return lt.next if lt.next else gt_eq.next
