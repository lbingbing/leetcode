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
    TreeNode* buildTree(vector<int>& preorder, vector<int>& inorder) {
        unordered_map<int,int> index;
        for(int i=0;i<inorder.size();++i) index[inorder[i]] = i;
        return buildTreeHelper(preorder,0,preorder.size(),inorder,0,inorder.size(),index);
    }
    TreeNode* buildTreeHelper(vector<int>& preorder, int l1, int r1, vector<int>& inorder, int l2, int r2, unordered_map<int,int>& index) {
        if(l1>=r1) return 0;
        int i = index[preorder[l1]];
        TreeNode* root = new TreeNode(inorder[i]);
        root->left = buildTreeHelper(preorder,l1+1,l1+1+i-l2,inorder,l2,i,index);
        root->right = buildTreeHelper(preorder,l1+1+i-l2,r1,inorder,i+1,r2,index);
        return root;
    }
};
