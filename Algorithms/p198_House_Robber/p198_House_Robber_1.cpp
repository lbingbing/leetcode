class Solution {
public:
    int rob(vector<int>& nums) {
        int res1 = 0;
        int res2 = 0;
        for(int i=0;i<nums.size();++i){
            int tmp = res2;
            res2 = max(res1+nums[i],res2);
            res1 = tmp;
        }
        return res2;
    }
};
