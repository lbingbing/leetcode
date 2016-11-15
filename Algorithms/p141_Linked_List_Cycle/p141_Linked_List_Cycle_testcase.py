t1 = ListNode(1)
t2 = ListNode(2)
t3 = ListNode(3)
t4 = ListNode(4)
t5 = ListNode(5)
t1.next = t2
t2.next = t3
t3.next = t4
t4.next = t5
t5.next = t3

s = Solution()
print(s.hasCycle(None))
print(s.hasCycle(t1))
