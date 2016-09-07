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
    int kthSmallest(TreeNode* root, int k) {
        int res;
        vector<TreeNode*> stack;
        while(1){
            if(root){
                stack.push_back(root);
                root = root->left;
            }else{
                if(--k==0){
                    res = (stack.back())->val;
                    break;
                };
                root = (stack.back())->right;
                stack.pop_back();
            }
        }
        return res;
    }
};
