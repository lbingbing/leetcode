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
    TreeNode* sortedArrayToBST(vector<int>& nums) {
        return sortedArrayToBSTStep(nums,0,nums.size()-1);
    }
    TreeNode* sortedArrayToBSTStep(vector<int>& nums, int i, int j){
        if(i<=j){
            int mid = (i+j+1)/2;
            TreeNode* root = new TreeNode(nums[mid]);
            root->left = sortedArrayToBSTStep(nums,i,mid-1);
            root->right = sortedArrayToBSTStep(nums,mid+1,j);
            return root;
        }else{
            return 0;
        }
    }
};
