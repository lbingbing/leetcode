class Solution {
public:
    int lengthOfLIS(vector<int>& nums) {
        if(nums.empty()) return 0;
        int n = nums.size();
        vector<int> table(n,1);
        for(int i=0;i<n;++i){
            for(int j=0;j<i;++j){
                if(nums[i]>nums[j]) table[i] = max(table[i],table[j]+1);
            }
        }
        return *max_element(table.begin(),table.end());
    }
};
