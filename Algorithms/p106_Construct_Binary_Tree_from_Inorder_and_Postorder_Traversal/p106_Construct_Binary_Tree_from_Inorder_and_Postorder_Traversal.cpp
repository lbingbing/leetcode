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
    TreeNode* buildTree(vector<int>& inorder, vector<int>& postorder) {
        unordered_map<int,int> index;
        for(int i=0;i<inorder.size();++i) index[inorder[i]] = i;
        return buildTreeHelper(inorder,0,inorder.size(),postorder,0,postorder.size(),index);
    }
    TreeNode* buildTreeHelper(vector<int>& inorder, int l1, int r1, vector<int>& postorder, int l2, int r2, unordered_map<int,int>& index) {
        if(l1>=r1) return 0;
        int i = index[postorder[r2-1]];
        TreeNode* root = new TreeNode(inorder[i]);
        root->left = buildTreeHelper(inorder,l1,i,postorder,l2,l2+i-l1,index);
        root->right = buildTreeHelper(inorder,i+1,r1,postorder,l2+i-l1,r2-1,index);
        return root;
    }
};
