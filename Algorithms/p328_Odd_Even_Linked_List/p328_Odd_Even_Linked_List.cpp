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
    ListNode* oddEvenList(ListNode* head) {
        if(head && head->next){
            ListNode* odd = head;
            ListNode* even_head = head->next;
            ListNode* even = even_head;
            while(even){
                odd->next = even->next;
                if(odd->next){
                    odd = odd->next;
                }else{
                    break;
                }
                even->next = odd->next;
                even = even->next;
            }
            odd->next = even_head;
        }
        return head;
    }
};
