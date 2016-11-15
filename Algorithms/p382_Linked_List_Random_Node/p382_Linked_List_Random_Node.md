Given a singly linked list, return a random node's value from the linked list. Each node must have the same probability of being chosen.

Follow up:
What if the linked list is extremely large and its length is unknown to you? Could you solve this efficiently without using extra space?

Example:

// Init a singly linked list [1,2,3].
ListNode head = new ListNode(1);
head.next = new ListNode(2);
head.next.next = new ListNode(3);
Solution solution = new Solution(head);

// getRandom() should return either 1, 2, or 3 randomly. Each element should have equal probability of returning.
solution.getRandom();

Solution:
traverse the list, save/overwrite the result with node i value in a probability of p[i] (q[i]=1-p[i])
then
p(v1)=p[1]q[2]q[3]...q[n]
p(v2)=p[2]q[3]...q[n]
...
p(v[n-1])=p[n-1]q[n]
p(v[n])=p[n]

because p(v[1])=p(v[2])=...=p(v[n])=1/n, so
p[i-1]q[i]=p[i]
p[i-1]=p[i]/(1-p[i])
then
p[i]=p[i+1]/(1-p[i+1])=p[i+2]/(1-2p[i+2])=...=p[i+k]/(1-kp[i+k])=1/(1/p[i+k]-k)
let k=n-i
p[i]=1/(1/p[n]-(n-i))=1/i