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
        stack<TreeNode*,vector<TreeNode*>> stack1;
        stack<TreeNode*,vector<TreeNode*>> stack2;
        TreeNode* cur1 = root;
        TreeNode* cur2 = root;
        while(1){
            if(cur1&&cur2){
                if(cur1->val!=cur2->val) return 0;
                stack1.push(cur1->right);
                stack2.push(cur2->left);
                cur1 = cur1->left;
                cur2 = cur2->right;
            }else if(!cur1&&!cur2){
                if(stack1.empty()&&stack2.empty()) break;
                if(stack1.empty()||stack2.empty()) return 0;
                cur1 = stack1.top();
                cur2 = stack2.top();
                stack1.pop();
                stack2.pop();
            }else{
                return 0;
            }
        }
        return 1;
    }
};
