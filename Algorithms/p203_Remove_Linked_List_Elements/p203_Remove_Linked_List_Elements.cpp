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
    ListNode* removeElements(ListNode* head, int val) {
        ListNode** pp = &head;
        while(*pp){
            if((*pp)->val==val){
                // save and free *pp
                *pp = (*pp)->next;
            }else{
                pp = &(*pp)->next;
            }
        }
        return head;
    }
};
