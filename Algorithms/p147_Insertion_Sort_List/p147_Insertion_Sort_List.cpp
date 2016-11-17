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
    ListNode* insertionSortList(ListNode* head) {
        if(!head) return 0;
        ListNode** p_head = &head;
        ListNode* p1 = head->next;
        ListNode* p2;
        ListNode** pp;
        head->next = 0;
        while(p1){
            pp = p_head;
            while((*pp)&&(*pp)->val<p1->val) pp = &(*pp)->next;
            p2 = p1->next;
            p1->next = *pp;
            *pp = p1;
            p1 = p2;
        }
        return *p_head;
    }
};
