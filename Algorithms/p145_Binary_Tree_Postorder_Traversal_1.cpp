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
    vector<int> postorderTraversal(TreeNode* root) {
        vector<int> res;
        postorderTraversalStep(root,res);
        return res;
    }
    void postorderTraversalStep(TreeNode* root, vector<int>& res) {
        if(root){
            postorderTraversalStep(root->left,res);
            postorderTraversalStep(root->right,res);
            res.push_back(root->val);
        }
    }
};
