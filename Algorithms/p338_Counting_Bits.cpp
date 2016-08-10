class Solution {
public:
    vector<int> countBits(int num) {
        vector<int> res(num+1);
        res[0] = 0;
        int m = 1;
        int m2 = 2;
        for(int i=1;i<=num;i++){
            if(i<m2){
                res[i] = res[i-m] + 1;
            }else{
                res[i] = 1;
                m = m2;
                m2 = m*2;
            }
        }
        return res;
    }
};
