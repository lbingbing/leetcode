class Solution {
public:
    bool isValidSerialization(string preorder) {
        if(preorder.empty()) return 0;
        int cnt = 1;
        int pos = 0;
        while(pos!=string::npos&&cnt>0){
            pos = preorder.find_first_of(',',pos+1);
            if(pos!=string::npos&&preorder[pos-1]=='#' || pos==string::npos&&preorder[preorder.size()-1]=='#'){
                --cnt;
            }else{
                ++cnt;
            }
        }
        return pos==string::npos&&cnt==0;
    }
};
