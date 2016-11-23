/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class Codec {
public:

    // Encodes a tree to a single string.
    string serialize(TreeNode* root) {
        string str1;
        stack<TreeNode*> stack1;
        while(1){
            if(root){
                str1 += to_string(root->val);
                stack1.push(root->right);
                root = root->left;
            }else{
                str1 += '#';
                if(!stack1.empty()){
                    root = stack1.top();
                    stack1.pop();
                }else{
                    break;
                }
            }
            str1 += ',';
        }
        return str1;
    }

    // Decodes your encoded data to tree.
    TreeNode* deserialize(string data) {
        stack<TreeNode*> stack1;
        TreeNode head(0);
        TreeNode* cur = &head;
        bool left = 1;
        int pos = 0;
        while(pos<data.size()){
            if(data[pos]!='#'){
                int end = pos;
                while(end<data.size()&&data[end]!=',') ++end;
                TreeNode* child = new TreeNode(stoi(data.substr(pos,end-pos)));
                pos = end+1;
                if(left){
                    stack1.push(cur);
                    cur->left = child;
                    cur = cur->left;
                }else{
                    cur->right = child;
                    cur = cur->right;
                    left = 1;
                }
            }else{
                pos += 2;
                if(left){
                    left = 0;
                }else{
                    if(!stack1.empty()){
                        cur = stack1.top();
                        stack1.pop();
                    }
                }
            }
        }
        return head.left;
    }
};

// Your Codec object will be instantiated and called as such:
// Codec codec;
// codec.deserialize(codec.serialize(root));
