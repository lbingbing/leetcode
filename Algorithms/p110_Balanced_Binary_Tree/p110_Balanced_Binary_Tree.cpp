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
    bool isBalanced(TreeNode* root) {
        return isBalancedHelper(root)!=-1;
    }
    int isBalancedHelper(TreeNode* root) {
        if(!root) return 0;
        int height_l = isBalancedHelper(root->left);
        if(height_l==-1) return -1;
        int height_r = isBalancedHelper(root->right);
        if(height_r==-1) return -1;
        int large = max(height_l,height_r);
        int small = min(height_l,height_r);
        return (large-small<=1) ? large+1 : -1;
    }
};
