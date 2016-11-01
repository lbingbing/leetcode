class Solution {
public:
    int wiggleMaxLength(vector<int>& nums) {
        if(nums.empty()) return 0;
        int up = 1; // max length of sequences with increasing tail so far
        int down = 1; // max length of sequences with decreasing tail so far
        for(int i=1;i<nums.size();++i){
            if(nums[i]>nums[i-1]){
                up = down+1;
            }else if(nums[i]<nums[i-1]){
                down = up+1;
            }
        }
        return max(up,down);
    }
};
