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
    vector<int> rightSideView(TreeNode* root) {
        vector<int> res;
        rightSideViewHelper(root,res,0);
        return res;
    }
    void rightSideViewHelper(TreeNode* root, vector<int>& res, int level){
        if(!root) return;
        if(level==res.size()) res.push_back(root->val);
        rightSideViewHelper(root->right,res,level+1);
        rightSideViewHelper(root->left,res,level+1);
    }
};
