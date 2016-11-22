# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head or not head.next:
            return True
        p1 = head
        p2 = p1.next
        p3 = p2.next
        fast = p2
        p1.next = None
        while fast.next and fast.next.next:
            fast = fast.next.next
            p2.next = p1
            p1 = p2
            p2 = p3
            p3 = p3.next
        if fast.next:
            p2 = p3
        while p1:
            if p1.val!=p2.val:
                return False
            p1 = p1.next
            p2 = p2.next
        return True
