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
    vector<vector<int>> zigzagLevelOrder(TreeNode* root) {
        if(!root) return {};
        vector<vector<int>> res;
        deque<TreeNode*> q;
        bool forward = 1;
        q.push_back(root);
        while(!q.empty()){
            res.push_back({});
            int size = q.size();
            for(int i=0;i<size;++i){
                TreeNode* p;
                if(forward){
                    p = q.front();
                    q.pop_front();
                    if(p->left) q.push_back(p->left);
                    if(p->right) q.push_back(p->right);
                }else{
                    p = q.back();
                    q.pop_back();
                    if(p->right) q.push_front(p->right);
                    if(p->left) q.push_front(p->left);
                }
                res.back().push_back(p->val);
            }
            forward = !forward;
        }
        return res;
    }
};
