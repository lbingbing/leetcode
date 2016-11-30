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
    ListNode *getIntersectionNode(ListNode *headA, ListNode *headB) {
        int len_a = 0;
        for(ListNode* p=headA;p;p=p->next) ++len_a;
        int len_b = 0;
        for(ListNode* p=headB;p;p=p->next) ++len_b;
        ListNode* pa = headA;
        ListNode* pb = headB;
        if(len_a>len_b){
            for(int i=len_a-len_b;i>0;--i) pa = pa->next;
        }else if(len_b>len_a){
            for(int i=len_b-len_a;i>0;--i) pb = pb->next;
        }
        while(pa!=pb){
            pa = pa->next;
            pb = pb->next;
        }
        return pa;
    }
};
