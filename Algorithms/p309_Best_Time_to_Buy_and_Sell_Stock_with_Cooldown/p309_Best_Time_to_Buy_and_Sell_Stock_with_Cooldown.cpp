class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int l = prices.size();
        if(l<=1) return 0;
        vector<int> s0(l); // not holding
        vector<int> s1(l); // holding
        vector<int> s2(l); // just sold
        s0[0] = 0;
        s1[0] = -prices[0];
        for(int i=1;i<l;++i){
            s0[i] = i>1 ? max(s0[i-1],s2[i-1]) : s0[0];
            s1[i] = max(s0[i-1]-prices[i],s1[i-1]);
            s2[i] = s1[i-1]+prices[i];
        }
        return max(s0[l-1],s2[l-1]);
    }
};
