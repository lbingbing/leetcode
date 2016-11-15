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
    vector<int> preorderTraversal(TreeNode* root) {
        vector<int> res;
        vector<TreeNode*> stack;
        while(1){
            if(root){
                res.push_back(root->val);
                stack.push_back(root->right);
                root = root->left;
            }else{
                if(!stack.empty()){
                    root = stack.back();
                    stack.pop_back();
                }else{
                    break;
                }
            }
        }
        return res;
    }
};
