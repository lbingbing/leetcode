class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int res = 0;
        for(int i=0;i<prices.size();++i){ // i: first day for 2nd section
            res = max(maxProfitInRange(prices,0,i)+maxProfitInRange(prices,i,prices.size()),res);
        }
        return res;
    }
    int maxProfitInRange(vector<int>& prices, int i, int j){
        int res = 0;
        int low = prices[i];
        for(int k=i+1;k<j;++k){
            if(prices[k]>low){
                res = max(prices[k]-low,res);
            }else{
                low = prices[k];
            }
        }
        return res;
    }
};
