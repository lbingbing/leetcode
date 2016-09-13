class Solution {
public:
    int maxProfit(vector<int>& prices) {
        if(prices.size()<=1){
            return 0;
        }
        
        int res = 0;
        int min = prices[0];
        for(int i=1;i<prices.size();++i){
            if(prices[i]>min){
                res = max(prices[i]-min,res);
            }else{
                min = prices[i];
            }
        }
        return res;
    }
};
