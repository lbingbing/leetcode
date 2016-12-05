# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if k<=1:
            return head
        head0 = ListNode(None)
        head0.next = head
        tail = head0
        p1 = head
        while True:
            p2 = p1
            i = 0
            while i<k and p2:
                p2 = p2.next
                i += 1
            if i==k:
                q1 = p1
                q2 = q1.next
                q3 = q2.next
                while True:
                    q2.next = q1
                    if q3==p2:
                        break
                    q1 = q2
                    q2 = q3
                    q3 = q3.next
                tail.next = q2
                tail = p1
                p1 = p2
            else:
                tail.next = p1
                break
        return head0.next
