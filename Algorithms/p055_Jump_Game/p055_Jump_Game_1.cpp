class Solution {
public:
    bool canJump(vector<int>& nums) {
        int min_reachable = nums.size()-1;
        for(int i=nums.size()-2;i>=0;--i){
            if(i+nums[i]>=min_reachable) min_reachable = i;
        }
        return min_reachable==0;
    }
};
