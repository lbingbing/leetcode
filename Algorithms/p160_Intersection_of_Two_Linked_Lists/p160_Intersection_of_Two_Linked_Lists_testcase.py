pa1 = ListNode(11)
pa2 = ListNode(12)
pb1 = ListNode(21)
pb2 = ListNode(22)
pc1 = ListNode(31)
pc2 = ListNode(32)
pd1 = ListNode(41)
pe1 = ListNode(51)
pa1.next = pa2
pa2.next = pc1
pb1.next = pb2
pb2.next = pc1
pc1.next = pc2

inputs = (
          (pa1,pb1),
          (pa2,pb1),
          (pa1,pb2),
          (pa1,pc1),
          (pc1,pa1),
          (pb1,pc1),
          (pc1,pb1),
          (pa1,pc2),
          (pc2,pa1),
          (pb1,pc2),
          (pc2,pb1),
          (None,pb2),
          (pa1,None),
          (None,None),
          (pd1,pe1),
         )

s = Solution()
for p1,p2 in inputs:
    p = s.getIntersectionNode(p1,p2)
    if p:
        print(p.val)
    else:
        print('null')
