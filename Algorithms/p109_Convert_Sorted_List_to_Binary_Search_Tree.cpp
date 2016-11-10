/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
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
    TreeNode* sortedListToBST(ListNode* head) {
        int length = 0;
        for(ListNode* p = head;p;p=p->next,++length);
        return sortedListToBSTHelper(head,length);
    }
    TreeNode* sortedListToBSTHelper(ListNode* head, int length) {
        if(length==0) return 0;
        int mid_index = length/2;
        ListNode* mid_p = head;
        for(int i=0;i<mid_index;++i){
            mid_p = mid_p->next;
        }
        TreeNode* root = new TreeNode(mid_p->val);
        root->left = sortedListToBSTHelper(head,mid_index);
        root->right = sortedListToBSTHelper(mid_p->next,length-mid_index-1);
        return root;
    }
};
