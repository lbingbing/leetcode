# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        else:
            p1 = head
            p2 = p1.next
            p3 = p2.next
            p1.next = None
            while True:
                p2.next = p1
                if not p3:
                    break
                p1 = p2
                p2 = p3
                p3 = p3.next
            return p2
