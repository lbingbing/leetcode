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
    vector<int> rightSideView(TreeNode* root) {
        vector<int> res;
        if(root){
            deque<TreeNode*> queue;
            queue.push_back(root);
            while(!queue.empty()){
                res.push_back(queue.front()->val);
                int size = queue.size();
                for(int i=0;i<size;++i){
                    if(queue.front()->right) queue.push_back(queue.front()->right);
                    if(queue.front()->left) queue.push_back(queue.front()->left);
                    queue.pop_front();
                }
            }
        }
        return res;
    }
};
