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
    ListNode* reverseKGroup(ListNode* head, int k) {
        if(k<=1) return head;
        ListNode head0(0);
        head0.next = head;
        ListNode* tail = &head0;
        ListNode* p1 = head;
        while(1){
            ListNode* p2 = p1;
            int i = 0;
            for(;i<k&&p2;++i,p2=p2->next) ;
            if(i==k){
                ListNode* q1 = p1;
                ListNode* q2 = q1->next;
                ListNode* q3 = q2->next;
                while(1){
                    q2->next = q1;
                    if(q3==p2) break;
                    q1 = q2;
                    q2 = q3;
                    q3 = q3->next;
                }
                tail->next = q2;
                tail = p1;
                p1 = p2;
            }else{
                tail->next = p1;
                break;
            }
        }
        return head0.next;
    }
};
