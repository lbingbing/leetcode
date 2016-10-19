# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        tmp = ListNode(0)
        tmp.next = head
        p = tmp
        q = tmp.next
        while q and q.next:
            p.next = q.next
            q.next = q.next.next
            p.next.next = q
            p = q
            q = q.next
        return tmp.next
