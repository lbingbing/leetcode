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
    vector<int> inorderTraversal(TreeNode* root) {
        vector<int> res;
        if(root){
            inorderTraversalStep(root,res);
        }
        return res;
    }
    void inorderTraversalStep(TreeNode* root, vector<int>& res) {
        if(root){
            inorderTraversalStep(root->left,res);
            res.push_back(root->val);
            inorderTraversalStep(root->right,res);
        }
    }
};
