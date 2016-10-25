class Solution {
public:
    vector<int> getRow(int rowIndex) {
        vector<int> res(rowIndex+1,1);
        int old_v;
        int new_v;
        for(int i=1;i<=rowIndex;++i){
            old_v = res[0];
            for(int j=1;j<i;++j){
                new_v = old_v+res[j];
                old_v = res[j];
                res[j] = new_v;
            }
        }
        return res;
    }
};
