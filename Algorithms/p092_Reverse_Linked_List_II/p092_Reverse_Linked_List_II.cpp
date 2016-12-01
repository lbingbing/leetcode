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
    ListNode* reverseBetween(ListNode* head, int m, int n) {
        if(m==n) return head;
        
        ListNode head0(0);
        head0.next = head;
        ListNode* p1 = &head0;
        int i = 1;
        for(;i<m;++i) p1 = p1->next;
        ListNode* p2 = p1->next;
        
        ListNode* q1 = p2;
        ListNode* q2 = q1->next;
        ListNode* q3 = q2->next;
        ++i;
        while(i<=n){
            q2->next = q1;
            q1 = q2;
            q2 = q3;
            if(!q3) break;
            q3 = q3->next;
            ++i;
        }
        p1->next = q1;
        p2->next = q2;
        return head0.next;
    }
};
