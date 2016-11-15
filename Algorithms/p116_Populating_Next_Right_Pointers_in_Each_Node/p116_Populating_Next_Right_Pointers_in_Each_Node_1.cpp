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
        if(!root || !root->left&&!root->right) return;
        connect(root->left);
        connect(root->right);
        TreeLinkNode* p = root->left;
        TreeLinkNode* q = root->right;
        for(;p&&q;p=p->right,q=q->left){
            p->next=q;
        }
    }
};
