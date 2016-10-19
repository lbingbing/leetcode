class Solution {
public:
    vector<int> lexicalOrder(int n) {
        vector<int> res(n);
        int i = 0;
        int m = 1;
        while(i<n){
            res[i++] = m;
            m *= 10;
            while(m>n){
                m /= 10;
                ++m;
                while(m%10==0) m /= 10;
            }
        }
        return res;
    }
};
