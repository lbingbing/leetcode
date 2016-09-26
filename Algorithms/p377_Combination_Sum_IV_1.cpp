class Solution {
public:
    int combinationSum4(vector<int>& nums, int target) {
        vector<int> table(target+1,-1);
        return getCombinationSum4(table,nums,target);
    }
    int getCombinationSum4(vector<int>& table, vector<int>& nums, int target) {
        if(table[target]==-1){
            table[target] = 0;
            for(int i=0;i<nums.size();++i){
                if(target>nums[i]){
                    table[target] += getCombinationSum4(table,nums,target-nums[i]);
                }else if(target==nums[i]){
                    table[target] += 1;
                }
            }
        }
        return table[target];
    }
};
