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
    int maxDepth(TreeNode* root) {
        int max_depth = 0;
        if(root){
            walk(root,1,max_depth);
        }
        return max_depth;
    }
    void walk(TreeNode* p, int cur_depth, int& max_depth){
        if(cur_depth>max_depth){
            max_depth = cur_depth;
        }
        if(p->left){
            walk(p->left,cur_depth+1,max_depth);
        }
        if(p->right){
            walk(p->right,cur_depth+1,max_depth);
        }
    }
};
