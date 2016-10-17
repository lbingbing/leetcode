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
        if(!root) return;
        for(TreeLinkNode* left_most=root;left_most->left;left_most=left_most->left){
            for(TreeLinkNode* p=left_most;;p=p->next){
                p->left->next = p->right;
                if(!p->next) break;
                p->right->next = p->next->left;
            }
        }
    }
};
