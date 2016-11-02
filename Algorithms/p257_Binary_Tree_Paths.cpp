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
    vector<string> binaryTreePaths(TreeNode* root) {
        vector<string> res;
        string cur_path;
        if(root) binaryTreePathsDFS(res,cur_path,root);
        return res;
    }
    void binaryTreePathsDFS(vector<string>& res, string& cur_path, TreeNode* root) {
        if(!cur_path.empty()) cur_path += "->";
        cur_path += to_string(root->val);
        if(!root->left&&!root->right){
            res.push_back(cur_path);
            return;
        }
        if(root->left){
            binaryTreePathsDFS(res,cur_path,root->left);
            cur_path.erase(cur_path.rfind('>')-1);
        }
        if(root->right){
            binaryTreePathsDFS(res,cur_path,root->right);
            cur_path.erase(cur_path.rfind('>')-1);
        }
    }
};
