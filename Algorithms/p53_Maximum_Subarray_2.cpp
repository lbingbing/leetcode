class Solution {
public:
    int maxSubArray(vector<int>& nums) {
        if(nums.size()==1) return nums[0];
        pair<int,int> res = getMaxSubArray(nums,nums.size()-1);
        return max(res.first,res.second);
    }
    // first: max within [0,i] when not ending with nums[i]
    // second: max within [0,i] when ending with nums[i]
    pair<int,int> getMaxSubArray(vector<int>& nums, int i){
        if(i>=2){
            pair<int,int> res = getMaxSubArray(nums,i-1);
            return {max(res.first,res.second),nums[i]+max(res.second,0)};
        }else{
            return {nums[0],nums[1]+max(nums[0],0)};
        }
    }
};
