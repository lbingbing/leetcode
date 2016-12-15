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
    ListNode* mergeKLists(vector<ListNode*>& lists) {
        ListNode head(0);
        ListNode* tail = &head;
        auto cmp = [&](ListNode* a, ListNode* b){ return a->val>b->val; };
        priority_queue<ListNode*,vector<ListNode*>,decltype(cmp)> heap(cmp);
        for(auto e : lists){
            if(e) heap.push(e);
        }
        while(!heap.empty()){
            tail->next = heap.top();
            heap.pop();
            tail = tail->next;
            if(tail->next) heap.push(tail->next);
        }
        return head.next;
    }
};
