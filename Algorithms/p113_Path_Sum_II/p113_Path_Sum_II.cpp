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
    vector<vector<int>> pathSum(TreeNode* root, int sum) {
        if(!root) return {};
        vector<vector<int>> res;
        vector<int> cur;
        dfs(res,cur,root,sum);
        return res;
    }
    void dfs(vector<vector<int>>& res, vector<int>& cur, TreeNode* root, int sum) {
        cur.push_back(root->val);
        sum -= root->val;
        if(root->left) dfs(res,cur,root->left,sum);
        if(root->right) dfs(res,cur,root->right,sum);
        if(!root->left&&!root->right&&sum==0) res.push_back(cur);
        cur.pop_back();
    }
};
