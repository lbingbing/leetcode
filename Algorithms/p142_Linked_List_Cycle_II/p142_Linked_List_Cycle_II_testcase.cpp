int main(){
    ListNode* t1 = new ListNode(1);
    ListNode* t2 = new ListNode(2);
    ListNode* t3 = new ListNode(3);
    ListNode* t4 = new ListNode(4);
    ListNode* t5 = new ListNode(5);
    t1->next = t2;
    t2->next = t3;
    t3->next = t4;
    t4->next = t5;
    t5->next = t3;

    Solution s;
    ListNode* res0 = s.detectCycle(0);
    ListNode* res1 = s.detectCycle(t1);
    cout<<(res0?res0->val:0)<<endl;
    cout<<(res1?res1->val:0)<<endl;

    return 0;
}
