class Solution {
public:
    int missingNumber(vector<int>& nums) {
        int len = nums.size();
        vector<int> cnt(len+1);
        for(int v : nums){
            cnt[v] = 1;
        }
        for(int i=0;i<=len;i++){
            if(!cnt[i]){
                return i;
            }
        }
        return -1;
    }
};
