class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int len = prices.size();
        if(len<=1){
            return 0;
        }
        
        vector<int> mins(len-1,prices[0]);
        vector<int> maxs(len-1,prices[len-1]);
        for(int i=1;i<len-1;++i){
            mins[i] = min(prices[i],mins[i-1]);
        }
        for(int i=len-3;i>=0;--i){
            maxs[i] = max(prices[i+1],maxs[i+1]);
        }
        int res = 0;
        for(int i=0;i<len-1;++i){
            res = max(maxs[i]-mins[i],res);
        }
        return res;
    }
};
