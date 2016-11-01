class Solution {
public:
    int wiggleMaxLength(vector<int>& nums) {
        if(nums.empty()) return 0;
        int res = 1;
        int tail = 0; // 0:eq, 1:inc, 2:dec
        for(int i=1;i<nums.size();++i){
            if(nums[i]>nums[i-1]&&tail!=1){
                ++res;
                tail = 1;
            }else if(nums[i]<nums[i-1]&&tail!=2){
                ++res;
                tail = 2;
            }
        }
        return res;
    }
};
