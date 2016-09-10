class Solution {
public:
    vector<string> generateParenthesis(int n) {
        vector<string> res;
        string cur_str;
        generateParenthesisStep(res,cur_str,n,n);
        return res;
    }
    void generateParenthesisStep(vector<string>& res, string& cur_str, int l, int r){
        if(l==0 && r==0){
            res.push_back(cur_str);
        }else{
            if(l){
                cur_str += "(";
                generateParenthesisStep(res,cur_str,l-1,r);
                cur_str.pop_back();
            }
            if(r>l){
                cur_str += ")";
                generateParenthesisStep(res,cur_str,l,r-1);
                cur_str.pop_back();
            }
        }
    }
};
