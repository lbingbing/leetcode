class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        int len = nums.size();
        vector<int> res(nums);
        res[0] = 1;
        for(int i=1;i<len;i++){
            res[i] = res[i-1] * nums[i-1];
        }
        int r_product = nums[len-1];
        for(int i=len-2;i>=0;i--){
            res[i] *= r_product;
            r_product *= nums[i];
        }
        return res;
    }
};
