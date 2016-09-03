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
    ListNode* reverseList(ListNode* head) {
        if(!head || !head->next){
            return head;
        }else{
            ListNode* p1 = head;
            ListNode* p2 = p1->next;
            ListNode* p3 = p2->next;
            p1->next = 0;
            while(1){
                p2->next = p1;
                if(!p3){
                    break;
                }
                p1 = p2;
                p2 = p3;
                p3 = p3->next;
            }
            return p2;
        }
    }
};
