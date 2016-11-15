class Solution {
public:
    vector<int> grayCode(int n) {
        int upper_bound = 1;
        for(int i=0;i<n;++i){
            upper_bound *= 2;
        }
        vector<int> res(upper_bound);
        for(int i=0;i<upper_bound;++i){
            for(int j=0;j<n;++j){
                res[i] |= ((i>>1)&(0x1<<j))^(i&(0x1<<j));
            }
        }
        return res;
    }
};
