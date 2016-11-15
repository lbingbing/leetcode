/**
 * Definition for binary tree with next pointer.
 * struct TreeLinkNode {
 *  int val;
 *  TreeLinkNode *left, *right, *next;
 *  TreeLinkNode(int x) : val(x), left(NULL), right(NULL), next(NULL) {}
 * };
 */
class Solution {
public:
    void connect(TreeLinkNode *root) {
        for(TreeLinkNode* left_most1=root;;){
            for(;left_most1 && !left_most1->left && !left_most1->right;left_most1=left_most1->next) ;
            if(!left_most1) break;
            TreeLinkNode* left_most2 = left_most1->left ? left_most1->left : left_most1->right;
            TreeLinkNode* p1 = left_most1;
            TreeLinkNode* p2 = left_most2;
            if(p2==p1->left && p1->right){
                p2->next = p1->right;
                p2 = p2->next;
            }
            for(p1=p1->next;p1;p1=p1->next){
                if(p1->left){
                    p2->next = p1->left;
                    p2 = p2->next;
                }
                if(p1->right){
                    p2->next = p1->right;
                    p2 = p2->next;
                }
            }
            left_most1 = left_most2;
        }
    }
};
