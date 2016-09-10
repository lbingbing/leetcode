class Solution {
public:
    int maxCoins(vector<int>& nums) {
        int len = nums.size();
        nums.insert(nums.begin(),1);
        nums.push_back(1);
        vector<vector<int>> coin(len+2,vector<int>(len+2,0));
        for(int l=0;l<len;++l){
            for(int i=1,j=i+l;j<=len;++i,++j){
                int coin_max = 0;
                for(int k=i;k<=j;++k){
                    coin_max = max(coin_max, nums[i-1]*nums[k]*nums[j+1]+coin[i][k-1]+coin[k+1][j]);
                }
                coin[i][j] = coin_max;
            }
        }
        return coin[1][len];
    }
};
