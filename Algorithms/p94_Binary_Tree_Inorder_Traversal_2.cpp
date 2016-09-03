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
        vector<TreeNode*> stack;
        while(1){
            if(root){
                stack.push_back(root);
                root = root->left;
            }else{
                if(!stack.empty()){
                    res.push_back((stack.back())->val);
                    root = (stack.back())->right;
                    stack.pop_back();
                }else{
                    break;
                }
            }
        }
        return res;
    }
};
