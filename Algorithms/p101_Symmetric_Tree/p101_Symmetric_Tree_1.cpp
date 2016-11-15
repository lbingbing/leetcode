/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class Solution {
public:
    bool isSymmetric(TreeNode* root) {
        return !root || isSymmetricHelper(root->left,root->right);
    }
    bool isSymmetricHelper(TreeNode* t1, TreeNode* t2) {
        return !t1&&!t2 || t1&&t2&&t1->val==t2->val&&isSymmetricHelper(t1->left,t2->right)&&isSymmetricHelper(t1->right,t2->left);
    }
};
