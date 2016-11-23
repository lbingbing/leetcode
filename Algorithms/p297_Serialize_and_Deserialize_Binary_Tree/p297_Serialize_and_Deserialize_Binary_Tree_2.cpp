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
        string str;
        queue<TreeNode*> q;
        if(root) q.push(root);
        while(!q.empty()){
            TreeNode* p = q.front();
            q.pop();
            if(p){
                str += to_string(p->val);
                q.push(p->left);
                q.push(p->right);
            }else{
                str += '#';
            }
            if(!q.empty()) str += ',';
        }
        return str;
    }

    // Decodes your encoded data to tree.
    TreeNode* deserialize(string data) {
        queue<TreeNode*> q;
        TreeNode head(0);
        TreeNode* cur = &head;
        bool left = 0;
        int pos = 0;
        while(pos<data.size()){
            if(data[pos]!='#'){
                int end = pos;
                while(end<data.size()&&data[end]!=',') ++end;
                TreeNode* child = new TreeNode(stoi(data.substr(pos,end-pos)));
                pos = end+1;
                q.push(child);
                if(left){
                    cur->left = child;
                    left = 0;
                }else{
                    cur->right = child;
                    cur = q.front();
                    q.pop();
                    left = 1;
                }
            }else{
                pos += 2;
                if(left){
                    left = 0;
                }else{
                    if(!q.empty()){
                        cur = q.front();
                        q.pop();
                    }
                    left = 1;
                }
            }
        }
        return head.right;
    }
};

// Your Codec object will be instantiated and called as such:
// Codec codec;
// codec.deserialize(codec.serialize(root));
