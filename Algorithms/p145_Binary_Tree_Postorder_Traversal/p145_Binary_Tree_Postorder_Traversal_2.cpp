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
    vector<int> postorderTraversal(TreeNode* root) {
        typedef pair<TreeNode*,bool> TreeNodePair; // second: childs visited
        vector<int> res;
        vector<TreeNodePair> stack;
        TreeNodePair cur(root,0);
        while(1){
            if(cur.first){
                if(!cur.second){
                    stack.push_back(TreeNodePair(cur.first,1));
                    stack.push_back(TreeNodePair(cur.first->right,0));
                    cur = TreeNodePair(cur.first->left,0);
                }else{
                    res.push_back(cur.first->val);
                    cur.first = 0;
                }
            }else{
                if(!stack.empty()){
                    cur = stack.back();
                    stack.pop_back();
                }else{
                    break;
                }
            }
        }
        return res;
    }
};
