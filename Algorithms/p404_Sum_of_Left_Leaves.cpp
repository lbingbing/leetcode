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
    int sumOfLeftLeaves(TreeNode* root) {
        int res = 0;
        if(root){
            if(root->left){
                res += (!root->left->left && !root->left->right) ? root->left->val : sumOfLeftLeaves(root->left);
            }
            if(root->right){
                res += sumOfLeftLeaves(root->right);
            }
        }
        return res;
    }
};
