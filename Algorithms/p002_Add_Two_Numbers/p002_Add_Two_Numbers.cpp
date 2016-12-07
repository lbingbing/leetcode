/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        ListNode head(0);
        ListNode* tail = &head;
        int carry = 0;
        while(l1||l2||carry){
            int op1 = l1?l1->val:0;
            int op2 = l2?l2->val:0;
            int res = op1+op2+carry;
            carry = (res>=10)?1:0;
            if(res>=10) res -= 10;
            tail->next = new ListNode(res);
            tail = tail->next;
            if(l1) l1 = l1->next;
            if(l2) l2 = l2->next;
        }
        return head.next;
    }
};
