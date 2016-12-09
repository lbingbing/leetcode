class Solution {
public:
    string convert(string s, int numRows) {
        if(numRows<=1) return s;
        int n = s.size();
        int m = numRows*2-2;
        string res;
        for(int i=0;i<n;i+=m){
            res += s[i];
        }
        for(int i=1;i<numRows-1;++i){
            for(int j=i,d=m-i*2;j<n;j+=d,d=m-d){
                res += s[j];
            }
        }
        for(int i=numRows-1;i<n;i+=m){
            res += s[i];
        }
        return res;
    }
};
