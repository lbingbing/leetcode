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
        return kthSmallestStep(root,k);
    }
    int kthSmallestStep(TreeNode* node, int& k){
        if(node){
            int val = kthSmallestStep(node->left,k);
            if(k==0){
                return val;
            }
            if(--k==0){
                return node->val;
            }
            return kthSmallestStep(node->right,k);
        }else{
            return -1; // dummy return value
        }
    }
};
