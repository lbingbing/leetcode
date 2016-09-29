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
    int rob(TreeNode* root) {
        pair<int,int> res = robHelper(root);
        return max(res.first,res.second);
    }
    // first: max when root not robbed, second: max when root robbed
    pair<int,int> robHelper(TreeNode* root){
        if(root){
            pair<int,int> left = root->left ? robHelper(root->left) : make_pair(0,0);
            pair<int,int> right = root->right ? robHelper(root->right) : make_pair(0,0);
            return {max(left.first,left.second)+max(right.first,right.second),root->val+left.first+right.first};
        }else{
            return {0,0};
        }
    }
};
