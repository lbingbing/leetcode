class Solution {
public:
    int rob(vector<int>& nums) {
        if(nums.size()==0) return 0;
        if(nums.size()==1) return nums[0];
        if(nums.size()==2) return max(nums[0],nums[1]);
        // res0: no robbing on 1st day
        // res1: robbing on 1st day
        int res0_1 = 0;
        int res0_2 = nums[1];
        int res1_1 = nums[0];
        int res1_2 = nums[0];
        for(int i=2;i<nums.size();++i){
            int tmp = res0_1;
            res0_1 = res0_2;
            res0_2 = max(tmp+nums[i],res0_2);
            tmp = res1_1;
            res1_1 = res1_2;
            res1_2 = max(tmp+nums[i],res1_2);
        }
        return max(res0_2,res1_1);
    }
};
