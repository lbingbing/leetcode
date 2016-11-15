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
    ListNode* removeNthFromEnd(ListNode* head, int n) {
        ListNode** pp = &head;
        ListNode* p = head;
        for(;n>1;--n){
            p = p->next;
        }
        while(p->next){
            pp = &(*pp)->next;
            p = p->next;
        }
        // save and free *pp
        *pp = (*pp)->next;
        return head;
    }
};
