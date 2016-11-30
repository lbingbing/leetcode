#include <iostream>
#include <vector>

using std::cout;
using std::endl;
using std::vector;

int main(){
    ListNode* pa1 = new ListNode(11);
    ListNode* pa2 = new ListNode(12);
    ListNode* pb1 = new ListNode(21);
    ListNode* pb2 = new ListNode(22);
    ListNode* pc1 = new ListNode(31);
    ListNode* pc2 = new ListNode(32);
    ListNode* pd1 = new ListNode(41);
    ListNode* pe1 = new ListNode(51);
    pa1->next = pa2;
    pa2->next = pc1;
    pb1->next = pb2;
    pb2->next = pc1;
    pc1->next = pc2;

    vector<vector<ListNode*>> inputs =
        {
         {pa1,pb1},
         {pa2,pb1},
         {pa1,pb2},
         {pa1,pc1},
         {pc1,pa1},
         {pb1,pc1},
         {pc1,pb1},
         {pa1,pc2},
         {pc2,pa1},
         {pb1,pc2},
         {pc2,pb1},
         {0,pb2},
         {pa1,0},
         {0,0},
         {pd1,pe1},
        };

    Solution s;
    for(auto e : inputs){
        ListNode* p = s.getIntersectionNode(e[0],e[1]);
        if(p){
            cout<<p->val<<endl;
        }else{
            cout<<"null"<<endl;
        }
    }
    return 0;
}
