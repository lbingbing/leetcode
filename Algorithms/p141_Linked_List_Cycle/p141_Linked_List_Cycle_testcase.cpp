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
    cout<<s.hasCycle(0)<<endl;
    cout<<s.hasCycle(t1)<<endl;

    return 0;
}
