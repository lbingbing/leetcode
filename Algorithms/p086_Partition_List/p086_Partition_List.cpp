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
    ListNode* partition(ListNode* head, int x) {
        ListNode lt(0);
        ListNode gt_eq(0);
        ListNode* p1 = &lt;
        ListNode* p2 = &gt_eq;
        while(head){
            if(head->val<x){
                p1->next = head;
                p1 = head;
            }else{
                p2->next = head;
                p2 = head;
            }
            head = head->next;
        }
        p1->next = gt_eq.next;
        p2->next = 0;
        return lt.next ? lt.next : gt_eq.next;
    }
};
