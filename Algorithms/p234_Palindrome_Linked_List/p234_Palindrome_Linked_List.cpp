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
    bool isPalindrome(ListNode* head) {
        if(!head||!head->next) return 1;
        ListNode* p1 = head;
        ListNode* p2 = p1->next;
        ListNode* p3 = p2->next;
        ListNode* fast = p2;
        p1->next = 0;
        while(fast->next&&fast->next->next){
            fast = fast->next->next;
            p2->next = p1;
            p1 = p2;
            p2 = p3;
            p3 = p3->next;
        }
        if(fast->next) p2 = p3;
        while(p1){
            if(p1->val!=p2->val) return 0;
            p1 = p1->next;
            p2 = p2->next;
        }
        return 1;
    }
};
