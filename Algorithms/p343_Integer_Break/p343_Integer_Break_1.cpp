class Solution {
public:
    int integerBreak(int n) {
        vector<int> f(n+1);
        vector<int> g(n+1);
        g[1] = 1;
        for(int i=2;i<n+1;i++){
            int max = 0;
            for(int j=1;j<i;j++){
                int v = j*g[i-j];
                if(v>max){
                    max = v;
                }
            }
            f[i] = max;
            g[i] = max>i ? max : i;
        }
        return f[n];
    }
};
