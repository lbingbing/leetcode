# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        len_a = 0
        p = headA
        while p:
            len_a += 1
            p = p.next
        len_b = 0
        p = headB
        while p:
            len_b += 1
            p = p.next
        pa = headA
        pb = headB
        if len_a>len_b:
            for i in range(len_a-len_b):
                pa = pa.next
        elif len_b>len_a:
            for i in range(len_b-len_a):
                pb = pb.next
        while pa!=pb:
            pa = pa.next
            pb = pb.next
        return pa
