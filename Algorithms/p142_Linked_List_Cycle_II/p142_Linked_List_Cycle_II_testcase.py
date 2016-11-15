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
res0 = s.detectCycle(None)
res1 = s.detectCycle(t1)
print(res0.val if res0 else 0)
print(res1.val if res1 else 0)
