class Solution {
public:
    int maxSubArray(vector<int>& nums) {
        if(nums.size()==1) return nums[0];
        // res0: max within [0,i] when not ending with nums[i]
        // res1: max within [0,i] when ending with nums[i]
        int res0 = nums[0];
        int res1 = nums[1]+max(nums[0],0);
        for(int i=2;i<nums.size();++i){
            res0 = max(res0,res1);
            res1 = nums[i]+max(res1,0);
        }
        return max(res0,res1);
    }
};
