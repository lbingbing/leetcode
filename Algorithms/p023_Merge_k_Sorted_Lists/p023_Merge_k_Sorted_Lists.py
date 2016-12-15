# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        head = ListNode(None)
        tail = head
        heap = []
        for e in lists:
            if e:
                heapq.heappush(heap,(e.val,e))
        while heap:
            tail.next = heap[0][1]
            heapq.heappop(heap)
            tail = tail.next
            if tail.next:
                heapq.heappush(heap,(tail.next.val,tail.next))
        return head.next
