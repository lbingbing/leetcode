class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int len = prices.size();
        if(len==0){
            return 0;
        }
        
        vector<int> forward_max(len,0);
        int lowest = prices[0];
        for(int i=1;i<len;++i){
            forward_max[i] = max(forward_max[i-1],prices[i]-lowest);
            lowest = min(lowest,prices[i]);
        }
        
        vector<int> backward_max(len,0);
        int highest = prices[len-1];
        for(int i=len-2;i>=0;--i){
            backward_max[i] = max(backward_max[i+1],highest-prices[i]);
            highest = max(highest,prices[i]);
        }
        
        int res = 0;
        for(int i=0;i<len;++i){
            res = max(res,forward_max[i]+backward_max[i]);
        }
        return res;
    }
};
