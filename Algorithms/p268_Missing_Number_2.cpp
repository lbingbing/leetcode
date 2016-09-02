class Solution {
public:
    int missingNumber(vector<int>& nums) {
        int sum = 0;
        int sum_exp = 0;
        int len = nums.size();
        int i;
        for(i=0;i<len;i++){
            sum += nums[i];
            sum_exp += i;
        }
        return sum_exp+i-sum;
    }
};
