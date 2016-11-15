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
    int sumNumbers(TreeNode* root) {
        int res = 0;
        if(root) sumNumbersHelper(res,root,0);
        return res;
    }
    void sumNumbersHelper(int& res, TreeNode* root, int n) {
        int n1 = n*10+root->val;
        if(!root->left&&!root->right) res += n1;
        if(root->left) sumNumbersHelper(res,root->left,n1);
        if(root->right) sumNumbersHelper(res,root->right,n1);
    }
};
