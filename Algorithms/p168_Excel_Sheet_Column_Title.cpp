class Solution {
public:
    string convertToTitle(int n) {
        string res;
        while(1){
            n--;
            res += 'A'+n%26;
            n = n/26;
            if(!n){
                break;
            }
        }
        reverse(res.begin(),res.end());
        return res;
    }
};
