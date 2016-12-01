# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        if m==n:
            return head
        
        head0 = ListNode(None)
        head0.next = head
        p1 = head0
        i = 1
        while i<m:
            p1 = p1.next
            i += 1
        p2 = p1.next
        
        q1 = p2
        q2 = q1.next
        q3 = q2.next
        i += 1
        while i<=n:
            q2.next = q1
            q1 = q2
            q2 = q3
            if not q3:
                break
            q3 = q3.next
            i += 1
        p1.next = q1
        p2.next = q2
        return head0.next
