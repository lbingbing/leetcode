# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head and head.next:
            odd = head
            even_head = head.next
            even = even_head
            while even:
                odd.next = even.next
                if odd.next:
                    odd = odd.next
                else:
                    break
                even.next = odd.next
                even = even.next
            odd.next = even_head
        return head
