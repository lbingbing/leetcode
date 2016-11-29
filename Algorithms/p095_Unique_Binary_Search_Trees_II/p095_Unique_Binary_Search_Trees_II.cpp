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
    vector<TreeNode*> generateTrees(int n) {
        if(n==0) return {};
        vector<vector<TreeNode*>> table(n+1);
        table[0].push_back(0);
        for(int i=1;i<=n;++i){
            for(int j=0;j<i;++j){
                for(auto t1 : table[j]){
                    for(auto t2 : table[i-1-j]){
                        TreeNode* root = new TreeNode(0);
                        int id = 0;
                        root->left = copyTree(t1,id);
                        root->val = ++id;
                        root->right = copyTree(t2,id);
                        table[i].push_back(root);
                    }
                }
            }
        }
        return table[n];
    }
    TreeNode* copyTree(TreeNode* root, int& id) {
        if(!root) return 0;
        TreeNode* root1 = new TreeNode(0);
        root1->left = copyTree(root->left,id);
        root1->val = ++id;
        root1->right = copyTree(root->right,id);
        return root1;
    }
};
