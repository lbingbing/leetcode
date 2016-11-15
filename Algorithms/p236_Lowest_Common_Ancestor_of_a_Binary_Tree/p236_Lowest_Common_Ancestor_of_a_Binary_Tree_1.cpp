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
    TreeNode* lowestCommonAncestor(TreeNode* root, TreeNode* p, TreeNode* q) {
        vector<pair<TreeNode*,int>> path;
        int found = 0;
        getNodePath(root,p,q,path,found);
        TreeNode* res = 0;
        for(const auto& e : path){
            if(e.second==0){
                res = e.first;
            }else{
                break;
            }
        }
        return res;
    }
    void getNodePath(TreeNode* root, TreeNode* p, TreeNode* q, vector<pair<TreeNode*,int>>& path, int& found){
        if(root){
            path.push_back({root,found});
            if(root==p) ++found;
            if(root==q) ++found;
            if(found<2) getNodePath(root->left,p,q,path,found);
            if(found<2) getNodePath(root->right,p,q,path,found);
            if(found<2) path.pop_back();
        }
    }
};
