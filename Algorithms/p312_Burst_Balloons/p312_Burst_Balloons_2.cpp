class Solution {
public:
    int maxCoins(vector<int>& nums) {
        int len = nums.size();
        nums.insert(nums.begin(),1);
        nums.push_back(1);
        vector<vector<int>> coin(len+2,vector<int>(len+2,-1));
        for(int i=1;i<=len+1;++i){
            coin[i][i-1] = 0;
        }
        return getMaxCoins(nums,coin,1,len);
    }
    int getMaxCoins(vector<int>& nums, vector<vector<int>>& coin, int i, int j){
        if(coin[i][j]==-1){
            for(int k=i;k<=j;++k){
                coin[i][j] = max(coin[i][j], nums[i-1]*nums[k]*nums[j+1]+getMaxCoins(nums,coin,i,k-1)+getMaxCoins(nums,coin,k+1,j));
            }
        }
        return coin[i][j];
    }
};
