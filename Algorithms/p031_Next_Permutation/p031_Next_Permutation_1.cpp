class Solution {
public:
    void nextPermutation(vector<int>& nums) {
        int i = nums.size()-1-(is_sorted_until(nums.rbegin(),nums.rend())-nums.rbegin());
        if(i>=0){
            int j = lower_bound(nums.begin()+i+1,nums.end(),nums[i],greater<int>())-nums.begin()-1;
            swap(nums[i],nums[j]);
        }
        reverse(nums.begin()+i+1,nums.end());
    }
};
