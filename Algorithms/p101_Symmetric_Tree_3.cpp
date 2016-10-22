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
        if(!root) return 1;
        queue<pair<TreeNode*,TreeNode*>> q;
        q.emplace(root->left,root->right);
        while(!q.empty()){
            pair<TreeNode*,TreeNode*> node = q.front();
            q.pop();
            if(!node.first&&!node.second) continue;
            if(!node.first||!node.second) return 0;
            if(node.first->val!=node.second->val) return 0;
            q.emplace(node.first->left,node.second->right);
            q.emplace(node.first->right,node.second->left);
        }
        return 1;
    }
};
