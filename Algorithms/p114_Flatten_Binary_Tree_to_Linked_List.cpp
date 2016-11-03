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
    void flatten(TreeNode* root) {
        flattenDFS(root);
    }
    TreeNode* flattenDFS(TreeNode* root) {
        if(!root) return 0;
        TreeNode* l_tail = flattenDFS(root->left);
        TreeNode* r_tail = flattenDFS(root->right);
        if(root->left){
            l_tail->right = root->right;
            root->right = root->left;
            root->left = 0;
        }
        return r_tail ? r_tail : l_tail ? l_tail : root;
    }
};
