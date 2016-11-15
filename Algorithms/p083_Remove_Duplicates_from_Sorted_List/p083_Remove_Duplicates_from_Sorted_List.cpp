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
    ListNode* deleteDuplicates(ListNode* head) {
        if(!head) return 0;
        ListNode *p = head;
        while(p->next){
            if(p->next->val==p->val){
                ListNode *tmp = p->next;
                p->next = tmp->next;
                delete tmp;
            }else{
                p = p->next;
            }
        }
        return head;
    }
};
